import express from "express";
import mongoose from "mongoose";
import cors from "cors";
import dotenv from "dotenv";
import productRoutes from "./routes/productRoutes";

dotenv.config();

const app = express();
const port = process.env.PORT || 3000;

app.use(cors());
app.use(express.json());

app.use("/products", productRoutes);

// Conexión a MongoDB
mongoose
  .connect(process.env.MONGODB_URI as string)
  .then(() => {
    console.log("MongoDB connected!");
    app.listen(port, () =>
      console.log(`Product Service running on port ${port}`)
    );
  })
  .catch((err) => {
    console.error("MongoDB connection error:", err);
  });
