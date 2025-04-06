import React, { useState } from "react";
import { Container, Typography, Button, Tabs, Tab, Paper } from "@mui/material";

const ReportDetails = ({ result }) => {
    const [tabIndex, setTabIndex] = useState(0);
    const [letterIndex, setLetterIndex] = useState(0);

    if (!result) return null;

    const { details, letter, summary } = result;
    const totalLetters = letter?.length || 0;

    const handleNext = () => {
        setLetterIndex((prev) => (prev + 1) % totalLetters);
    };

    const handlePrev = () => {
        setLetterIndex((prev) => (prev - 1 + totalLetters) % totalLetters);
    };

    // Convert summary text into bullet points
    const bulletPoints = summary
        .split(". ") // Split into sentences
        .filter(sentence => sentence.trim() !== "") // Remove empty strings
        .map((sentence, index) => <li key={index}>{sentence.trim()}.</li>); // Convert to <li>

    return (
        <Container>
            <Tabs value={tabIndex} onChange={(e, newIndex) => setTabIndex(newIndex)} centered>
                <Tab label="Letters" />
                <Tab label="Summary" />
            </Tabs>

            {/* Letter Section */}
            {tabIndex === 0 && totalLetters > 0 && (
                <Paper elevation={3} style={{ padding: "20px", marginTop: "20px", textAlign: "left" }}>
                    <Typography variant="h6">Letter for {details[letterIndex]?.Name}</Typography>
                    <Typography variant="body1" style={{ whiteSpace: "pre-line", marginTop: "10px" }}>
                        {letter[letterIndex]}
                    </Typography>

                    <div style={{ display: "flex", justifyContent: "space-between", marginTop: "20px" }}>
                        <Button onClick={handlePrev} disabled={letterIndex === 0}>Previous</Button>
                        <Typography>{letterIndex + 1} / {totalLetters}</Typography>
                        <Button onClick={handleNext} disabled={letterIndex === totalLetters - 1}>Next</Button>
                    </div>
                </Paper>
            )}

            {/* Summary Section */}
{tabIndex === 1 && (
    <Paper elevation={3} style={{ padding: "20px", marginTop: "20px", textAlign: "left" }}>
        <Typography variant="h6">Summary</Typography>
        <div style={{ marginTop: "10px" }}>
            {summary.split('\n').map((line, index) => {
                if (line.startsWith('**')) {
                    return (
                        <Typography key={index} variant="subtitle1" style={{ fontWeight: 'bold', marginTop: '16px' }}>
                            {line.replace(/\*\*/g, '')}
                        </Typography>
                    );
                } else if (line.startsWith('* ')) {
                    return (
                        <ul key={index} style={{ margin: 0, paddingLeft: "20px" }}>
                            <li>{line.slice(2)}</li>
                        </ul>
                    );
                } else if (line.startsWith('+ ')) {
                    return (
                        <ul key={index} style={{ margin: 0, paddingLeft: "40px" }}>
                            <li>{line.slice(2)}</li>
                        </ul>
                    );
                } else if (line.trim() === '') {
                    return <br key={index} />;
                } else {
                    return (
                        <Typography key={index} variant="body2">
                            {line}
                        </Typography>
                    );
                }
            })}
        </div>
    </Paper>
)}

        </Container>
    );
};

export default ReportDetails;
