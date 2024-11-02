from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Example data of batik products
batik = [
    {
        "id": 1,
        "name": "Batik Tulis Pekalongan",
        "description": "Batik tulis asli dari Pekalongan dengan motif khas pesisir.",
        "price": 300,  # in thousands
        "address": "Jl. Raya Pekalongan No.10, Pekalongan"
    },
    {
        "id": 2,
        "name": "Batik Cap Solo",
        "description": "Batik cap tradisional dari Solo dengan motif klasik.",
        "price": 200,  # in thousands
        "address": "Jl. Slamet Riyadi No.15, Solo"
    },
    {
        "id": 3,
        "name": "Batik Sutra Bali",
        "description": "Batik berbahan sutra dengan motif eksotis dari Bali.",
        "price": 500,  # in thousands
        "address": "Jl. Diponegoro No.25, Denpasar, Bali"
    },
    {
        "id": 4,
        "name": "Batik Modern Yogyakarta",
        "description": "Batik modern dengan sentuhan desain kontemporer dari Yogyakarta.",
        "price": 350,  # in thousands
        "address": "Jl. Malioboro No.50, Yogyakarta"
    },
    {
        "id": 5,
        "name": "Kain Batik Cirebon",
        "description": "Kain batik khas Cirebon dengan motif megamendung yang ikonik.",
        "price": 400,  # in thousands
        "address": "Jl. Siliwangi No.5, Cirebon"
    },
    {
        "id": 6,
        "name": "Batik Lasem",
        "description": "Batik dengan motif unik dan kombinasi warna khas Lasem.",
        "price": 450,  # in thousands
        "address": "Jl. Lasem Indah No.8, Lasem"
    },
    {
        "id": 7,
        "name": "Batik Betawi",
        "description": "Batik dengan motif khas budaya Betawi yang berwarna cerah.",
        "price": 280,  # in thousands
        "address": "Jl. Salemba Raya No.12, Jakarta"
    },
    {
        "id": 8,
        "name": "Batik Kawung",
        "description": "Batik klasik dengan pola kawung yang berulang, khas Jawa Tengah.",
        "price": 320,  # in thousands
        "address": "Jl. Diponegoro No.45, Semarang"
    },
    {
        "id": 9,
        "name": "Batik Priangan",
        "description": "Batik dengan motif flora dan fauna yang terinspirasi dari alam Priangan.",
        "price": 370,  # in thousands
        "address": "Jl. Merdeka No.30, Bandung"
    },
    {
        "id": 10,
        "name": "Batik Parang",
        "description": "Batik tradisional dengan motif parang yang memiliki makna filosofis.",
        "price": 430,  # in thousands
        "address": "Jl. Parang Kusumo No.7, Surakarta"
    }
]

class BatikProductList(Resource):
    def get(self):
        return jsonify(batik)

class BatikProductDetail(Resource):
    def get(self, product_id):
        product = next((p for p in batik if p["id"] == product_id), None)
        if product:
            return jsonify(product)
        return {"message": "Product not found"}, 404

class AddBatikProduct(Resource):
    def post(self):
        data = request.get_json()
        new_product = {
            "id": len(batik) + 1,
            "name": data["name"],
            "description": data.get("description", "No description provided"),
            "price": data["price"],
            "address": data.get("address", "No address provided")
        }
        batik.append(new_product)
        return jsonify(new_product)

class UpdateBatikProduct(Resource):
    def put(self, product_id):
        product = next((p for p in batik if p["id"] == product_id), None)
        if not product:
            return {"message": "Product not found"}, 404
        data = request.get_json()
        product.update(data)
        return jsonify(product)

class DeleteBatikProduct(Resource):
    def delete(self, product_id):
        global batik
        batik = [p for p in batik if p["id"] != product_id]
        return {"message": "Product deleted successfully"}

# Adding resources to the API
api.add_resource(BatikProductList, '/batik-products')
api.add_resource(BatikProductDetail, '/batik-products/<int:product_id>')
api.add_resource(AddBatikProduct, '/batik-products/add')
api.add_resource(UpdateBatikProduct, '/batik-products/update/<int:product_id>')
api.add_resource(DeleteBatikProduct, '/batik-products/delete/<int:product_id>')

if __name__ == '__main__':
    app.run(debug=True)
