from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Contoh data menu cafe dengan deskripsi
products = [
    {"id": 1, "name": "Espresso", "price": 25, "description": "Espresso shot dengan aroma dan cita rasa kopi yang kuat."},
    {"id": 2, "name": "Latte", "price": 30, "description": "Kopi espresso dicampur dengan susu hangat, disajikan dengan foam di atasnya."},
    {"id": 3, "name": "Cappuccino", "price": 30, "description": "Kombinasi espresso, susu, dan foam yang seimbang dengan taburan bubuk cokelat."},
    {"id": 4, "name": "Cold Brew", "price": 35, "description": "Kopi diseduh dingin selama 12 jam untuk rasa kopi yang lebih halus."},
    {"id": 5, "name": "Matcha Latte", "price": 28, "description": "Latte hijau dengan bubuk matcha berkualitas tinggi, cocok untuk pecinta teh."}
]

class ProductList(Resource):
    def get(self):
        return jsonify(products)

class ProductDetail(Resource):
    def get(self, product_id):
        product = next((p for p in products if p["id"] == product_id), None)
        if product:
            return jsonify(product)
        return {"message": "Product not found"}, 404

class AddProduct(Resource):
    def post(self):
        data = request.get_json()
        new_product = {
            "id": len(products) + 1,
            "name": data["name"],
            "price": data["price"],
            "description": data.get("description", "No description provided.")
        }
        products.append(new_product)
        return jsonify(new_product)

class UpdateProduct(Resource):
    def put(self, product_id):
        product = next((p for p in products if p["id"] == product_id), None)
        if not product:
            return {"message": "Product not found"}, 404
        data = request.get_json()
        product.update(data)
        return jsonify(product)

class DeleteProduct(Resource):
    def delete(self, product_id):
        global products
        products = [p for p in products if p["id"] != product_id]
        return {"message": "Product deleted successfully"}

# Menambahkan resource ke API
api.add_resource(ProductList, '/products')
api.add_resource(ProductDetail, '/products/<int:product_id>')
api.add_resource(AddProduct, '/products/add')
api.add_resource(UpdateProduct, '/products/update/<int:product_id>')
api.add_resource(DeleteProduct, '/products/delete/<int:product_id>')

if __name__ == '__main__':
    app.run(debug=True)
