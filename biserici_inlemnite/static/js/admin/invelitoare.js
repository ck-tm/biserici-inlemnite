
function show(group) {
    $(`div[data-contentpath="${group}_sindrila_lungime"]`).parent().show()
    $(`div[data-contentpath="${group}_sindrila_latime_medie"]`).parent().show()
    $(`div[data-contentpath="${group}_sindrila_grosime_medie"]`).parent().show()
    $(`div[data-contentpath="${group}_sindrila_pasul_latuirii"]`).parent().show()
    $(`div[data-contentpath="${group}_sindrila_pasul_baterii"]`).parent().show()
    $(`div[data-contentpath="${group}_sindrila_numar_straturi"]`).parent().show()
    $(`div[data-contentpath="${group}_sindrila_cu_horj"]`).parent().show()
    $(`div[data-contentpath="${group}_sindrlia_tipul_de_batere"]`).parent().show()
    $(`div[data-contentpath="${group}_sindrlia_tipul_prindere"]`).parent().show()
    $(`div[data-contentpath="${group}_sindrlia_forma_botului"]`).parent().show()
    $(`div[data-contentpath="${group}_sindrila_cu_tesitura"]`).parent().show()
    $(`div[data-contentpath="${group}_sindrlia_prelucrare"]`).parent().show()
    $(`div[data-contentpath="${group}_sindrlia_esenta_lemnoasa"]`).parent().show()
}
// function show(group) {
//     $(`#${group}-group .field-sindrila_lungime`).show()
//     $(`#${group}-group .field-sindrila_lungime`).show()
//     $(`#${group}-group .field-sindrila_latime_medie`).show()
//     $(`#${group}-group .field-sindrila_grosime_medie`).show()
//     $(`#${group}-group .field-sindrila_pasul_latuirii`).show()
//     $(`#${group}-group .field-sindrila_pasul_baterii`).show()
//     $(`#${group}-group .field-sindrila_numar_straturi`).show()
//     $(`#${group}-group .field-sindrila_cu_horj`).show()
//     $(`#${group}-group .field-sindrlia_tipul_de_batere`).show()
//     $(`#${group}-group .field-sindrlia_tipul_prindere`).show()
//     $(`#${group}-group .field-sindrlia_forma_botului`).show()
//     $(`#${group}-group .field-sindrila_cu_tesitura`).show()
//     $(`#${group}-group .field-sindrlia_prelucrare`).show()
//     $(`#${group}-group .field-sindrlia_esenta_lemnoasa`).show()
// }

// function hide(group) {
//     $(`#${group}-group .field-sindrila_lungime`).hide()
//     $(`#${group}-group .field-sindrila_lungime`).hide()
//     $(`#${group}-group .field-sindrila_latime_medie`).hide()
//     $(`#${group}-group .field-sindrila_grosime_medie`).hide()
//     $(`#${group}-group .field-sindrila_pasul_latuirii`).hide()
//     $(`#${group}-group .field-sindrila_pasul_baterii`).hide()
//     $(`#${group}-group .field-sindrila_numar_straturi`).hide()
//     $(`#${group}-group .field-sindrila_cu_horj`).hide()
//     $(`#${group}-group .field-sindrlia_tipul_de_batere`).hide()
//     $(`#${group}-group .field-sindrlia_tipul_prindere`).hide()
//     $(`#${group}-group .field-sindrlia_forma_botului`).hide()
//     $(`#${group}-group .field-sindrila_cu_tesitura`).hide()
//     $(`#${group}-group .field-sindrlia_prelucrare`).hide()
//     $(`#${group}-group .field-sindrlia_esenta_lemnoasa`).hide()
// }

function hide(group) {
    $(`div[data-contentpath="${group}_sindrila_lungime"]`).parent().hide()
    $(`div[data-contentpath="${group}_sindrila_latime_medie"]`).parent().hide()
    $(`div[data-contentpath="${group}_sindrila_grosime_medie"]`).parent().hide()
    $(`div[data-contentpath="${group}_sindrila_pasul_latuirii"]`).parent().hide()
    $(`div[data-contentpath="${group}_sindrila_pasul_baterii"]`).parent().hide()
    $(`div[data-contentpath="${group}_sindrila_numar_straturi"]`).parent().hide()
    $(`div[data-contentpath="${group}_sindrila_cu_horj"]`).parent().hide()
    $(`div[data-contentpath="${group}_sindrlia_tipul_de_batere"]`).parent().hide()
    $(`div[data-contentpath="${group}_sindrlia_tipul_prindere"]`).parent().hide()
    $(`div[data-contentpath="${group}_sindrlia_forma_botului"]`).parent().hide()
    $(`div[data-contentpath="${group}_sindrila_cu_tesitura"]`).parent().hide()
    $(`div[data-contentpath="${group}_sindrlia_prelucrare"]`).parent().hide()
    $(`div[data-contentpath="${group}_sindrlia_esenta_lemnoasa"]`).parent().hide()
}

$( document ).ready(function() {
  console.log('merge')
    const groups = ['invelitoare_corp', 'invelitoare_turn', 'inchidere_tambur_turn']
    let material = ''

    for (let i = 0; i < groups.length; i++) {
        material = $(`#id_${groups[i]}_material`).val();
        console.log(groups[i], material)
        if (material == 4){
            show(groups[i])
        }
        else {
            console.log('hide')
            hide(groups[i])
        }

        $(`#id_${groups[i]}_material`).change(function() {
            material = $(`#id_${groups[i]}_material`).val();
            console.log(groups[i], material)
            if (material == 4)
                show(groups[i])
            else 
                hide(groups[i])
        });
    }
    

});



