import random

def generate_super_bowl_page():
    # --- AUDITABLE SEED ---
    # Changing this number will change the entire board. 
    # Use any integer here.
    RANDOM_SEED = 42 
    random.seed(RANDOM_SEED)
    
    # 1. Setup Players
    players = ["Dave G", "Mom", "Steve W", "Linda K", "John D", 
               "Sarah P", "Mike R", "Kelly B", "Tom H", "Anna S", "Chris L"]
    
    # 2. Assign Squares
    pool = []
    base_count = 100 // len(players) # 9
    
    # We pick the lucky winner using the seed so it's reproducible
    extra_square_winner = random.choice(players)
    
    for p in players:
        count = base_count + (1 if p == extra_square_winner else 0)
        symbol = "".join([name[0] for name in p.split()]).upper()[:2]
        pool.extend([(p, symbol)] * count)
    
    # Shuffle names and axes using the seed
    random.shuffle(pool)
    rows_patriots = list(range(10))
    cols_seahawks = list(range(10))
    random.shuffle(rows_patriots)
    random.shuffle(cols_seahawks)

    # 3. CSS Styling
    css = """
    <style>
        :root { --patriots-red: #C60C30; --seahawks-navy: #002244; }
        .wrapper { max-width: 800px; margin: auto; font-family: -apple-system, sans-serif; line-height: 1.5; }
        table { border-collapse: collapse; table-layout: fixed; width: 100%; margin-bottom: 20px; }
        th, td { border: 1px solid #333; text-align: center; padding: 4px; overflow: hidden; }
        .seahawks-header { background-color: var(--seahawks-navy); color: white; font-weight: bold; font-size: 0.9em; }
        .patriots-header { background-color: var(--patriots-red); color: white; font-weight: bold; width: 25px; font-size: 0.8em; line-height: 1.2; }
        .axis-num { background-color: #eee; font-weight: bold; }
        .grid-cell { font-size: 0.8rem; height: 35px; background: white; }
        .legend-table { width: auto; min-width: 300px; margin-top: 20px; }
        footer { margin-top: 50px; padding: 20px; border-top: 1px solid #eee; font-size: 0.85em; color: #666; }
        a { color: #0066cc; }
    </style>
    """

    # 4. Build HTML
    repo_url = "https://github.com/dbg456.github.io" 
    
    html = f"""
    <div class="wrapper">
        <h1>🏈 Superb Owl Squares 2026 </h1>
        <p><strong>Payouts:</strong> Q1: $40 | Half: $120 | Q3: $40 | Final: $240</p>
        <p class="lucky">Note: {extra_square_winner} won the random 'Lucky 100th' square!</p>
        
        <table>
            <tr>
                <th colspan="2" style="border:none"></th>
                <th colspan="10" class="seahawks-header">SEAHAWKS</th>
            </tr>
            <tr>
                <th colspan="2" style="border:none"></th>
    """
    for c in cols_seahawks:
        html += f"<th class='axis-num'>{c}</th>"
    html += "</tr>"

    for i, r_num in enumerate(rows_patriots):
        html += "<tr>"
        if i == 0:
            html += f'<th rowspan="10" class="patriots-header">P<br>A<br>T<br>R<br>I<br>O<br>T<br>S</th>'
        html += f"<td class='axis-num' style='width:30px'>{r_num}</td>"
        for j in range(10):
            name, symbol = pool[(i * 10) + j]
            html += f"<td class='grid-cell'>{symbol}</td>"
        html += "</tr>"
    html += "</table>"

    # Legend
    html += "<h3>Player Legend</h3><table class='legend-table'><tr><th>ID</th><th>Player</th></tr>"
    unique_mapping = sorted(list(set(pool)), key=lambda x: x[1])
    for name, symbol in unique_mapping:
        html += f"<tr><td><strong>{symbol}</strong></td><td>{name}</td></tr>"
    html += "</table>"

    # Footer
    html += f"""
        <footer>
            <p>Built with ❤️ by Dave & Gemini.</p>
            <p>View the <a href="{repo_url}">source code on GitHub</a> to verify the randomization logic.</p>
        </footer>
    </div>
    """

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(f"<!DOCTYPE html><html><head><title>Super Bowl Squares</title>{css}</head><body>{html}</body></html>")

if __name__ == "__main__":
    generate_super_bowl_page()