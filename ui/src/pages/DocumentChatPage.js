import { React, useState } from "react";
import { Box, Stack } from "@mui/material";
import DocumentUpload from "../components/DocumentUpload"; // Adjust the import based on your project structure
import QueryInput from "../components/QueryInput"; // Adjust the import based on your project structure
import NavBar from "../components/NavBar";

const DocumentChatPage = () => {
  // const [docCount, setDocCount] = useState(0);
  return (
    <Box sx={{ flexGrow: 1, p: 3 }}>
      <NavBar />

      <Stack direction={{ xs: "column", md: "row" }} spacing={3} sx={{ mt: 3 }}>
        {/* Left Section: Document Upload (30% width) */}
        <Box sx={{ flex: 0.2, p: 2, minHeight: 300 }}>
          <DocumentUpload />
        </Box>

        {/* Right Section: Chat Assistant (70% width) */}
        <Box sx={{ flex: 0.8, p: 2, minHeight: 300 }}>
          <QueryInput />
        </Box>
      </Stack>
    </Box>
  );
};

export default DocumentChatPage;
