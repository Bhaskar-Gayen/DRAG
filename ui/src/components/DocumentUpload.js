// src/components/DocumentUpload.js
import React, { useState } from "react";
import {
  Box,
  Button,
  Typography,
  LinearProgress,
  IconButton,
  Paper,
} from "@mui/material";
import { CloudUpload, InsertDriveFile } from "@mui/icons-material";

const DocumentUpload = () => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [uploadProgress, setUploadProgress] = useState(0);
  const [isUploading, setIsUploading] = useState(false);

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const handleUpload = async () => {
    if (!selectedFile) {
      alert("Please select a file first.");
      return;
    }

    setIsUploading(true);
    setUploadProgress(0);

    // Simulate file upload process
    const simulatedUpload = setInterval(() => {
      setUploadProgress((oldProgress) => {
        if (oldProgress === 100) {
          clearInterval(simulatedUpload);
          setIsUploading(false);
          setSelectedFile(null);
          return 0;
        }
        return Math.min(oldProgress + 10, 100);
      });
    }, 300);
  };

  return (
    <Box
      display="flex"
      flexDirection="column"
      alignItems="center"
      p={3}
      component={Paper}
      elevation={3}
      sx={{ maxWidth: 400, margin: "auto" }}
    >
      <Typography variant="h6" gutterBottom>
        Upload Document
      </Typography>

      <Box
        display="flex"
        flexDirection="column"
        alignItems="center"
        width="100%"
      >
        <input
          type="file"
          accept=".pdf,.ppt,.pptx,.csv"
          style={{ display: "none" }}
          id="file-input"
          onChange={handleFileChange}
        />
        <label htmlFor="file-input">
          <IconButton color="primary" component="span" sx={{ p: 2 }}>
            <CloudUpload fontSize="large" />
          </IconButton>
        </label>

        {selectedFile && (
          <Box display="flex" alignItems="center" mt={2} mb={1}>
            <InsertDriveFile color="action" sx={{ mr: 1 }} />
            <Typography variant="body2">{selectedFile.name}</Typography>
          </Box>
        )}

        <Button
          variant="contained"
          color="primary"
          onClick={handleUpload}
          disabled={isUploading || !selectedFile}
          sx={{ mt: 2 }}
          fullWidth
        >
          Upload
        </Button>

        {isUploading && (
          <Box width="100%" mt={2}>
            <LinearProgress variant="determinate" value={uploadProgress} />
            <Typography variant="body2" color="textSecondary" align="center">
              Uploading... {uploadProgress}%
            </Typography>
          </Box>
        )}
      </Box>
    </Box>
  );
};

export default DocumentUpload;
