import { Router } from "express";
import Product, { IProduct } from "../models/Product";

const router = Router();

// Obtener todos los productos
router.get("/", async (req, res) => {
  const products = await Product.find();
  res.json(products);
});

// Crear un nuevo producto
router.post("/", async (req, res) => {
  const product = new Product(req.body as IProduct);
  await product.save();
  res.status(201).json(product);
});

router.get("/:id", async (req, res) => {
  const { id } = req.params;

  try {
    const product = await Product.findById(id);
    if (!product) {
      return void res.status(404).json({ message: "Producto no encontrado" });
    }
    res.json(product);
  } catch (error) {
    res.status(500).json({ message: "Error al obtener el producto" });
  }
});

export default router;
