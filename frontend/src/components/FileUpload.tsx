// File: src/components/FileUpload.tsx
import React from "react";
import * as XLSX from "xlsx";

type FileUploadProps = {
  onUpload: (file: File, data: any[]) => void;
};

const FileUpload: React.FC<FileUploadProps> = ({ onUpload }) => {
  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = (event) => {
      const data = new Uint8Array(event.target?.result as ArrayBuffer);
      const workbook = XLSX.read(data, { type: "array" });
      const sheetName = workbook.SheetNames[0];
      const sheet = workbook.Sheets[sheetName];
      const json = XLSX.utils.sheet_to_json(sheet);
      onUpload(file, json);
    };
    reader.readAsArrayBuffer(file);
  };

  return (
    <div className="mb-4">
      <input type="file" accept=".xlsx,.xls" onChange={handleFileChange} />
    </div>
  );
};

export default FileUpload;
