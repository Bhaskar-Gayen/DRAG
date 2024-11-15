import React, { useState } from "react";
import {
  AppBar,
  Toolbar,
  IconButton,
  Typography,
  Box,
  Menu,
  MenuItem,
} from "@mui/material";
import FolderIcon from "@mui/icons-material/Folder";
import UploadFileIcon from "@mui/icons-material/UploadFile";
import ChatIcon from "@mui/icons-material/Chat";
import AccountCircleIcon from "@mui/icons-material/AccountCircle";

const Navbar = () => {
  const [userMenuAnchor, setUserMenuAnchor] = useState(null); // For user-specific menu (e.g., Logout, UserID)
  const [userInfo] = useState({ userID: "User123" });

  const handleUserMenuClick = (event) => {
    setUserMenuAnchor(event.currentTarget); // Open the menu
  };

  const handleUserMenuClose = () => {
    setUserMenuAnchor(null); // Close the menu
  };

  return (
    <AppBar position="sticky">
      <Toolbar sx={{ display: "flex", justifyContent: "space-between" }}>
        {/* Title on the left */}
        <Typography variant="h6" sx={{ flexShrink: 0 }}>
          Data Chat
        </Typography>

        {/*Menu and User icon on the right */}
        <Box sx={{ display: "flex", alignItems: "center" }}>
          <IconButton color="inherit" sx={{ mr: 2 }}>
            <FolderIcon />
          </IconButton>
          <IconButton color="inherit" sx={{ mr: 2 }}>
            <UploadFileIcon />
          </IconButton>
          <IconButton color="inherit" sx={{ mr: 2 }}>
            <ChatIcon />
          </IconButton>
          <IconButton
            color="inherit"
            onClick={handleUserMenuClick} // Open user menu when clicked
          >
            <AccountCircleIcon />
          </IconButton>

          {/* User menu dropdown */}
          <Menu
            anchorEl={userMenuAnchor}
            open={Boolean(userMenuAnchor)} // Show menu if it's open
            onClose={handleUserMenuClose} // Close menu on click outside
          >
            <MenuItem onClick={handleUserMenuClose}>Logout</MenuItem>
            <MenuItem onClick={handleUserMenuClose}>
              UserID: {userInfo.userID}
            </MenuItem>
          </Menu>
        </Box>
      </Toolbar>
    </AppBar>
  );
};

export default Navbar;
