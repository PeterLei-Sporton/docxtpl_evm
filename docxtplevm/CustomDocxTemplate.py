import re
from docxtpl import DocxTemplate


class CustomDocxTemplate(DocxTemplate):
    """A custom DocxTemplate class

    Added feature:
        Extended Verical Merge: {% evm [start_row_index_list] [counter] %}

            start_row_index_list: list of row indexes of the merged cell
            counter: a single counter variable in a list, e.g. [0]

    """

    def patch_xml(self, src_xml):
        src_xml = super().patch_xml(src_xml)

        # add extended vMerge functionality for merging cells that can't be merged in a nested table
        # use {% evm <start_row_index_list> <counter> %} to merge cells vertically
        # <start_row_index_list> is a list of row indexes that the merge starts, index starts from 0
        # <counter> is a single counter variable in a list
        def extend_v_merge_tc(m):
            def v_merge(m1):
                return (
                    '<w:vMerge w:val="{% if ' + m1.group(4) + '[0] in ' + m1.group(3) + ' %}restart{% else %}continue{% endif %}"/>' +
                    m1.group(1) +  # Everything between ``</w:tcPr>`` and ``<w:t>``.
                    "{% if " + m1.group(4) + "[0] in " + m1.group(3) + " %}" +
                    m1.group(2) +  # Everything before ``{% vm %}``.
                    m1.group(5) +  # Everything after ``{% vm %}``.
                    "{% endif %}" +
                    "{% if " + m1.group(4) + ".append(" + m1.group(4) + ".pop() + 1) %}{% endif %}" +
                    m1.group(6)  # ``</w:t>``.
                )
            return re.sub(
                r'(</w:tcPr[ >].*?<w:t(?:.*?)>)(.*?)(?:{%\s*evm\s+([^%]*)\s+([^%]*)\s+%})(.*?)(</w:t>)',
                v_merge,
                m.group(),  # Everything between ``</w:tc>`` and ``</w:tc>`` with ``{% vm %}`` inside.
                flags=re.DOTALL,
            )
        src_xml = re.sub(r'<w:tc[ >](?:(?!<w:tc[ >]).)*?{%\s*evm\s+([^%]*)\s+([^%]*)\s+%}.*?</w:tc[ >]',
                         extend_v_merge_tc, src_xml, flags=re.DOTALL)

        return src_xml
