
import React from "react";

const TraceViewer = ({ traceUrl }: { traceUrl: string }) => {
  return (
    <div className="bg-white rounded-lg shadow p-4 mt-4">
      <h2 className="text-lg font-semibold">Agent Workflow Trace</h2>
      <iframe
        src={traceUrl}
        className="w-full h-[500px] border mt-2"
        title="LangGraph Visual Trace"
      />
    </div>
  );
};

export default TraceViewer;
