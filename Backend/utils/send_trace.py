from routers.trace_router import upload_trace, TraceUploadPayload, TraceEvent

async def send_trace(records, trace_id, all_letters, summaries):
    events = []

    for i, (record, letter, summary) in enumerate(zip(records, all_letters, summaries)):
        events.append(TraceEvent(
            step=(i * 2) + 1,
            action=f"Generated Letter for {record.get('name', 'Unknown')}",
            type="LLM Generation",
            input=str(record),
            output=letter
        ))
        events.append(TraceEvent(
            step=(i * 2) + 2,
            action=f"Summarized for {record.get('name', 'Unknown')}",
            type="Summary",
            input=str(record),
            output=summary
        ))

    payload = TraceUploadPayload(trace_id=trace_id, events=events)
    await upload_trace(payload)
