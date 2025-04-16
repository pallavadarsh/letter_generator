from fastapi import APIRouter
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
import json

router = APIRouter()

class TraceEvent(BaseModel):
    step: int
    action: str
    input: str = ""
    output: str = ""
    group: str = "default"

class TraceUploadPayload(BaseModel):
    trace_id: str
    events: list[TraceEvent]

TRACE_STORE = {}

@router.post("/trace/upload")
async def upload_trace(payload: TraceUploadPayload):
    TRACE_STORE[payload.trace_id] = payload.events
    print(f"Trace received for ID: {payload.trace_id}")
    for event in payload.events:
        print(f"Step {event.step}: {event.action}")
    return JSONResponse(content={"message": "Trace uploaded successfully"})

@router.get("/trace/{trace_id}")
async def get_trace(trace_id: str):
    events = TRACE_STORE.get(trace_id)
    if not events:
        return JSONResponse(status_code=404, content={"error": "Trace not found"})

    grouped = {}
    for e in events:
        grouped.setdefault(e.group, []).append(e)

    all_graphs = ""
    for idx, (group_name, group_events) in enumerate(grouped.items()):
        nodes = []
        edges = []
        for i, e in enumerate(group_events):
            node_id = f"g{idx}_step{i+1}"
            color = "#28a745" if "summarize" in e.action.lower() else "#007BFF"
            if "generate" in e.action.lower():
                color = "#ffc107"
            nodes.append({"data": {"id": node_id, "label": e.action, "info": json.dumps(e.dict()), "color": color}})
            if i > 0:
                edges.append({"data": {"source": f"g{idx}_step{i}", "target": node_id}})

        graph_json = json.dumps(nodes + edges)

        graph_div = f"""
        <div style='width: 48%; height: 600px; display: inline-block; margin: 1%; vertical-align: top;'>
            <h3 style='text-align:center;'>Workflow: {group_name}</h3>
            <div id='cy{idx}' style='width: 100%; height: 550px;'></div>
        </div>
        <script>
            const cy{idx} = cytoscape({{
                container: document.getElementById('cy{idx}'),
                elements: {graph_json},
                style: [
                    {{ selector: 'node', style: {{
                        'label': 'data(label)',
                        'background-color': 'data(color)',
                        'color': 'white',
                        'font-size': '14px',
                        'text-valign': 'center',
                        'text-halign': 'center',
                        'text-wrap': 'wrap',
                        'text-max-width': 120,
                        'width': 140,
                        'height': 80
                    }} }},
                    {{ selector: 'edge', style: {{
                        'width': 2,
                        'line-color': '#ccc',
                        'target-arrow-color': '#ccc',
                        'target-arrow-shape': 'triangle'
                    }} }}
                ],
                layout: {{ name: 'breadthfirst', directed: true, padding: 10 }}
            }});

            cy{idx}.on('tap', 'node', function(evt) {{
                const data = JSON.parse(evt.target.data('info'));
                alert(`Step ${'{'}data.step{'}'}\nAction: ${'{'}data.action{'}'}\n\nInput: ${'{'}data.input || 'N/A'{'}'}\n\nOutput: ${'{'}data.output || 'N/A'{'}'}`);
            }});
        </script>
        """
        all_graphs += graph_div

    html_content = f"""
    <html>
    <head>
        <title>DAG Trace Viewer</title>
        <script src="https://unpkg.com/cytoscape@3.23.0/dist/cytoscape.min.js"></script>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; background: #f8f9fa; }}
            .legend span {{ display: inline-block; width: 16px; height: 16px; margin: 0 8px 0 16px; }}
        </style>
    </head>
    <body>
        <h2 style="margin-bottom: 10px;">Trace ID: {trace_id}</h2>
        <div class="legend" style="margin-bottom: 20px;">
            <strong>Legend:</strong>
            <span style="background-color: #ffc107;"></span> Generate
            <span style="background-color: #28a745;"></span> Summarize
            <span style="background-color: #007BFF;"></span> Other
        </div>
        {all_graphs}
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)
