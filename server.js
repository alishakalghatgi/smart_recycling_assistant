const express = require("express");
const cors = require("cors");
const app = express();
const PORT = 5000;

// Middleware
app.use(cors());           // Allow frontend to connect
app.use(express.json());   // Parse JSON body

// ✅ POST method for login
app.post("/api/login", (req, res) => {
  const { username, password } = req.body;

  // Example validation (you can replace this with a database later)
  if (username === "admin" && password === "1234") {
    res.json({ success: true, message: "Login successful" });
  } else {
    res.json({ success: false, message: "Invalid credentials" });
  }
});

// Start server
app.listen(5000, () => {
  console.log(`✅ Server running on http://localhost:${PORT}`);
});