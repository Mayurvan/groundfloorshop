import re

# Read the HTML
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Define property-type-specific gradients
gradients = {
    'Retail Shop': 'linear-gradient(135deg, #FF6B6B 0%, #FFA94D 100%)',
    'Office Space': 'linear-gradient(135deg, #4ECDC4 0%, #44A08D 100%)',
    'F&B/Restaurant': 'linear-gradient(135deg, #F7B731 0%, #F368E0 100%)',
    'Showroom': 'linear-gradient(135deg, #9B59B6 0%, #E91E63 100%)'
}

# Replace the propertyTypeImages object with gradients
old_block = """        const propertyTypeImages = {
            'Retail Shop': 'url('/images/retail-shop.svg')',
            'Office Space': 'url('/images/office-space.svg')',
            'F&B/Restaurant': 'url('/images/fb-restaurant.svg')',
            'Showroom': 'url('/images/showroom.svg')'
        };"""

new_block = f"""        const propertyTypeImages = {{
            'Retail Shop': '{gradients["Retail Shop"]}',
            'Office Space': '{gradients["Office Space"]}',
            'F&B/Restaurant': '{gradients["F&B/Restaurant"]}',
            'Showroom': '{gradients["Showroom"]}'
        }};"""

html = html.replace(old_block, new_block)

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ Gradients applied")
