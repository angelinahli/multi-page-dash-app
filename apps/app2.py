from app import app, base_template

layout = base_template.render_template(
    title_text="Page 2",
    subtitle_text="Page 2 Subtitle"
)