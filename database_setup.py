import sqlite3

# Create database and table
conn = sqlite3.connect('audio_agent.db')
c = conn.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS responses (
    intent TEXT PRIMARY KEY,
    response TEXT
)
''')

# Insert sample data
sample_data = [
    ('reduce_noise', 'To reduce noise, check grounding and use decoupling capacitors.'),
    ('design_filter', 'Design a low-pass filter using f = 1/(2πRC).'),
    ('reduce_distortion', 'Use high slew rate op-amps and avoid signal overload to reduce distortion.')
]

c.executemany('INSERT OR REPLACE INTO responses VALUES (?, ?)', sample_data)
conn.commit()
conn.close()