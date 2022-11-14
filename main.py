#!/usr/bin/env python3

from jinja2 import Environment, FileSystemLoader
import os
import capellambse

def generate_svg(physical_links):

    environment = Environment(
        loader=FileSystemLoader("template")
    )
    results_template = environment.get_template("svg/ethernet.svg")
    # there is probably a nicer way to do the underscore replacement with jinja
    context = {
        "eth_line1": physical_links[0].pvmt['Cable.Extension_1.Line_1'].replace("_", '\_'),
        "eth_line2": physical_links[0].pvmt['Cable.Extension_1.Line_2'].replace("_", '\_'),
        "eth_line3": physical_links[0].pvmt['Cable.Extension_1.Line_3'].replace("_", '\_'),
        "eth_line4": physical_links[0].pvmt['Cable.Extension_1.Line_4'].replace("_", '\_'),
        "eth_line5": physical_links[0].pvmt['Cable.Extension_1.Line_5'].replace("_", '\_'),
        "eth_line6": physical_links[0].pvmt['Cable.Extension_1.Line_6'].replace("_", '\_'),
        "eth_line7": physical_links[0].pvmt['Cable.Extension_1.Line_7'].replace("_", '\_'),
        "eth_line8": physical_links[0].pvmt['Cable.Extension_1.Line_8'].replace("_", '\_'),
    }

    svg_filename = "tex/svg/ethernet.svg"
    os.makedirs(os.path.dirname(svg_filename), exist_ok=True)
    with open(svg_filename, mode="w", encoding="utf-8") as results:
        results.write(results_template.render(context))
        print(f"SVG created.")

def generate_tex():
    latex_jinja_env = Environment(
        block_start_string = '\BLOCK{',
        block_end_string = '}',
        variable_start_string = '\VAR{',
        variable_end_string = '}',
        comment_start_string = '\#{',
        comment_end_string = '}',
        line_statement_prefix = '%%',
        line_comment_prefix = '%#',
        trim_blocks = True,
        autoescape = False,
        loader=FileSystemLoader("template")
    )
    results_template = latex_jinja_env.get_template("report.tex")
    context = {
        "author": "M. Treber",
        "title": "Some Test Report"
    }

    tex_filename = "tex/report.tex"
    with open(tex_filename, mode="w", encoding="utf-8") as results:
        results.write(results_template.render(context))
        print(f"Tex created.")
        print(f"You can run now `xelatex --shell-escape tex/report.tex`")
        
def main():

    path_to_model = "model/Ethernet/Ethernet.aird"
    model = capellambse.MelodyModel(path_to_model, jupyter_untrusted=True,)
    
    # model.pa.all_physical_links is a list with all physical links.
    # todo: logic to select the right links
    generate_svg(model.pa.all_physical_links)

    generate_tex()

if __name__ == "__main__":
    main()
