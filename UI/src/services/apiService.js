import axios from "axios";

const API_URL = "http://localhost:8000/process_report";  // Ensure correct backend endpoint

const processReport = async (formData) => {
    try {
        const response = await axios.post(API_URL, formData, {
            headers: {
                "Content-Type": "multipart/form-data",  // Ensure correct content type
            },
        });
        return response.data;
    } catch (error) {
        console.error("Error in API call:", error);
        throw error;
    }
};

export default processReport;
