import requests

# 用户名
USERNAME = "isinvon"

# 动态内容 URL
STATS_URL = f"https://github-readme-stats.vercel.app/api?username={USERNAME}&show_icons=true&count_private=true&theme=react&hide_border=true&bg_color=313335&title_color=ffffff&icon_color=F8D866"
LANGUAGES_URL = f"https://denvercoder1-github-readme-stats.vercel.app/api/top-langs/?username={USERNAME}&langs_count=8&layout=compact&theme=react&hide_border=true&bg_color=313335&title_color=ffffff&icon_color=F8D866&hide=Jupyter%20Notebook,Roff"
ACTIVITY_GRAPH_URL = f"https://github-readme-activity-graph.vercel.app/graph/?username={USERNAME}&bg_color=313335&color=ffffff&line=019a61&point=FFFFFF&hide_border=true"

# 生成 README 内容
def generate_readme():
    with open("README.md", "r", encoding="utf-8") as f:
        readme_content = f.read()

    # 更新 Stats 图片
    readme_content = readme_content.replace(
        "https://github-readme-stats.vercel.app/api?username=isinvon&show_icons=true&count_private=true&theme=react&hide_border=true&bg_color=313335&title_color=ffffff&icon_color=F8D866",
        STATS_URL
    )

    # 更新 Languages 图片
    readme_content = readme_content.replace(
        "https://denvercoder1-github-readme-stats.vercel.app/api/top-langs/?username=isinvon&langs_count=8&layout=compact&theme=react&hide_border=true&bg_color=313335&title_color=ffffff&icon_color=F8D866&hide=Jupyter%20Notebook,Roff",
        LANGUAGES_URL
    )

    # 更新 Activity Graph 图片
    readme_content = readme_content.replace(
        "https://github-readme-activity-graph.vercel.app/graph/?username=isinvon&bg_color=313335&color=ffffff&line=019a61&point=FFFFFF&hide_border=true",
        ACTIVITY_GRAPH_URL
    )

    # 写入更新内容
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)


if __name__ == "__main__":
    generate_readme()
