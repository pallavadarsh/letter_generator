from langgraph.graph import StateGraph
from langgraph.tracers import LangGraphTracer

def simple_node(state):
    print("Received state:", state)
    return state

def build_graph():
    g = StateGraph()
    g.add_node("step_1", simple_node)
    g.set_entry_point("step_1")
    return g

tracer = LangGraphTracer(project_name="Client AI Trace")

graph = build_graph().with_tracer(tracer).compile()

result = graph.invoke({"input": "test"})

print("Done running graph.")
print("LangGraph trace URL:", tracer.get_url())
