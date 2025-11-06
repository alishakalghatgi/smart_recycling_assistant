const mongoose = require('mongoose');

const wasteSchema = new mongoose.Schema({
  name: { type: String, required: true },
  type: { type: String, enum: ['Recyclable', 'Non-Recyclable'], required: true },
  imageUrl: String,
  createdAt: { type: Date, default: Date.now }
});

// This creates a "wastes" collection in MongoDB
const Waste = mongoose.model('Waste', wasteSchema);

module.exports = Waste;