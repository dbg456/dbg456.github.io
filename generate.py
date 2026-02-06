import random

def generate_super_bowl_page():
    # 1. Setup Players (11 players)
    players = ["Dave G", "Mom", "Steve W", "Linda K", "John D", 
               "Sarah P", "Mike R", "Kelly B", "Tom H", "Anna S", "Chris L"]
    
    # 2. Assign Squares (9 each + 1 lucky winner)
    pool = []
    base_count = 100 // len(players) # 9
    extra_square_winner = random.choice(players)
    
    for p in players:
        count = base_count + (1 if p == extra_square_winner else 0)
        # Create symbol (Initials) - e.g. "Dave G" -> "DG"
        symbol = "".join([name[0] for name in p.split()]).upper()[:2]
        pool.extend([(p, symbol)] * count)
    
    random.shuffle(pool)
    
    # 3. Randomize Axis Numbers
    rows_patriots = list(range(10))
    cols_seahawks = list(range(10))
    random.shuffle(rows_patriots)
    random.shuffle(cols_seahawks)

    # 4. CSS for Teams and Layout
    css = """
    <style>
        :root { --patriots-red: #C60C30; --seahawks-navy: #002244; }
        .wrapper { max-width: 800px; margin: auto; font-family: sans-serif; }
        table { border-collapse: collapse; table-layout: fixed; width: 100%; margin-bottom: 20px; }
        th, td { border: 1px solid #333; text-align: center; padding: 5px; overflow: hidden; }
        
        /* Team Headers */
        .seahawks-header { background-color: var(--seahawks-navy); color: white; font-weight: bold; }
        .patriots-header { background-color: var(--patriots-red); color: white; font-weight: bold; width: 30px; }
        
        /* Axis Numbers */
        .axis-row { background-color: #eee; font-weight: bold; width: 35px; }
        .axis-col { background-color: #eee; font-weight: bold; height: 35px; }
        
        /* Grid Cells */
        .grid-cell { font-size: 0.85rem; height: 40px; }
        .legend-table { width: auto; min-width: 300px; margin-top: 20px; }
        .legend-table td { text-align: left; padding: 8px; }
        .lucky { color: #d4af37; font-weight: bold; font-size: 0.8em; }
    </style>
    """

    # 5. Build the Table
    html_table = f"""
    <div class="wrapper">
        <h1>Super Bowl Squares</h1>
        <p>Payouts: Q1: $40 | Half: $120 | Q3: $40 | Final: $240</p>
        <p class="lucky">Note: {extra_square_winner} won the random 'Lucky 100th' square!</p>
        
        <table>
            <tr>
                <th colspan="2" style="border:none"></th>
                <th colspan="10" class="seahawks-header">SEAHAWKS (Columns)</th>
            </tr>
            <tr>
                <th colspan="2" style="border:none"></th>
    """
    for c in cols_seahawks:
        html_table += f"<th class='axis-col'>{c}</th>"
    html_table.strip()
    html_table += "</tr>"

    # Rows with Side Header
    for i, r_num in enumerate(rows_patriots):
        html_table += "<tr>"
        if i == 0:
            html_table += f'<th rowspan="10" class="patriots-header">P<br>A<br>T<br>R<br>I<br>O<br>T<br>S</th>'
        
        html_table += f"<td class='axis-row'>{r_num}</td>"
        
        for j in range(10):
            name, symbol = pool[(i * 10) + j]
            html_table += f"<td class='grid-cell'>{symbol}</td>"
        html_table += "</tr>"
    
    html_table += "</table>"

    # 6. Build Legend Table
    html_table += "<h3>Player Legend</h3><table class='legend-table'><tr><th>Symbol</th><th>Player</th></tr>"
    unique_players = sorted(list(set(pool)))
    for name, symbol in unique_players:
        html_table += f"<tr><td><strong>{symbol}</strong></td><td>{name}</td></tr>"
    html_table += "</table></div>"

    # Final File Output
    with open("index.html", "w") as f:
        f.write(f"<html><head>{css}</head><body>{html_table}</body></html>")

generate_super_bowl_page()
print("Website generated with team colors and symbol mapping!")