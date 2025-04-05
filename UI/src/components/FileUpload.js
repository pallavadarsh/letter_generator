import React from "react";
import { Button } from "@mui/material";
import CloudUploadIcon from "@mui/icons-material/CloudUpload";

const FileUpload = ({ setFile }) => {
    return (
        <>
            <input type="file" accept="image/*,application/pdf" onChange={(e) => setFile(e.target.files[0])} style={{ display: "none" }} id="file-upload" />
            <label htmlFor="file-upload">
                <Button variant="contained" component="span" startIcon={<CloudUploadIcon />}>
                    Choose File
                </Button>
            </label>
        </>
    );
};

export default FileUpload;
