import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import { CssBaseline, Container } from "@mui/material";
import PoliceReportUploader from "./pages/PoliceReportUploader";

const App = () => {
    return (
        <Router>
            <CssBaseline />
            <Container>
                <Routes>
                    <Route path="/" element={<PoliceReportUploader />} />
                </Routes>
            </Container>
        </Router>
    );
};

export default App;
