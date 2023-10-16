import random
import string

import matplotlib.pyplot as plt  # Import the matplotlib library


def get_score(answers):
    score = 0
    for answer in answers:
        if answer == 1:
            score += 1
        elif answer == 2:
            score += 2
        elif answer == 3:
            score += 3
        elif answer == 4:
            score += 4
    return score


def calculate_t_score(section_score, section_average, section_std_dev):
    t_score = 50 + (section_score - section_average) / section_std_dev
    return t_score


def proccess(answers) -> dict:
    result_data = {}

    atencion_answers = []
    enganno_answers = []
    manipulacion_answers = []
    grandiosidad_answers = []
    interpersonal_answers = []
    irrespondabilidad_answers = []
    impulsividad_answers = []
    estimulo_answers = []
    distractibilidad_answers = []
    adiccion_answers = []
    aislamiento_answers = []
    depresivo_answers = []
    ansiosos_answers = []
    inestabilidad_answers = []
    hostil_answers = []
    rigidez_answers = []
    afecto_answers = []
    inseguridad_answers = []
    estres_answers = []
    hipomaniacas_answers = []
    inusuales_answers = []
    paranoia_answers = []
    desregulacion_answers = []
    excentricidad_answers = []

    # <---------------------->
    negacionproblemas_answers = []
    exageracionvirtudes_answers = []
    sobrereportedepsicopatia_answers = []
    exageraciondeseveridad_answers = []
    inconsistencia_answers = []
    afectonegativo_answers = []
    desapego_answers = []
    antagonismo_answers = []
    desinhibicion_answers = []
    psicotismo_answers = []

    for answer in answers:
        if len(atencion_answers) < 5:
            atencion_answers.append(answer)
        elif len(enganno_answers) < 5:
            enganno_answers.append(answer)
        elif len(manipulacion_answers) < 5:
            manipulacion_answers.append(answer)
        elif len(grandiosidad_answers) < 5:
            grandiosidad_answers.append(answer)
        elif len(interpersonal_answers) < 5:
            interpersonal_answers.append(answer)
        elif len(interpersonal_answers) < 5:
            irrespondabilidad_answers.append(answer)
        elif len(interpersonal_answers) < 5:
            impulsividad_answers.append(answer)
        elif len(estimulo_answers) < 5:
            estimulo_answers.append(answer)
        elif len(distractibilidad_answers) < 5:
            distractibilidad_answers.append(answer)
        elif len(adiccion_answers) < 5:
            adiccion_answers.append(answer)
        elif len(aislamiento_answers) < 5:
            aislamiento_answers.append(answer)
        elif len(depresivo_answers) < 5:
            depresivo_answers.append(answer)
        elif len(ansiosos_answers) < 5:
            ansiosos_answers.append(answer)
        elif len(inestabilidad_answers) < 5:
            inestabilidad_answers.append(answer)
        elif len(hostil_answers) < 5:
            hostil_answers.append(answer)
        elif len(rigidez_answers) < 5:
            rigidez_answers.append(answer)
        elif len(afecto_answers) < 5:
            afecto_answers.append(answer)
        elif len(inseguridad_answers) < 5:
            inseguridad_answers.append(answer)
        elif len(estres_answers) < 5:
            estres_answers.append(answer)
        elif len(estres_answers) < 5:
            estres_answers.append(answer)
        elif len(hipomaniacas_answers) < 5:
            hipomaniacas_answers.append(answer)
        elif len(inusuales_answers) < 5:
            inusuales_answers.append(answer)
        elif len(paranoia_answers) < 5:
            paranoia_answers.append(answer)
        elif len(desregulacion_answers) < 5:
            desregulacion_answers.append(answer)
        elif len(excentricidad_answers) < 5:
            excentricidad_answers.append(answer)

        elif len(negacionproblemas_answers) < 5:
            negacionproblemas_answers.append(answer)
        elif len(exageracionvirtudes_answers) < 5:
            exageracionvirtudes_answers.append(answer)
        elif len(sobrereportedepsicopatia_answers) < 5:
            sobrereportedepsicopatia_answers.append(answer)
        elif len(exageraciondeseveridad_answers) < 5:
            exageraciondeseveridad_answers.append(answer)
        elif len(inconsistencia_answers) < 5:
            inconsistencia_answers.append(answer)
        elif len(afectonegativo_answers) < 5:
            afectonegativo_answers.append(answer)
        elif len(desapego_answers) < 5:
            desapego_answers.append(answer)
        elif len(antagonismo_answers) < 5:
            antagonismo_answers.append(answer)
        elif len(desinhibicion_answers) < 5:
            desinhibicion_answers.append(answer)
        elif len(psicotismo_answers) < 5:
            psicotismo_answers.append(answer)

    # Calculate scores for each section
    atencion_score = get_score(atencion_answers)
    enganno_score = get_score(enganno_answers)
    manipulacion_score = get_score(manipulacion_answers)
    grandiosidad_score = get_score(grandiosidad_answers)
    interpersonal_score = get_score(interpersonal_answers)
    irresponsabilidad_score = get_score(interpersonal_answers)
    impulsividad_score = get_score(impulsividad_answers)
    estimulo_score = get_score(estimulo_answers)
    distractibilidad_score = get_score(distractibilidad_answers)
    adiccion_score = get_score(adiccion_answers)
    aislamiento_score = get_score(aislamiento_answers)
    depresivo_score = get_score(depresivo_answers)
    ansioso_score = get_score(ansiosos_answers)
    inestabilidad_score = get_score(inestabilidad_answers)
    hostil_score = get_score(hostil_answers)
    rigidez_score = get_score(rigidez_answers)
    afecto_score = get_score(afecto_answers)
    inseguridad_score = get_score(inseguridad_answers)
    estres_score = get_score(estres_answers)
    hipomaniacas_score = get_score(hipomaniacas_answers)
    inusuales_score = get_score(inusuales_answers)
    paranoia_score = get_score(paranoia_answers)
    desregulacion_score = get_score(desregulacion_answers)
    excentricidad_score = get_score(excentricidad_answers)
    negacionproblemas_score = get_score(negacionproblemas_answers)
    exageracionvirtudes_score = get_score(exageracionvirtudes_answers)
    sobrereportedepsicopatia_score = get_score(sobrereportedepsicopatia_answers)
    exageraciondeseveridad_score = get_score(exageraciondeseveridad_answers)
    inconsistencia_score = get_score(inconsistencia_answers)
    afectonegativo_score = get_score(afecto_answers)
    desapego_score = get_score(desapego_answers)
    antagonismo_score = get_score(antagonismo_answers)
    desinhibicion_score = get_score(desinhibicion_answers)
    psicotismo_score = get_score(psicotismo_answers)

    # Constants for section averages and standard deviations
    # Chart 1
    negacionproblemas_average = 42.5109
    negacionproblemas_std_dev = 7.21173
    exageracionvirtudes_average = 40.7664
    exageracionvirtudes_std_dev = 4.96694
    sobrereportedepsicopatia_average = 30.7956
    sobrereportedepsicopatia_std_dev = 6.6933
    exageraciondeseveridad_average = 38.8942
    exageraciondeseveridad_std_dev = 9.2372
    inconsistencia_average = 11.0000
    inconsistencia_std_dev = 4.0428
    afectonegativo_average = 85.943971
    afectonegativo_std_dev = 28.02867
    desapego_average = 38.313796
    desapego_std_dev = 11.73598
    antagonismo_average = 77.006043
    antagonismo_std_dev = 20.83766
    desinhibicion_average = 54.506158
    desinhibicion_std_dev = 13.31106
    psicotismo_average = 69.799650
    psicotismo_std_dev = 20.51200

    # ESPECTRO DE EXTERNALIZACIÓN
    atencion_average = 17.583082
    atencion_std_dev = 4.692501
    enganno_average = 20.319277
    enganno_std_dev = 5.654496
    manipulacion_average = 21.174962
    manipulacion_std_dev = 6.438614
    grandiosidad_average = 20.381599
    grandiosidad_std_dev = 5.107079
    interpersonal_average = 21.174962
    interpersonal_std_dev = 5.107079
    irresponsabilidad_average = 15.352378
    irresponsabilidad_std_dev = 5.643104
    impulsividad_average = 14.585899
    impulsividad_std_dev = 4.654283
    estimulo_average = 21.540682
    estimulo_std_dev = 6.091848
    distractibilidad_average = 19.023233
    distractibilidad_std_dev = 7.516042
    adiccion_average = 17.679697
    adiccion_std_dev = 9.231313
    # ESPECTRO DE INTERNALIZACIÓN
    aislamiento_average = 22.813468
    aislamiento_std_dev = 8.19557
    depresivo_average = 18.263572
    depresivo_std_dev = 8.42421
    ansiosos_average = 17.892442
    ansiosos_std_dev = 8.08490
    inestabilidad_average = 13.784177
    inestabilidad_std_dev = 4.94694
    hostil_average = 29.912396
    hostil_std_dev = 10.54092
    rigidez_average = 15.917559
    rigidez_std_dev = 3.76570
    afecto_average = 14.532853
    afecto_std_dev = 4.49279
    inseguridad_average = 13.727388
    inseguridad_std_dev = 3.82314
    estres_average = 18.685587
    estres_std_dev = 6.54518
    hipomaniacas_average = 19.516847
    hipomaniacas_std_dev = 5.20864
    # ESPECTRO DE PSICOTICISMO
    inusuales_average = 14.832992
    inusuales_std_dev = 5.42643
    paranoia_average = 23.722045
    paranoia_std_dev = 6.87312
    desregulacion_average = 12.927838
    desregulacion_std_dev = 5.29957
    excentricidad_average = 14.596008
    excentricidad_std_dev = 6.57116

    # Calculate T scores for each section
    negacionproblemas_t_score = calculate_t_score(
        negacionproblemas_score, negacionproblemas_average, negacionproblemas_std_dev
    )
    exageracionvirtudes_t_score = calculate_t_score(
        exageracionvirtudes_score,
        exageracionvirtudes_average,
        exageracionvirtudes_std_dev,
    )
    sobrereportedepsicopatia_t_score = calculate_t_score(
        sobrereportedepsicopatia_score,
        sobrereportedepsicopatia_average,
        sobrereportedepsicopatia_std_dev,
    )
    exageraciondeseveridad_t_score = calculate_t_score(
        exageraciondeseveridad_score,
        exageraciondeseveridad_average,
        exageraciondeseveridad_std_dev,
    )
    inconsistencia_t_score = calculate_t_score(
        inconsistencia_score, inconsistencia_average, inconsistencia_std_dev
    )
    afectonegativo_t_score = calculate_t_score(
        afectonegativo_score, afectonegativo_average, afectonegativo_std_dev
    )
    desapego_t_score = calculate_t_score(
        desapego_score, desapego_average, desapego_std_dev
    )
    antagonismo_t_score = calculate_t_score(
        antagonismo_score, antagonismo_average, antagonismo_std_dev
    )
    desinhibicion_t_score = calculate_t_score(
        desinhibicion_score, desinhibicion_average, desinhibicion_std_dev
    )
    psicotismo_t_score = calculate_t_score(
        psicotismo_score, psicotismo_average, psicotismo_std_dev
    )

    # <--------------------------------------------->
    atencion_t_score = calculate_t_score(
        atencion_score, atencion_average, atencion_std_dev
    )
    enganno_t_score = calculate_t_score(enganno_score, enganno_average, enganno_std_dev)
    manipulacion_t_score = calculate_t_score(
        manipulacion_score, manipulacion_average, manipulacion_std_dev
    )
    grandiosidad_t_score = calculate_t_score(
        grandiosidad_score, grandiosidad_average, grandiosidad_std_dev
    )
    interpersonal_t_score = calculate_t_score(
        interpersonal_score, interpersonal_average, interpersonal_std_dev
    )
    distractibilidad_t_score = calculate_t_score(
        distractibilidad_score, distractibilidad_average, distractibilidad_std_dev
    )
    adiccion_t_score = calculate_t_score(
        adiccion_score, adiccion_average, adiccion_std_dev
    )
    aislamiento_t_score = calculate_t_score(
        aislamiento_score, aislamiento_average, aislamiento_std_dev
    )
    depresivo_t_score = calculate_t_score(
        depresivo_score, depresivo_average, depresivo_std_dev
    )
    ansiosos_t_score = calculate_t_score(
        ansioso_score, ansiosos_average, ansiosos_std_dev
    )
    inestabilidad_t_score = calculate_t_score(
        inestabilidad_score, inestabilidad_average, inestabilidad_std_dev
    )
    irresponsabilidad_t_score = calculate_t_score(
        irresponsabilidad_score, irresponsabilidad_average, irresponsabilidad_std_dev
    )
    impulsividad_t_score = calculate_t_score(
        impulsividad_score, impulsividad_average, impulsividad_std_dev
    )
    estimulo_t_score = calculate_t_score(
        estimulo_score, estimulo_average, estimulo_std_dev
    )
    # <--------------------------------------------->
    hostil_t_score = calculate_t_score(hostil_score, hostil_average, hostil_std_dev)
    rigidez_t_score = calculate_t_score(rigidez_score, rigidez_average, rigidez_std_dev)
    afecto_t_score = calculate_t_score(afecto_score, afecto_average, afecto_std_dev)
    inseguridad_t_score = calculate_t_score(
        inseguridad_score, inseguridad_average, inseguridad_std_dev
    )
    estres_t_score = calculate_t_score(estres_score, estres_average, estres_std_dev)
    hipomaniacas_t_score = calculate_t_score(
        hipomaniacas_score, hipomaniacas_average, hipomaniacas_std_dev
    )
    inusuales_t_score = calculate_t_score(
        inusuales_score, inusuales_average, inusuales_std_dev
    )
    paranoia_t_score = calculate_t_score(
        paranoia_score, paranoia_average, paranoia_std_dev
    )
    desregulacion_t_score = calculate_t_score(
        desregulacion_score, desregulacion_average, desregulacion_std_dev
    )
    excentricidad_t_score = calculate_t_score(
        excentricidad_score, excentricidad_average, excentricidad_std_dev
    )

    characters = string.ascii_letters + string.digits
    file_name = "".join(random.choice(characters) for i in range(12))
    """
    FIRST CHART
    """
    # Update section names
    section_labels = [
        "NEGACIÓN DE PROBLEMAS",
        "EXAGERACIÓN DE VIRTUDES",
        "SOBREREPORTE DE PSICOPATOLOGÍA",
        "EXAGERACIÓN DE SEVERIDAD",
        "INCONSISTENCIA",
        "AFECTO NEGATIVO",
        "DESAPEGO",
        "ANTAGONISMO",
        "DESINHIBICIÓN",
        "PSICOTICISMO",
    ]

    t_scores = [
        negacionproblemas_t_score,
        exageracionvirtudes_t_score,
        sobrereportedepsicopatia_t_score,
        exageraciondeseveridad_t_score,
        inconsistencia_t_score,
        afectonegativo_t_score,
        desapego_t_score,
        antagonismo_t_score,
        desinhibicion_t_score,
        psicotismo_t_score,
    ]

    plt.figure(figsize=(12, 6))  # Adjust the figure size
    plt.plot(section_labels, t_scores, marker="o", linestyle="-")
    plt.title(
        "TINVENTARIO DIMENSIONAL DE PSICOPATOLOGÍA DE LA PERSONALIDAD (IDPP) SUPER ESPECTRO DE EXTERNALIZACIÓN"
    )
    plt.xlabel("Seccion")
    plt.ylabel("Puntajes T")
    plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
    plt.grid(True)
    plt.tight_layout()  # Adjust layout for better spacing
    plt.savefig(f"static/charts/{file_name}_first_chart.png")  # Save char as image
    result_data[
        "first_chart_titel"
    ] = "TINVENTARIO DIMENSIONAL DE PSICOPATOLOGÍA DE LA PERSONALIDAD (IDPP) SUPER ESPECTRO DE EXTERNALIZACIÓN"
    result_data["first_chart_path"] = f"charts/{file_name}_first_chart.png"

    """
    SECOND CHART
    """
    # Update section names
    section_labels = [
        "BÚSQUEDA DE ATENCIÓN",
        "TENDENCIA AL ENGAÑO",
        "RASGOS MANIPULATORIOS",
        "RASGOS DE GRANDIOSIDAD",
        "Interpersonal",
        "Distractibilidad",
        "Aislamiento",
        "Depresivo",
        "Ansioso",
        "Inestabilidad",
        "Irresponsabilidad",
        "Impulsividad",
        "Estimulo",
        "Distracciones",
        "Adiccion",
    ]

    t_scores = [
        atencion_t_score,
        enganno_t_score,
        manipulacion_t_score,
        grandiosidad_t_score,
        interpersonal_t_score,
        distractibilidad_t_score,
        aislamiento_t_score,
        depresivo_t_score,
        ansiosos_t_score,
        inestabilidad_t_score,
        irresponsabilidad_t_score,
        impulsividad_t_score,
        estimulo_t_score,
        distractibilidad_t_score,
        adiccion_t_score,
    ]

    plt.figure(figsize=(12, 6))  # Adjust the figure size
    plt.plot(section_labels, t_scores, marker="o", linestyle="-")
    plt.title(
        "TINVENTARIO DIMENSIONAL DE PSICOPATOLOGÍA DE LA PERSONALIDAD (IDPP) SUPER ESPECTRO DE EXTERNALIZACIÓN"
    )
    plt.xlabel("Seccion")
    plt.ylabel("Puntajes T")
    plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
    plt.grid(True)
    plt.tight_layout()  # Adjust layout for better spacing
    plt.savefig(f"static/charts/{file_name}_second_chart.png")  # Save char as image
    result_data[
        "second_chart_titel"
    ] = "TINVENTARIO DIMENSIONAL DE PSICOPATOLOGÍA DE LA PERSONALIDAD (IDPP) SUPER ESPECTRO DE EXTERNALIZACIÓN"
    result_data["second_chart_path"] = f"charts/{file_name}_second_chart.png"

    """
    THIRD CHART
    """
    # Update section names
    section_labels = [
        "Depresivos",
        "Ansiosos",
        "Inestabilidad",
        "Rasgos Hostiles",
        "Rigidez",
        "Inseguridad",
        "Estres",
    ]

    t_scores = [
        depresivo_t_score,
        ansiosos_t_score,
        inestabilidad_t_score,
        hostil_t_score,
        rigidez_t_score,
        inseguridad_t_score,
        estres_t_score,
    ]

    plt.figure(figsize=(12, 6))  # Adjust the figure size
    plt.plot(section_labels, t_scores, marker="o", linestyle="-")
    plt.title(
        "INVENTARIO DIMENSIONAL DE PSICOPATOLOGÍA DE LA PERSONALIDAD (IDPP) ESPECTRO DE INTERNALIZACIÓN"
    )
    plt.xlabel("Seccion")
    plt.ylabel("Puntajes T")
    plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
    plt.grid(True)
    plt.tight_layout()  # Adjust layout for better spacing
    plt.savefig(f"static/charts/{file_name}_third_chart.png")  # Save char as image
    result_data[
        "third_chart_titel"
    ] = "INVENTARIO DIMENSIONAL DE PSICOPATOLOGÍA DE LA PERSONALIDAD (IDPP) ESPECTRO DE INTERNALIZACIÓN"
    result_data["third_chart_path"] = f"charts/{file_name}_third_chart.png"

    """
    FOURTH CHART
    """
    section_labels = [
        "Inusuales",
        "Paranoia",
        "Cognitiva",
        "Excentricidad",
        "Hipomaniacas",
        "Aislamiento",
        "Afecto Rest",
    ]

    t_scores = [
        inusuales_t_score,
        paranoia_t_score,
        desregulacion_t_score,
        excentricidad_t_score,
        hipomaniacas_t_score,
        aislamiento_t_score,
        afecto_t_score,
    ]

    plt.figure(figsize=(12, 6))  # Adjust the figure size
    plt.plot(section_labels, t_scores, marker="o", linestyle="-")
    plt.title(
        "INVENTARIO DIMENSIONAL DE PSICOPATOLOGÍA DE LA PERSONALIDAD (IDPP) SUPER ESPECTRO DE PSICOSIS"
    )
    plt.xlabel("Seccion")
    plt.ylabel("Puntajes T")
    plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
    plt.grid(True)
    plt.tight_layout()  # Adjust layout for better spacing
    plt.savefig(f"static/charts/{file_name}_fourth_chart.png")  # Save char as image
    result_data[
        "fourth_chart_titel"
    ] = "INVENTARIO DIMENSIONAL DE PSICOPATOLOGÍA DE LA PERSONALIDAD (IDPP) SUPER ESPECTRO DE PSICOSIS"
    result_data["fourth_chart_path"] = f"charts/{file_name}_fourth_chart.png"

    return result_data
