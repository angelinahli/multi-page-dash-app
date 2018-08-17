from app import app, base_template

layout = base_template.render_template(
    title_text="Page 1",
    subtitle_text="Page 1 Subtitle"
)