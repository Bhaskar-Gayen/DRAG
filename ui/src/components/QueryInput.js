import React, { useState } from "react";
import axios from "axios";
import { Box, TextField, Button, Typography, Paper } from "@mui/material";

const API_URL = "localhost:8000";
const QueryInput = () => {
  const [query, setQuery] = useState("");
  const [chat, setChat] = useState([]);

  const handleQuery = async () => {
    if (!query) return;

    // Add the user's question to the chat
    setChat((prevChat) => [...prevChat, { sender: "user", message: query }]);

    try {
      const result = await axios.post(`${API_URL}/query`, { query });
      setChat((prevChat) => [
        ...prevChat,
        { sender: "model", message: result.data.response },
      ]);
    } catch (error) {
      console.error("Query error", error);
      setChat((prevChat) => [
        ...prevChat,
        { sender: "model", message: "Error: Unable to fetch response." },
      ]);
    } finally {
      setQuery(""); // Clear input after submission
    }
  };

  return (
    <Box
      display="flex"
      flexDirection="column"
      alignItems="center"
      p={2}
      sx={{
        width: "100%",
        maxWidth: "100%", // Ensures it uses the full screen width
        margin: "auto",
      }}
    >
      <Paper
        elevation={3}
        sx={{
          width: "100%", // Takes full width
          height: "60vh", // 60% of the viewport height, adjusts based on screen size
          maxHeight: "80vh", // Ensure it doesn't grow too large
          overflowY: "auto",
          p: 2,
          mb: 2,
          borderRadius: 2,
        }}
      >
        {chat.map((entry, index) => (
          <Box
            key={index}
            display="flex"
            justifyContent={entry.sender === "user" ? "flex-end" : "flex-start"}
            mb={1}
          >
            <Paper
              elevation={1}
              sx={{
                p: 1.5,
                maxWidth: "75%",
                bgcolor: entry.sender === "user" ? "primary.main" : "grey.300",
                color: entry.sender === "user" ? "white" : "black",
                borderRadius:
                  entry.sender === "user"
                    ? "15px 15px 0 15px"
                    : "15px 15px 15px 0",
              }}
            >
              <Typography variant="body1">{entry.message}</Typography>
            </Paper>
          </Box>
        ))}
      </Paper>

      <Box display="flex" width="100%" alignItems="center">
        <TextField
          fullWidth
          variant="outlined"
          placeholder="Type a message..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          onKeyPress={(e) => e.key === "Enter" && handleQuery()}
          sx={{ mr: 1 }}
        />
        <Button
          variant="contained"
          color="primary"
          onClick={handleQuery}
          disabled={!query}
        >
          Send
        </Button>
      </Box>
    </Box>
  );
};

export default QueryInput;
