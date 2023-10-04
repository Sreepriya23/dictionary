from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

simple_detail = [
    {
        "id": 1,
        "name": "Akshaya",
        "image": "fdghj.jpg",
    },
    {
        "id": 2,
        "name": "John Doe",
        "image": "john.jpg",
    },
    {
        "id": 3,
        "name": "Jane Smith",
        "image": "jane.jpg",
    },
]

advanced_detail = [
    {
        'id': 1,
        'f_name': 'akshaya',
        'l_name': 'p',
        'contact': '123-456-7890',
        'email': 'akshaya@example.com',
        'image': 'fgh.jpg',
    },
    {
        'id': 2,
        'f_name': 'John',
        'l_name': 'Doe',
        'contact': '123-456-7890',
        'email': 'john.doe@example.com',
        'image': 'john.jpg',
    },
    {
        'id': 3,
        'f_name': 'Jane',
        'l_name': 'Smith',
        'contact': '987-654-3210',
        'email': 'jane.smith@example.com',
        'image': 'jane.jpg',
    },
]

def get_detail_by_id(request, id=None):
    if id:
        details = [detail for detail in advanced_detail if detail['id'] == id]
        if details:
            return JsonResponse(details[0])
        else:
            return JsonResponse({'error': 'ID not found'}, status=404)
    else:
        return JsonResponse(simple_detail, safe=False)