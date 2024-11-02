from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Contoh data menu kafe dengan deskripsi
menu_items = [
    {"id": 1, "name": "Espresso", "price": 25, "description": "Kopi hitam pekat tanpa gula."},
    {"id": 2, "name": "Latte", "price": 30, "description": "Kopi dengan campuran susu yang lembut."},
    {"id": 3, "name": "Cappuccino", "price": 32, "description": "Kopi dengan busa susu di atasnya, cocok untuk pecinta kopi ringan."},
    {"id": 4, "name": "Iced Coffee", "price": 28, "description": "Kopi dingin yang segar untuk cuaca panas."},
    {"id": 5, "name": "Green Tea Latte", "price": 35, "description": "Minuman dengan campuran teh hijau dan susu, manis dan menenangkan."}
]

class MenuList(Resource):
    def get(self):
        return jsonify(menu_items)

class MenuItemDetail(Resource):
    def get(self, item_id):
        item = next((m for m in menu_items if m["id"] == item_id), None)
        if item:
            return jsonify(item)
        return {"message": "Menu item not found"}, 404

class AddMenuItem(Resource):
    def post(self):
        data = request.get_json()
        new_item = {
            "id": len(menu_items) + 1,
            "name": data["name"],
            "price": data["price"],
            "description": data.get("description", "No description provided.")
        }
        menu_items.append(new_item)
        return jsonify(new_item)

class UpdateMenuItem(Resource):
    def put(self, item_id):
        item = next((m for m in menu_items if m["id"] == item_id), None)
        if not item:
            return {"message": "Menu item not found"}, 404
        data = request.get_json()
        item.update(data)
        return jsonify(item)

class DeleteMenuItem(Resource):
    def delete(self, item_id):
        global menu_items
        menu_items = [m for m in menu_items if m["id"] != item_id]
        return {"message": "Menu item deleted successfully"}

# Menambahkan resource ke API
api.add_resource(MenuList, '/menu')
api.add_resource(MenuItemDetail, '/menu/<int:item_id>')
api.add_resource(AddMenuItem, '/menu/add')
api.add_resource(UpdateMenuItem, '/menu/update/<int:item_id>')
api.add_resource(DeleteMenuItem, '/menu/delete/<int:item_id>')

if __name__ == '__main__':
    app.run(debug=True)
