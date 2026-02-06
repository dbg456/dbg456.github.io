import random

def generate_squares_html(participants):
    # 1. Create the list of 100 names based on their 'buy-in'
    pool = []
    for name, count in participants.items():
        pool.extend([name] * count)
    
    # Fill remaining squares with 'Available' if not at 100
    while len(pool) < 100:
        pool.append("Available")
    
    # 2. Randomize the assignment of names to the 0-99 index
    random.shuffle(pool)
    
    # 3. Randomize the Row (NFC) and Column (AFC) numbers
    row_headers = list(range(10))
    col_headers = list(range(10))
    random.shuffle(row_headers)
    random.shuffle(col_headers)
    
    # 4. Build the HTML Table
    html = """
    <style>
        .sb-table { border-collapse: collapse; width: 100%; table-layout: fixed; }
        .sb-table th, .sb-table td { border: 1px solid #444; padding: 10px; text-align: center; font-size: 0.8em; }
        .axis { background-color: #333; color: white; font-weight: bold; width: 40px; }
        .corner { background: transparent; border: none !important; }
    </style>
    <div style="overflow-x: auto;">
    <table class="sb-table">
        <thead>
            <tr>
                <th class="corner"></th>"""
    
    # Add Column Headers
    for col in col_headers:
        html += f"<th class='axis'>{col}</th>"
    html += "</tr></thead><tbody>"
    
    # Add Rows
    for i, row_num in enumerate(row_headers):
        html += f"<tr><td class='axis'>{row_num}</td>"
        for j in range(10):
            # Mapping 2D grid back to our 1D shuffled pool
            square_index = (i * 10) + j
            name = pool[square_index]
            html += f"<td>{name}</td>"
        html += "</tr>"
        
    html += "</tbody></table></div>"
    return html

# --- CONFIGURATION ---
family_picks = {
    "Dave": 15,
    "Mom": 10,
    "Uncle Steve": 5,
    "Aunt Linda": 20,
    # Add more here until you hit 100!
}

# Run the generator
my_table_html = generate_squares_html(family_picks)

# Save it to a file
with open("index.html", "w") as f:
    # Adding some basic page structure around the table
    f.write(f"<html><head><link rel='stylesheet' href='https://cdn.jsdelivr.net/npm/water.css@2/out/water.css'></head><body>")
    f.write("<h1>Super Bowl LIX Squares</h1>")
    f.write(my_table_html)
    f.write("</body></html>")

print("index.html has been generated!")