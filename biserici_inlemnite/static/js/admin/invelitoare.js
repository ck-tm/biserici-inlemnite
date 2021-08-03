function show(group) {
    $(`#${group}-group .field-sindrila_lungime`).show()
    $(`#${group}-group .field-sindrila_lungime`).show()
    $(`#${group}-group .field-sindrila_latime_medie`).show()
    $(`#${group}-group .field-sindrila_grosime_medie`).show()
    $(`#${group}-group .field-sindrila_pasul_latuirii`).show()
    $(`#${group}-group .field-sindrila_pasul_baterii`).show()
    $(`#${group}-group .field-sindrila_numar_straturi`).show()
    $(`#${group}-group .field-sindrila_cu_horj`).show()
    $(`#${group}-group .field-sindrlia_tipul_de_batere`).show()
    $(`#${group}-group .field-sindrlia_tipul_prindere`).show()
    $(`#${group}-group .field-sindrlia_forma_botului`).show()
    $(`#${group}-group .field-sindrila_cu_tesitura`).show()
    $(`#${group}-group .field-sindrlia_prelucrare`).show()
    $(`#${group}-group .field-sindrlia_esenta_lemnoasa`).show()
}

function hide(group) {
    $(`#${group}-group .field-sindrila_lungime`).hide()
    $(`#${group}-group .field-sindrila_lungime`).hide()
    $(`#${group}-group .field-sindrila_latime_medie`).hide()
    $(`#${group}-group .field-sindrila_grosime_medie`).hide()
    $(`#${group}-group .field-sindrila_pasul_latuirii`).hide()
    $(`#${group}-group .field-sindrila_pasul_baterii`).hide()
    $(`#${group}-group .field-sindrila_numar_straturi`).hide()
    $(`#${group}-group .field-sindrila_cu_horj`).hide()
    $(`#${group}-group .field-sindrlia_tipul_de_batere`).hide()
    $(`#${group}-group .field-sindrlia_tipul_prindere`).hide()
    $(`#${group}-group .field-sindrlia_forma_botului`).hide()
    $(`#${group}-group .field-sindrila_cu_tesitura`).hide()
    $(`#${group}-group .field-sindrlia_prelucrare`).hide()
    $(`#${group}-group .field-sindrlia_esenta_lemnoasa`).hide()
}

$( document ).ready(function() {
  console.log('merge')
    const groups = ['finisaje_actuale', 'finisaje_tambur_turn', 'finisaje_invelitoare_turn']
    let material = ''

    for (let i = 0; i < groups.length; i++) {
        material = $(`#id_${groups[i]}-0-material`).val();
        console.log(groups[i], material)
        if (material == 4)
            show(groups[i])
        else 
            hide(groups[i])

        $(`#id_${groups[i]}-0-material`).change(function() {
            material = $(`#id_${groups[i]}-0-material`).val();
            if (material == 4)
                show(groups[i])
            else 
                hide(groups[i])
        });
    }
    

});



