import ipywidgets as ipw

def get_start_widget(appbase, jupbase):
    #http://fontawesome.io/icons/
    template = """
    <table>
    <tr>
        <th width="20%" style="text-align:center">Structures</th>
        <th width="20%" style="text-align:center">Slab Models</th>
        <th width="20%" style="text-align:center">Molecules</th>
        <th width="20%" style="text-align:center">Bulks</th>
        
    <tr>
    <td valign="top"><ul>
        <li><a href="{appbase}/upload_structure.ipynb" target="_blank">Upload structures</a>
        <li><a href="{appbase}/edit_structure.ipynb" target="_blank">Assign spin, remove atoms</a>
    </ul></td>
    
    <td valign="top"><ul>
        <li><a href="{appbase}/slab/build.ipynb" target="_blank">Construct slab</a>
        <li><a href="{appbase}/slab/submit_geopt.ipynb" target="_blank">Submit geo-opt</a>
        <li><a href="{appbase}/slab/search.ipynb" target="_blank">Search database</a>
        <li><a href="{appbase}/slab/submit_adsorption.ipynb" target="_blank">Adsorption energy</a>
    </ul></td>

    <td valign="top"><ul>
        <li><a href="{appbase}/molecules/submit_geoopt.ipynb" target="_blank">Submit Geo Opt</a>
        <li><a href="{appbase}/molecules/submit_gw.ipynb" target="_blank">Submit GW or GW+IC</a>
        <li><a href="{appbase}/molecules/search.ipynb" target="_blank">Search Optimized molecules</a>
    </ul></td>

    <td valign="top"><ul>
        <li><a href="{appbase}/bulks/upload_many_structures.ipynb" target="_blank">Upload Structures</a>
        <li><a href="{appbase}/bulks/submit_cellopt.ipynb" target="_blank">Submit Cell Opt</a>
        <li><a href="{appbase}/bulks/submit_bulkopt.ipynb" target="_blank">Submit Bulk Opt</a>
        <li><a href="{appbase}/bulks/search.ipynb" target="_blank">Search Cell Opt</a>
    </ul></td>


    <tr>
        <th width="60px" style="text-align:center">Constrained opt.</th>
        <th width="60px" style="text-align:center">Nudged Elastic Band</th>
    </tr>
    <tr>
    <td valign="top"><ul>
        <li><a href="{appbase}/reactions/replicas.ipynb" target="_blank">Generate replicas</a>
        <li><a href="{appbase}/reactions/SearchReplica.ipynb" target="_blank">Search replicas</a>
    </ul></td>
    <td><ul>
        <li><a href="{appbase}/reactions/NEB.ipynb" target="_blank">Submit NEB</a>
        <li><a href="{appbase}/reactions/SearchNEB.ipynb" target="_blank">Search NEBs</a>
    </ul></td>

    </tr></table>

"""
    
    html = template.format(appbase=appbase, jupbase=jupbase)
    return ipw.HTML(html)
    
#EOF
