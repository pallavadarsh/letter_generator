
from langgraph.graph import StateGraph
from langgraph.tracers import LangGraphTrace

# GRAPH is bieing build here
def build_graph():
    graph = StateGraph()
    # Define your graph here: nodes, edges, entry, etc.
    return graph

#this runs the the entire agentic flow in langgraph
def run_agentic_workflow(input_data):
    tracer = LangGraphTracer(project_name="AI Patient Intake")
    graph = build_graph()
    graph = graph.with_tracer(tracer)
    compiled_graph = graph.compile()
    result = compiled_graph.invoke(input_data)
    trace_url = tracer.get_url()  # This returns the URL to visualize the trace

    return {
        "result": result,
        "trace_url": trace_url
    }
