import React, { useState } from "react";
import FileUpload from "../components/FileUpload";
import TraceViewer from "../components/TraceViewer";
import SummaryCard from "../components/SummaryCard";
import LetterViewer from "../components/LetterViewer";
const baseURL = import.meta.env.VITE_API_URL;

const UploadPage = () => {
  const [traceId, setTraceId] = useState<string | null>(null);
  const [traceUrl, setTraceUrl] = useState<string | null>(null);
  const [summary, setSummary] = useState<string | null>(null);
  const [tableData, setTableData] = useState<any[] | null>(null);
  const [uploadedFile, setUploadedFile] = useState<File | null>(null);
  const [letters, setLetters] = useState<string[] | null>(null);
  const [currentLetterIndex, setCurrentLetterIndex] = useState(0);
  const [activeSection, setActiveSection] = useState<"letters" | "summary" | "trace">("letters");

  const handleUpload = async (file: File, data: any[]) => {
    setTableData(data);
    setUploadedFile(file);
    setTraceId(null);
    setTraceUrl(null);
    setSummary(null);
    setLetters(null);
    setCurrentLetterIndex(0);
    setActiveSection("letters");
  };

  const generateLetter = async () => {
    if (!uploadedFile) return;

    const formData = new FormData();
    formData.append("file", uploadedFile);

    const response = await fetch(`${baseURL}/generate`, {
      method: "POST",
      body: formData,
    });

    const result = await response.json();

    setTraceId(result.trace_id);
    setTraceUrl(`${baseURL}/trace/${result.trace_id}`);
    setSummary(result.summary);
    setLetters(result.letters);
    setCurrentLetterIndex(0);
    setActiveSection("letters");
  };

  const handleNext = () => {
    if (letters && currentLetterIndex < letters.length - 1) {
      setCurrentLetterIndex(currentLetterIndex + 1);
    }
  };

  const handlePrev = () => {
    if (letters && currentLetterIndex > 0) {
      setCurrentLetterIndex(currentLetterIndex - 1);
    }
  };

  return (
    <div className="p-4">
      <h2 className="text-2xl font-bold mb-4">Upload Accident Report</h2>
      <FileUpload onUpload={handleUpload} />

      {tableData && (
        <div className="bg-white p-4 rounded shadow mt-4 overflow-auto">
          <h3 className="text-lg font-semibold mb-2">Excel Content</h3>
          <table className="min-w-full text-sm text-left text-gray-700">
            <thead>
              <tr>
                {Object.keys(tableData[0]).map((key) => (
                  <th key={key} className="px-4 py-2 border-b bg-gray-200">{key}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {tableData.map((row, idx) => (
                <tr key={idx}>
                  {Object.values(row).map((val, i) => (
                    <td key={i} className="px-4 py-2 border-b">{val as string}</td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {uploadedFile && (
        <div className="flex items-center gap-4 mt-4">
          <button
            onClick={generateLetter}
            className="px-4 py-2 bg-blue-600 text-white rounded shadow hover:bg-blue-700"
          >
            Generate Letter
          </button>
        </div>
      )}

      {traceId && (
        <div className="flex items-center gap-4 mt-4">
          <button
            onClick={() => setActiveSection("letters")}
            className={`px-4 py-2 rounded shadow ${
              activeSection === "letters"
                ? "bg-blue-700 text-white"
                : "bg-blue-100 text-blue-700 hover:bg-blue-200"
            }`}
          >
            Letters
          </button>
          <button
            onClick={() => setActiveSection("summary")}
            className={`px-4 py-2 rounded shadow ${
              activeSection === "summary"
                ? "bg-green-700 text-white"
                : "bg-green-100 text-green-700 hover:bg-green-200"
            }`}
          >
            Summary
          </button>
          <button
            onClick={() => setActiveSection("trace")}
            className={`px-4 py-2 rounded shadow ${
              activeSection === "trace"
                ? "bg-gray-700 text-white"
                : "bg-gray-100 text-gray-700 hover:bg-gray-200"
            }`}
          >
            View Trace
          </button>
        </div>
      )}

      {traceUrl && activeSection === "trace" && <TraceViewer traceUrl={traceUrl} />}
      {summary && activeSection === "summary" && <SummaryCard summary={summary} />}
      {letters && letters.length > 0 && activeSection === "letters" && (
        <LetterViewer
          letters={letters}
          currentIndex={currentLetterIndex}
          handleNext={handleNext}
          handlePrev={handlePrev}
        />
      )}
    </div>
  );
};

export default UploadPage;
