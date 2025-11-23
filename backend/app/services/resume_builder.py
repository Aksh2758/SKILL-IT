from jinja2 import Template

def render_resume_template(data):
    template = """
    <html>
    <body style="font-family: Arial; padding: 20px;">
        <h1>{{ name }}</h1>
        <p><b>Email:</b> {{ email }}</p>
        <p><b>Phone:</b> {{ phone }}</p>

        <h2>Summary</h2>
        <p>{{ summary }}</p>

        <h2>Skills</h2>
        <ul>
        {% for s in skills %}
            <li>{{ s }}</li>
        {% endfor %}
        </ul>

        <h2>Projects</h2>
        {% for p in projects %}
            <h3>{{ p.title }}</h3>
            <p>{{ p.description }}</p>
            <p><b>Tech:</b> {{ ", ".join(p.tech) }}</p>
            <hr/>
        {% endfor %}
    </body>
    </html>
    """

    return Template(template).render(data)
