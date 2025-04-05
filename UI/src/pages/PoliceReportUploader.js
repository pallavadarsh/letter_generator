import React, { useState } from "react";
import { Container, Typography, Button, CircularProgress } from "@mui/material";
import { DataGrid } from "@mui/x-data-grid";
import FileUpload from "../components/FileUpload";
import ReportDetails from "../components/ReportDetails";
import processReport from "../services/apiService";
import Papa from "papaparse";

const PoliceReportUploader = () => {
    const [file, setFile] = useState(null);
    const [loading, setLoading] = useState(false);
    const [result, setResult] = useState(null);
    const [fileData, setFileData] = useState([]);
    const [columns, setColumns] = useState([]);

    const handleFileUpload = (selectedFile) => {
        setFile(selectedFile);
        const reader = new FileReader();
        reader.onload = ({ target }) => {
            Papa.parse(target.result, {
                complete: (result) => {
                    const [headers, ...rows] = result.data;
                    const formattedColumns = headers.map((header) => ({
                        field: header,
                        headerName: header,
                        width: 150,
                    }));
                    const formattedRows = rows.map((row, index) => {
                        let obj = { id: index };
                        headers.forEach((header, i) => {
                            obj[header] = row[i] || "";
                        });
                        return obj;
                    });
                    setColumns(formattedColumns);
                    setFileData(formattedRows);
                },
                header: false,
            });
        };
        reader.readAsText(selectedFile);
    };

    const handleGenerate = async () => {
        if (!file) return;
        setLoading(true);
        try {
            const formData = new FormData();
            formData.append("file", file);  // Ensure correct key "file"
    
            const response = await processReport(formData);
            setResult(response);
        } catch (error) {
            console.error("Error generating report:", error);
        }
        setLoading(false);
    };
    

    return (
        <Container maxWidth="md" style={{ textAlign: "center", marginTop: "50px" }}>
            <Typography variant="h4" gutterBottom>Police Report Processor</Typography>
            <FileUpload setFile={handleFileUpload} />
            {file && <Typography variant="body1">Selected File: {file.name}</Typography>}
            {fileData.length > 0 && (
                <div style={{ height: 400, width: "100%", marginTop: "20px" }}>
                    <DataGrid rows={fileData} columns={columns} pageSize={5} />
                </div>
            )}
            {fileData.length > 0 && (
                <Button
                    variant="contained"
                    color="primary"
                    onClick={handleGenerate}
                    disabled={loading}
                    style={{ marginTop: "20px" }}
                >
                    {loading ? <CircularProgress size={24} /> : "Generate Letters"}
                </Button>
            )}
            <ReportDetails result={result} />
        </Container>
    );
};

export default PoliceReportUploader;
