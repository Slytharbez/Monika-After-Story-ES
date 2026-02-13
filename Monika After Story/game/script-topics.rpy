
default persistent._topic_database = dict()
init offset = 5

default -5 persistent._jn_out_of_topics_warning_given = False


default -5 persistent._jn_player_pet = None


default -5 persistent.jn_player_favourite_season = None


default -5 persistent.jn_player_appearance_declined_share = False
default -5 persistent.jn_player_appearance_eye_colour = None
default -5 persistent.jn_player_appearance_hair_length = None
default -5 persistent.jn_player_appearance_hair_colour = None
default -5 persistent.jn_player_appearance_height_cm = None
default -5 persistent._jn_player_birthday_day_month = None
default -5 persistent._jn_player_birthday_is_leap_day = False
default -5 persistent._jn_player_is_multilingual = None
default -5 persistent._jn_player_had_work_placement = None


default -5 persistent.jn_player_gaming_frequency = None
default -5 persistent.jn_player_can_drive = None
default -5 persistent._jn_player_has_flown = None


default -5 persistent.jn_player_love_you_count = 0


default -5 persistent.jn_player_tea_coffee_preference = None

init -5 python in topics:
    import store
    TOPIC_MAP = dict()


label talk_out_of_topics:
    if Natsuki.isNormal(higher=True):
        n 3kllpo "Uhmm..."
        n 1knmaj "Oye...{w=0.5}{nw}"
        extend 4knmss " ¿[player]?"
        n 1fslss "Emm...{w=0.3} me está costando un poco pensar en más cosas de las que quiero hablar."
        n 1ulraj "Así que...{w=0.5}{nw}"
        extend 1nsrss " no creo que hable mucho hasta que se me ocurra algo más."
        n 3nsrpo "..."
        n 4tnmem "¿Qué?{w=0.5}{nw}"
        extend 3fllpol " ¡No hablo solo porque me guste el sonido de mi propia voz,{w=0.1} sabes!"
        n 1tllpu "Pero...{w=0.5}{nw}"
        extend 1unmbo " supongo que {i}podría{/i} contarte cualquier cosa que se me venga a la mente."
        n 1nchbg "Entonces...{w=0.3} ¿qué dices?"

        show natsuki 2nsrsssbl
        menu:
            n "¿Te importa si repito algunas cosas,{w=0.2} o...?"
            "Claro, no me importa escuchar":

                $ persistent.jn_natsuki_repeat_topics = True

                n 4uchgn "¡Okaaay!{w=0.5}{nw}"
                extend 1tcsaj " Ahora,{w=0.2} déjame pensar..."
            "No me importa escuchar, pero no me recuerdes la próxima vez":

                $ persistent.jn_natsuki_repeat_topics = True
                $ persistent._jn_natsuki_out_of_topics_remind = False

                n 2tnmboeqm "¿Huh?{w=0.75}{nw}"
                extend 2unmfl " Oh.{w=0.75}{nw}"
                extend 2nslsssbl " Cierto.{w=0.5} Claro."
                n 2cslsl "Ahora,{w=0.2} déjame pensar..."
            "Prefiero esperar":

                n 2tllaj "Bueno...{w=0.5}{nw}"
                extend 2tnmbo " si estás seguro."

                if Natsuki.isAffectionate(higher=True):
                    n 2kwmpol "Trataré de que se me ocurra algo pronto,{w=0.5}{nw}"
                    extend 4klrssl " ¿vale?"
                else:

                    n 1flrpol "S-{w=0.2}¡solo no hagas que el silencio se ponga incómodo,{w=0.2} entendiste?!"
            "Prefiero esperar, pero no me recuerdes la próxima vez":

                $ persistent._jn_natsuki_out_of_topics_remind = False

                n 2tsqpueqm "¿Huh?{w=0.75}{nw}"
                extend 2unmfl " Oh.{w=0.75}{nw}"
                extend 2csrsssbl " Je."
                n 2clrsl "Bueno...{w=1}{nw}"
                extend 2tnmca " si estás seguro,{w=0.2} [player]."

                if Natsuki.isAffectionate(higher=True):
                    n 4cllss "I'll...{w=1}{nw}"
                    extend 1cslbosbr " trataré de pensar en algo pronto."

    elif Natsuki.isDistressed(higher=True):
        n 1nllsf "..."
        n 1fllaj "Sí,{w=0.1} bueno.{w=0.5}{nw}"
        extend 1fnmsl " No tengo nada más que decir."
        n 2fsqpu "...O cosas que quiera contarte a {i}ti{/i},{w=0.1} de todas formas."
        n 2fslsr "Así que solo me voy a callar."
        n 1fcsun "Je.{w=0.5}{nw}"
        extend 1fsqun " No es como si eso fuera un {i}problema{/i} para ti,{w=0.1} ¿eh?"
    else:

        n 2fslun "...{w=2}{nw}"
        extend 1fsqem " ¿Qué?"
        n 2fcsan "Eres la {i}última{/i} persona con la que quiero pensar en más cosas de qué hablar.{w=1}{nw}"
        extend 1fsrem " Idiota."

    $ persistent._jn_out_of_topics_warning_given = True
    return




init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_did_you_have_pets",
            unlocked=True,
            prompt="¿Alguna vez tuviste mascotas?",
            category=["Animales", "Familia"],
            player_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_did_you_have_pets:
    if get_topic("talk_did_you_have_pets").shown_count > 0:
        n 4unmaj "¿Huh?{w=0.75}{nw}"
        extend 4tnmpu " ¿Mascotas?"
        n 3ccspu "Espera...{w=1}{nw}"
        extend 7tnmbo " ¿no hablamos ya de esto,{w=0.2} [player]?{w=1}{nw}"
        extend 7clrpu " Huh."
        n 2ulraj "Bueno,{w=0.2} como sea.{w=0.75}{nw}"
        extend 2tnmsl " Estoy bastante segura de que no necesitabas que te dijera que {i}eso{/i} no ha cambiado.{w=1}{nw}"
        extend 2cslca " Como puedes ver."

        if jn_desk_items.getDeskItem("jn_sanjo").unlocked:
            n 2csrss "No es como si Sanjo contara realmente como mascota tampoco,{w=0.5}{nw}"
            extend 2csrbo " antes de que digas nada."

        n 4ccsfl "...Y de hecho,{w=0.5}{nw}"
        extend 7csrfl " ahora que lo pienso..."
        n 7tnmfl "¿De dónde siquiera {i}sacaría{/i} una ahora de todas formas?{w=0.75}{nw}"
        extend 4clremsbl " ¡D-{w=0.2}deja tú todas las cosas que necesitaría para mantenerla aquí!"
        n 2nsqem "No pensarías en serio que tengo todo ese equipo ahí tirado en mi escritorio o algo,{w=0.2} ¿verdad?"
        n 4cslflsbr "...Y de alguna forma dudo que el armario se haya quedado abastecido con comida de mascota y arena de gato,{w=0.75}{nw}"
        extend 4cllbosbr " de entre todas las cosas."
        n 2unmfl "Digo,{w=0.5}{nw}"
        extend 2ccsgs " ¡no me malinterpretes!{w=0.5}{nw}"
        extend 2clrfll " No es como si no me {i}gustaría{/i} la compañía."

        if Natsuki.isEnamored(higher=True):
            n 2ccsbolsbr "T-{w=0.2}tanto como tenerte aquí ayuda.{w=0.75}{nw}"

        elif Natsuki.isAffectionate(higher=True):
            n 2fcsajlsbr "E-{w=0.2}entre tus visitas,{w=0.2} quiero decir.{w=0.75}{nw}"
        else:

            n 2fcsemlsbr "¡C-{w=0.2}claro que me gustaría!{w=0.75}{nw}"

        extend 4clrsll " Pero..."
        n 4tnmpu "¿Mantener algo {i}más{/i} aquí?{w=0.75}{nw}"
        extend 5cllpu " Eso es..."

        if Natsuki.isAffectionate(higher=True):
            n 5kslslsbl "..."
            n 7cllslsbl "Supongo que simplemente no se sentiría justo...{w=1}{nw}"
            extend 7knmbosbrl " ¿sabes?{w=0.75}{nw}"
            extend 4klrbolsbr " Como que..."
            n 2ccsfl "Y-{w=0.2}yo sé que ya estoy atrapada aquí.{w=0.75}{nw}"
            extend 2clrfl " ¿{i}Realmente{/i} quiero forzar eso en algo más también?{w=0.75}{nw}"
            extend 2ksrpusbr " ¿Solo por mi propio bien?"

            if Natsuki.isEnamored(higher=True):
                n 7ksrslsbr "..."
                n 7kcsflsbr "No lo sé, {w=0.2}[player].{w=0.75}{nw}"
                n 4kllflsbr "Simplemente..."
                n 4kslcasbr "..."
                n 2ccsfll "Simplemente no me sienta bien.{w=0.75}{nw}"
                extend 2csrsll " A-{w=0.2}Al menos justo {i}ahora{/i}."
                n 2nsrbol "..."
            else:

                n 1cslsllsbr "..."
                n 4ccsfllsbr "O-{w=0.2}olvídalo.{w=0.75}{nw}"
                extend 3ccsajsbl " Simplemente no sería justo para lo que fuera.{w=0.75}{nw}"
                extend 3ccscasbl " Es todo lo que digo."

            n 4ccsemsbl "C-{w=0.2}como sea.{w=0.75}{nw}"
            extend 4ullaj " Creo que ya he hablado suficiente.{w=0.75}{nw}"
            extend 3cllbo " Pero..."

            if Natsuki.isAffectionate(higher=True):
                n 3tnmbo "¿Por qué toda esta charla de mascotas tan de repente,{w=0.2} [player]?{w=0.75}{nw}"
                extend 3fsqss " ¿Hay algo que no me estás contando?"
                n 3fsqsm "..."
                n 3fcsbg "¿Y bien?{w=0.75}{nw}"
                $ chosen_descriptor = jn_utils.getRandomTease() if Natsuki.isEnamored(higher=True) else player
                extend 4fchgn " ¡Desembucha ya,{w=0.2} [chosen_descriptor]!"

                show natsuki option_wait_smug
            else:

                n 7tnmaj "¿Por qué toda esta charla de mascotas tan de repente,{w=0.2} [player]?"

                show natsuki option_wait_curious
        else:

            n 1cslsllsbr "..."
            n 4ccsfllsbr "O-{w=0.2}olvídalo.{w=0.75}{nw}"
            extend 3ccsajsbl " Simplemente no sería justo para lo que fuera.{w=0.75}{nw}"
            extend 3ccscasbl " Es todo lo que digo."
            n 3tlraj "Pero...{w=1}{nw}"
            extend 7tnmbo " ¿por qué toda esta charla de mascotas tan de repente,{w=0.2} [player]?"

            show natsuki option_wait_curious
    else:

        n 3tnmboeqm "¿Huh?{w=0.75}{nw}"
        extend 3tsqfl " ¿Que si alguna vez tuve mascotas?"
        n 1fcssl "Je.{w=0.75}{nw}"
        extend 4fllfl " Ya quisiera.{w=0.75}{nw}"
        extend 4fcswr " ¡Como si eso fuera a pasar con {i}mis{/i} padres!"

        if jn_desk_items.getDeskItem("jn_sanjo").unlocked:
            n 4ccsem "...Y no,{w=0.5}{nw}"
            extend 4csrsl " Sanjo no cuenta."
            n 4fnmem "Pero en serio -{w=0.5}{nw}"
        else:

            n 4fnmem "En serio -{w=0.5}{nw}"

        extend 2flrwr " ¡Nunca me permitieron tener nada!{w=0.75}{nw}"
        extend 2fcsan " ¡Siempre había alguna razón {i}conveniente{/i} por la que no podía pasar!"
        n 1fcsgs "Y solo para rematar..."
        n 3fllwr "¡No era como si las excusas tuvieran {i}sentido{/i} tampoco!{w=0.75}{nw}"
        extend 3fcsanean " ¡Cada maldita vez que intentaba sacar el tema!"
        n 6flrgs "Siempre era sobre el desastre que haría,{w=0.5}{nw}"
        extend 6fllem " o cómo lo pagaríamos,{w=0.5}{nw}"
        extend 3fsrem " o literalmente cualquier otra cosa que se les ocurriera..."
        n 4fcsan "...¡Incluso cuando ya había {i}dicho{/i} que yo me encargaría de todo eso yo misma!"
        n 2fcsemesi "Ugh..."
        n 2fsrsll "Hablemos de cosas que {i}sacan de quicio{/i}.{w=1}{nw}"
        extend 2csrfl " Pero supongo que no es como si nada de eso importara ahora,{w=0.2} de todas formas.{w=1}{nw}"
        extend 2cllbosbr " Estando atrapada aquí y todo."
        n 2cslbosbr "..."
        n 2ullaj "Aunque...{w=1}{nw}"
        extend 7tnmbo " ¿qué hay de ti,{w=0.2} [player]?"

        show natsuki option_wait_curious

    $ player_has_pet = persistent._jn_player_pet is not None
    $ prompt = "¿Tienes alguna mascota,{w=0.2} o...?" if not player_has_pet else "¿Acabas de conseguir otra mascota,{w=0.2} o...?"
    $ response_yes = "Sí, tengo." if not player_has_pet else "Sí, conseguí otra."
    $ response_no = "No, no tengo." if not player_has_pet else "No, no conseguí."
    $ response_gone = "Solía tener." if not player_has_pet else "Perdí una."

    menu:
        n "[prompt]"
        "[response_yes]":

            n 1uspgs "¡Oh! {w=0.5}{nw}"
            extend 4fchbs "¡Oh{w=0.2} oh{w=0.2} oh!"
            n 4unmbs "¡Vamos!{w=0.75}{nw}"
            extend 3unmbg " ¡Tienes que decirme,{w=0.2} [player]!{w=0.75}{nw}"

            if player_has_pet:
                extend 3uchgnedz " ¿Qué conseguiste?{w=0.2} ¿Qué conseguiste?"
            else:

                extend 3uchgnedz " ¿Qué es?{w=0.2} ¿Qué es?"

            show natsuki option_wait_excited at jn_left

            $ pet_options = [
                ("Pájaros", "birds"),
                ("Gatos", "cats"),
                ("Camaleones", "chameleons"),
                ("Perros", "dogs"),
                ("Hurones", "ferrets"),
                ("Peces", "fish"),
                ("Ranas", "frogs"),
                ("Geckos", "geckos"),
                ("Gerbos", "gerbils"),
                ("Cuyos", "guinea_pigs"),
                ("Hámsteres", "hamsters"),
                ("Caballos", "horses"),
                ("Insectos", "insects"),
                ("Lagartijas", "lizards"),
                ("Ratones", "mice"),
                ("Ratas", "rats"),
                ("Conejos", "rabbits"),
                ("Serpientes", "snakes"),
                ("Algo más", "something_else")
            ]
            $ pet_options.sort()
            call screen scrollable_choice_menu(items=pet_options)
            $ persistent._jn_player_pet = _return
            show natsuki at jn_center
        "[response_no]":

            n 4cllfl "Hombre...{w=1}{nw}"
            extend 4tsqfl " ¿en serio?"
            n 2nsrsl "..."
            n 2nsraj "Bueno...{w=1}{nw}"
            extend 1nlrbo " tengo que admitirlo.{w=0.75}{nw}"
            extend 3nsrfl " Estaría mintiendo si dijera que no estoy al menos {i}algo{/i} decepcionada."

            if player_has_pet:
                n 3cslss "Incluso si {i}sí{/i} dijiste que tenías [player_pet_es] ya."
                n 3cslbosbr "..."

            if Natsuki.isAffectionate(higher=True):
                n 3ullaj "Bueno, {w=0.2} como sea. {w=0.75}{nw}"
                extend 1ccsss "No es como si la gente consiguiera mascotas regularmente o algo así,{w=0.2} despues de todo."
                n 4fsqss "Pero no empieces a pensar que eso significa que te salvaste,{w=0.2} [player].{w=0.75}{nw}"
                extend 4fsqsm " Ehehe."
                n 3fchbg "¡Nop!{w=0.75}{nw}"

                if Natsuki.isEnamored(higher=True):
                    extend 3fcsbg " Como si fuera a perderme esa clase de noticias.{w=0.75}{nw}"
                    extend 3flrss " Y además..."
                    n 6fcsbgeme "Algo me dice que simplemente {i}tendrías{/i} que compartirlo conmigo,{w=0.2} de todos modos."
                    n 4fsqsm "...¿No es así?{w=0.75}{nw}"
                    extend 1fchsm " Ahaha."
                else:

                    extend 3fcsbg " Como si fuera a perderme esa clase de noticias.{w=0.75}{nw}"
                    extend 7nchgn " ¡Mejor cuéntamelo todo!"
            else:

                n 7ulraj "Bueno...{w=1}{nw}"
                extend 7tnmbo " solo avísame cuando eso cambie,{w=0.2} supongo.{w=0.75}{nw}"
                extend 3fcssmesm " ¡Todavía quiero escuchar todo al respecto!"

            return
        "[response_gone]":

            if Natsuki.isAffectionate(higher=True):
                n 4klrbo "..."
                n 4klrpusbr "Y...{w=1}{nw}"
                extend 5ksrpusbr " y-yo realmente no se que decir,{w=0.2} [player]."
                n 4ccsflsbr "Solo..."
                n 1kslslsbl "..."
                n 4ccsslsbl "...Solo no te lo guardes si no tienes que hacerlo.{w=0.75}{nw}"
                extend 4cnmflsbl " ¿Entendido?"
                n 5csrsllsbl "D-{w=0.2}deberías saber que tienes gente a tu alrededor que te escucharía."

                if Natsuki.isEnamored(higher=True):
                    n 4ksrsllsbl "..."
                    n 4knmflsbr "...¿Y [player]?"
                    n 5kllbosbr "..."
                    n 5ccspulsbr "Y...{w=1.25}{nw}"
                    extend 4clrpulsbr " yo sé que dije que nunca tuve mascota ni nada de eso.{w=0.75}{nw}"
                    extend 1csrpulsbr " Ni de cerca.{w=1}{nw}"
                    extend 1ksrsll " Pero..."
                    n 2ksrbol "..."
                    n 2ksrajl "...Sabes que he perdido amigos también.{w=0.75}{nw}"
                    extend 2ksqcal " ¿Cierto?"
                    n 2ccsfllsbl "N-{w=0.2}no estoy diciendo que {i}sé{/i} como te sientes.{w=0.75}{nw}"
                    extend 2cllfllsbl " ¡Claro que no!{w=0.75}{nw}"
                    extend 2cllbolsbl " Solo tú sabes eso,{w=0.2} [player].{w=1.5}{nw}"
                    extend 4kslbolsbl " Pero..."
                    n 1ccsbolesisbl "..."
                    n 1kslsll "...Entiendo.{w=0.75}{nw}"
                    extend 4ksqsll " ¿Vale?"
                    n 4knmcal "De verdad."

                    if Natsuki.isLove(higher=True):
                        n 5ksrbol "...Lo entiendo.{w=1.25}{nw}"
                        extend 1ccsfllsbl " Solo quería que supieras eso también."
                        n 4ksrcal "..."
                        n 4ksqbol "...¿Y [player]?"
                        n 5kslsllsbl "..."

                        show natsuki 4ccssllsbr at jn_center
                        play audio chair_out
                        show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
                        $ jnPause(2)
                        play audio clothing_ruffle
                        show natsuki 1ccscalsbr at jn_center
                        $ jnPause(3)
                        play audio chair_in
                        $ jnPause(3)
                        hide black with Dissolve(1.25)
                    else:

                        n 5ksrbol "...Lo entiendo. {w=0.75}{nw}"
                        extend 1ccsfllsbl "Solo quería que supieras eso también. {w=1.25}{nw}"
                        extend 1cllpulsbl "Pero..."
                        n 4cslbolsbl "..."
                        n 4kslbolsbl "... Sí."

                n 5kslcal "..."
                n 4nslajl "Así que..."
                n 4tnmsllsbr "¿Querías hablar de otra cosa,{w=0.2} o...?"
            else:

                n 4ccsemsbr "E-{w=0.2}espera.{w=0.75}{nw}"
                extend 4knmemsbr " Tú..."
                n 1ksrpusbr "...Oh.{w=1}{nw}"
                extend 4ksrflsbr " Jeez."
                n 5kslbosbr "..."
                n 4ccsflsbl "E...{w=1.25}{nw}"
                extend 2cllslsbl " en serio lamento escuchar eso,{w=0.2} [player].{w=1}{nw}"
                extend 2kslbolsbl " D-{w=0.2}de verdad."
                n 4kslcalsbr "..."
                n 4ccsemlsbr "...Tal vez deberíamos hablar de otra cosa por ahora.{w=0.75}{nw}"
                extend 2cnmemlsbr " S-{w=0.2}si quisieras,{w=0.5}{nw}"
                extend 2nsrbolsbr " digo."
                n 4ksrcalsbr "..."

            return

    if persistent._jn_player_pet == "birds":
        n 1unmaj "¿Oh?{w=0.75}{nw}"
        extend 2tnmss " Pájaros,{w=0.2} ¿eh?{w=0.75}{nw}"
        extend 2fchsm " ¡Genial!"
        n 1flrss "Apuesto a que entraste en todo un{w=0.5}{nw}"
        extend 4fsqbg " {i}aleteo{/i}{w=0.75}{nw}"
        extend 4usqbg " cuando viste el tuyo por primera vez,{w=0.2} ¿eh?"

        if Natsuki.isLove(higher=True):
            n 3fcssmeme "Ehehe.{w=0.75}{nw}"
            extend 3fwlbgl " ¡Te amo,{w=0.2} [player]~!"
        else:

            n 3fchsmeme "Ehehe."

    elif persistent._jn_player_pet == "cats":
        n 4unmbg "¿Gatitos?{w=0.75}{nw}"
        extend 4uchgn " ¡{i}Ahora{/i} sí estamos hablando,{w=0.2} [player]!"

        if Natsuki.isAffectionate(higher=True):
            n 4clraj "Bueno..."
            n 3ccsbglsbl "A menos que solo hayas dicho eso esperando que a {i}mí{/i} me gusten también,{w=0.2} de todas formas."
        else:

            n 2nllaj "Aunque...{w=1}{nw}"
            extend 2fllss " tengo que preguntar."
            n 4fcsbg "...¿Exactamente de cuántos videos has hecho a los {i}tuyos{/i} estrellas,{w=0.5}{nw}"
            extend 4fsqbg " [player]?"

        n 3usqsm "..."
        n 3fcssm "¿Oh?{w=0.75}{nw}"
        extend 7fcsbg " ¿Qué pasa,{w=0.2} [player]?"
        extend 7fchgn " ¿Te descubrí?"
        n 4ulraj "Bueno,{w=0.2} como sea.{w=0.75}{nw}"
        extend 3fcsaj " ¡Más te vale estar cuidando bien de los tuyos,{w=0.2} [player]!"
        n 3fcspo "...O realmente te daré un {i}zarpazo{/i} de realidad.{w=0.75}{nw}"

        if Natsuki.isLove(higher=True):
            extend 3fchsmeme " Ehehe."
            n 3fchbll "¡Te amo también,{w=0.2} [player]~!"
        else:

            extend 3fchsmeme " Ehehe."

    elif persistent._jn_player_pet == "chameleons":
        n 4tnmfl "¿Camaleones?{w=0.75}{nw}"
        extend 7unmbo " ¿Como con los ojos locos giratorios y todo eso?{w=0.75}{nw}"
        extend 7clrbo " Huh."
        n 7clrfl "Yo...{w=1}{nw}"
        extend 3tnmbo " ni siquiera sabía que la gente tenía de esos,{w=0.2} honestamente.{w=0.75}{nw}"
        extend 3tllss " Genial."
        n 1fcssm "...Je."
        n 4flrss "Bueno...{w=1}{nw}"
        extend 3fcsbg " ¡déjame de {i}colores{/i} con la sorpresa!"
        extend 3fchsm " Ehehe."

        if Natsuki.isEnamored(higher=True):
            n 4nchgn "¡Sin arrepentimientos,{w=0.2} [player]!"

    elif persistent._jn_player_pet == "dogs":
        n 7unmaj "Perros,{w=0.2} ¿eh?{w=0.75}{nw}"
        extend 4fchsm " ¡Cool!"
        n 4csrss "...Aunque no me veo a mí misma teniendo uno,{w=0.2} la verdad.{w=0.75}{nw}"
        extend 2csrpo " Con los paseos todos los días y todo eso."

        if get_topic("talk_skateboarding").shown_count > 0:
            n 2fcsaj "¡Nop!{w=0.75}{nw}"
            extend 2fcsbg " ¡La patineta es más que suficiente para mí!"
        else:

            n 2fcsaj "¡Nop!{w=0.75}{nw}"
            extend 2fcsgs " Tomaré mis paseos cuando {i}yo{/i} los quiera,{w=0.5}{nw}"
            extend 2fcspo " muchas gracias."
            n 2fsqsm "Ehehe."

        n 4ullaj "Bueno,{w=0.2} como sea -{w=0.5}{nw}"
        extend 4ccstr " mejor asegúrate de estar cuidando de los tuyos,{w=0.2} [player]..."
        n 2csqpo "O realmente tendré un {i}hueso{/i} duro de roer contigo."

    elif persistent._jn_player_pet == "ferrets":
        n 7clrpu "Sabes...{w=1}{nw}"
        extend 7cnmbo " siempre me pregunté sobre los hurones.{w=0.75}{nw}"
        extend 7tslpu " ¿Es más como tener un gato o un perro?"
        n 7cslbo "Huh."
        n 4ullaj "Bueno como sea...{w=1}{nw}"
        extend 4fcstr " como sea que sean.{w=0.75}{nw}"
        extend 2fcssmesm " ¡Más te vale estar cuidando del pequeño!"

        if Natsuki.isLove(higher=True):
            n 5flrssl "Al menos tanto como me cuidas a mí,{w=0.2} de todas formas."
            n 7tlrajl "Bueno...{w=1}{nw}"
            extend 3fsqssl " {i}casi{/i} tanto.{w=0.75}{nw}"
            extend 3fchsml " Ehehe."

    elif persistent._jn_player_pet == "fish":
        n 3tllpu "Peces,{w=0.5}{nw}"
        extend 3tnmbo " ¿huh?"
        n 7tlrbo "..."
        n 7tlrss "Bueno...{w=1}{nw}"
        extend 5csrss " No los llamaría {i}súper{/i} cariñosos ni nada...{w=1}{nw}"
        extend 7ulrca " pero supongo que puedo ver las razones para tenerlos.{w=0.75}{nw}"
        extend 7unmbg " ¡Como para el estrés!"
        n 4fcsss "Je."
        n 3fcssm "Apuesto a que sientes que podrías perderte en ese tanque,{w=0.5}{nw}"
        extend 3fsqsm " ¿eh?{w=0.75}{nw}"
        extend 3fchsm " Ehehe."

    elif persistent._jn_player_pet == "frogs":
        n 3unmaj "¡Ooh!{w=0.2} ¡Ranitas!{w=0.75}{nw}"
        extend 3fchbg " ¡Qué lindas!"
        n 4fllss "En serio no me canso de sus caras.{w=0.75}{nw}"
        extend 3uchgn " ¡Siempre se ven tan {i}confundidas{/i}!{w=0.75}{nw}"
        extend 3nchgn " Ahaha."
        n 1ulrss "Bueno,{w=0.2} como sea...{w=1}{nw}"
        extend 4tnmss " Supongo que no debería hacerte esperar,{w=0.2} [player]."
        n 4fsqss "Ya sabes."
        n 6fcsbg "...¡Solo por si acaso tienes que {i}saltar{/i} a la acción y cuidar de los tuyos!"

        if Natsuki.isLove(higher=True):
            n 3fchsmleme "Ehehe.{w=0.75}{nw}"
            extend 3fchbll " ¡Te amo,{w=0.2} [player]~!"
        else:

            n 3fchsmeme "Ehehe."

    elif persistent._jn_player_pet == "geckos":
        n 1unmbg "¡Geckos!{w=0.75}{nw}"
        extend 4fchbg " ¡Sí!{w=0.75}{nw}"
        extend 4fchsm " ¡He oído sobre esos!"
        n 1flrss "Hombre...{w=1}{nw}"
        extend 3fchgn " ¡Simplemente no puedo superar lo tontos que se ven!{w=0.75}{nw}"
        extend 3cslbosbr " Incluso si tienes que alimentarlos con bichos."
        n 1ccstr "Pero solo una advertencia,{w=0.2} [player]..."
        n 2csqpo "Mejor no escucho sobre ninguna cola cayéndose en tu guardia."

    elif persistent._jn_player_pet == "gerbils":
        n 3ulraj "Gerbos,{w=0.5}{nw}"
        extend 3tnmbo " ¿eh?"
        n 4fsqaj "...¿Y por qué eso,{w=0.2} [player]?{w=0.75}{nw}"
        extend 2fnmfl " ¿Los hámsteres no son suficientemente buenos para ti?{w=0.75}{nw}"
        extend 2fnmaj " ¿Es eso?"
        n 2fsqpo "..."
        n 2fcssm "Ehehe.{w=0.75}{nw}"
        extend 4ulrss " Nah,{w=0.2} supongo que lo entiendo.{w=0.75}{nw}"
        extend 7tnmbo " Mantienes a los gerbos juntos,{w=0.2} ¿verdad?{w=0.75}{nw}"
        extend 3fchsm " ¡Lindo!"
        n 3fcsaj "Aunque mejor cuida bien de los tuyos,{w=0.2} [player]..."
        n 4fsqss "...O realmente {i}sí{/i} necesitarás que te desentierren del problema.{w=0.75}{nw}"
        extend 4fcssm " Ehehe."

        if Natsuki.isLove(higher=True):
            n 2fchsmleaf "Love you,{w=0.2} [player]~!"

    elif persistent._jn_player_pet == "guinea_pigs":
        n 4uwdaj "¡Ooh!{w=0.75}{nw}"
        extend 3uchbg " ¡Sí!{w=0.2} ¡He visto esos!"
        n 3clrbgsbl "No sé exactamente {i}montones{/i} sobre ellos,{w=0.5}{nw}"
        extend 3fchgn " ¡pero me encantan los soniditos que hacen!{w=0.75}"
        extend 4fchbg " ¡Especialmente cuando tienes un montón de ellos juntos!"
        n 2fcssm "Apuesto a que los tuyos son un montón de parlanchines también,{w=0.2} ¿eh?{w=0.75}{nw}"
        extend 2fchsm " Ehehe."

    elif persistent._jn_player_pet == "hamsters":
        n 1fcsaj "E-{w=0.2}espera.{w=0.75}{nw}"
        extend 4unmfl " ¿Hámsteres?{w=0.75}{nw}"
        extend 4fnmfl " ¿En serio?"
        n 2fcsun "..."
        n 2fcsem "Me...{w=1}{nw}"
        extend 1fcsaj " estás...{w=1}{nw}"
        extend 4fspgs " ¡¿JODIENDO?!{w=0.75}{nw}"
        extend 4uchbs " ¡Me {b}encantan{/b} los hámsteres!"
        n 3fcsbgl "Esas colitas rechonchas,{w=0.5}{nw}"
        extend 3flrbgl " esas patitas diminutas...{w=1}{nw}"
        extend 3fchgnl " ¿esas mejillas regordetas?"
        n 1fcssml "Ehehe.{w=0.75}{nw}"
        extend 4fcsbs " ¡Sip!{w=0.75}{nw}"
        extend 4fllbg " Cuando se trata de una demostración {i}profesional{/i} de ternura,{w=0.5}{nw}"
        extend 3fcsbg " me temo que tengo que decirlo."
        n 3nchgn "¡Simplemente no puedes ganarle a los hámsteres!"
        n 3nllsssbr "Aunque...{w=1}{nw}"
        extend 3nslss " dicho eso."
        n 1csqtr "Mejor cuida {i}muy{/i} bien los tuyos,{w=0.2} [player]..."

        if Natsuki.isAffectionate(higher=True):
            n 4nsrpo "...O realmente descubrirás cúanto me saco de mis casillas y {i}hago un drama{/i}.{w=0.75}{nw}"
            extend 4fsqsm " Ehehe."

            if Natsuki.isLove(higher=True):
                n 4fchsmleaf "¡Te amo también,{w=0.2} [player]~!"
        else:

            n 4fcspo "...O realmente {i}sí{/i} descubrirás cúanto me saco de mis casillas y hago un drama."

    elif persistent._jn_player_pet == "horses":
        n 1unmemesu "H-{w=0.2}huh?{w=0.75}{nw}"
        extend 4unmgssbl " ¿Caballos?{w=0.75}{nw}"
        extend 4tnmflsbl " ¡¿En serio?!"
        n 2clremsbr "Jeez...{w=1}{nw}"
        extend 2csqposbr " no te estás quedando conmigo,{w=0.2} ¿verdad?{w=0.75}{nw}"
        extend 2cllemsbr " ¿Cómo siquiera puedes {i}pagar{/i} algo así,{w=0.2} [player]?"

        if get_topic("talk_careful_spending").shown_count > 0:
            n 4tllsl "..."
            n 7tllpu "...Huh.{w=0.75}{nw}"
            extend 7cslsssbr " Tal vez esa conversación sobre ser cuidadoso con tu dinero {i}sí{/i} era necesaria después de todo."
        else:

            n 5csrsssbr "...Incluso si {i}es{/i} bastante genial."

        n 2csrsssbr "B-{w=0.2}bueno,{w=0.2} como sea.{w=0.75}{nw}"

        if Natsuki.isAffectionate(higher=True):
            extend 2fcsbg " Espero que estés ensillado,{w=0.2} [player]..."
            n 2nchgnelg "¡Porque no hay forma de que te escapes de darme lecciones de equitación gratis!{w=0.75}{nw}"
            extend 2nchgn " Ehehe."
        else:

            extend 4nsqpo " Más te vale que no te atrape cabalgando sin casco,{w=0.2} [player]."
            n 2ccspoesi "Porque que acabes cargando con un montón de estúpidas facturas de hospital es lo último de lo que quiero escuchar."

    elif persistent._jn_player_pet == "insects":
        n 2tsqan "Ack-{w=0.75}{nw}"
        n 2cllunlsbr "..."
        n 2ccssslsbr "B-{w=0.2}bichos,{w=0.5}{nw}"
        extend 4clrsslsbl " ¿huh?"
        n 4csrunlsbl "..."
        n 1ccsajlsbl "D-{w=0.2}digo,{w=0.75}{nw}"
        extend 2cllsssbl " ¡no me malinterpretes!{w=0.75}{nw}"
        extend 2cllbosbl " Alguien tiene que cuidar de todas las cosas rastreras."
        n 5cslemsbl "...Solo me alegra que no sea yo.{w=0.75}{nw}"
        extend 1ccsemsbl " Yeesh."
        n 4csrbosbl "..."
        n 4ccssssbl "B-{w=0.2}bueno..."
        n 2fllbg "¡Supongo que intentaré que no me{w=0.5}{nw}"
        extend 2fsqsm " {i}pique{/i}{w=0.75}{nw}"
        extend 4fwlbg " la curiosidad entonces!{w=0.75}{nw}"
        extend 4fcssmeme " Ehehe."

        if Natsuki.isLove(higher=True):
            n 3fchblleaf "¡Te amo también,{w=0.2} [player]~!"

    elif persistent._jn_player_pet == "lizards":
        n 1tnmfl "¿Oh?{w=0.75}{nw}"
        extend 2tllfl " ¿En serio,{w=0.2} [player]?{w=1.25}{nw}"
        extend 2tsqem " ¿Lagartijas?"
        n 4ccsss "Je.{w=0.75}{nw}"
        extend 7ulraj " Tengo que decir,{w=0.2} [player] -{w=0.5}{nw}"
        extend 7unmbo " estoy impresionada."
        n 6fchbg "...¡{i}Finalmente{/i} lograste encontrar una mascota tan sangre fría como tú!"
        n 1fsqdv "..."
        n 4fchdvesi "¡Pfffft!{w=0.75}{nw}"
        extend 3fchbg " ¡Estoy bromeando,{w=0.2} [player]!{w=0.5} ¡Solo bromeo!{w=0.75}{nw}"
        extend 3kllbg " Jeez..."
        n 3cnmss "..."
        n 1fsqbo "..."
        n 4fnmem "¡Oye!{w=0.75}{nw}"
        extend 4flrfl " Vamos,{w=0.2} [player].{w=0.75}{nw}"
        extend 4fcspo " No me mires así.{w=0.75}{nw}"
        extend 3fchgn " ¡Esa fue buena!"
        n 6fcsbg "Y además -{w=0.5}{nw}"
        extend 6unmaj " ¡piénsalo!"
        n 4fnmsg "¿No deberías tú de entre todas las personas saber cómo{w=0.5}{nw}"
        extend 3fsqbg " {i}desprenderte{/i}{w=0.75}{nw}"
        extend 3fchbg " de las cosas?{w=0.75}{nw}"
        extend 3nchgn " Ahaha."

        if Natsuki.isLove(higher=True):
            n 4fwlbgl "¡Te amo también,{w=0.2} [player]~!"
        else:

            n 4fwlbg "¡Estaré aquí toda la semana,{w=0.2} [player]!"

    elif persistent._jn_player_pet == "mice":
        n 7tlrbo "Ratones,{w=0.2} ¿eh?{w=0.75}{nw}"
        extend 7tsqfl " ¿Estás seguro,{w=0.2} [player]?"
        n 4fsqss "¿No hámsteres?{w=1}{nw}"
        extend 4fnmbg " ¿Gerbos?"
        n 3fsqbg "...¿O me huele a rata?"
        n 3fsqsm "..."
        n 3fchsm "Ehehe.{w=0.75}{nw}"
        extend 4ullss " Nah,{w=0.2} supongo que entiendo el atractivo.{w=0.75}{nw}"
        extend 7unmaj " Son animales sociales,{w=0.2} ¿verdad?"
        n 3fcssmesm "¡Más te vale darle mucha compañía a los tuyos también,{w=0.2} [player]!"

    elif persistent._jn_player_pet == "rats":
        n 7tnmbo "Ratas,{w=0.2} ¿eh?{w=0.75}{nw}"
        extend 7ullaj " Eso es bastante genial."
        n 2ullsl "..."
        n 2fsqsm "..."
        n 2fcsbg "¿Oh?{w=0.75}{nw}"
        extend 4fnmbg " ¿Qué pasa,{w=0.2} [player]?{w=0.75}{nw}"
        extend 4fnmsm " ¿{i}Esperabas{/i} que me diera asco o qué?"
        n 1fcssm "Ehehe.{w=0.75}{nw}"
        extend 3tllss " Nah,{w=0.2} las ratas están bien.{w=1}{nw}"
        extend 3unmaj " ¡Son súper inteligentes también!{w=0.75}{nw}"
        extend 3nlrsssbl " Pero apuesto a que ya sabías eso de todas formas."
        n 1fcsss "Je.{w=0.75}{nw}"
        extend 4fcsbg " De hecho..."
        n 2fsqbg "Apuesto a que probablemente tienes muchas {i}historias{/i} de cola que contar por ahora,{w=0.5}{nw}"
        extend 2nchgn " ¿verdad?"

        if Natsuki.isLove(higher=True):
            n 1nchsml "Ahaha.{w=0.75}{nw}"
            extend 3fchbll " ¡Te amo también,{w=0.2} [player]~!"

    elif persistent._jn_player_pet == "rabbits":
        n 4unmbg "¡Conejitos!{w=0.75}{nw}"
        extend 4uchgnl " ¡Sí!{w=0.75}{nw}"
        extend 3ccsssl " Hombre..."
        n 3cllbolsbr "..."
        n 4ccsfllsbr "D-{w=0.2}digo,{w=0.5}{nw}"
        extend 2fcsajlsbr " ¿cómo podría alguien {i}no{/i} amar esas bolitas de pelusa?{w=0.75}{nw}"
        extend 2fllsslsbr " ¡¿Estás bromeando?!"
        n 4fcsbgl "¡Especialmente los que tienen las orejas caídas!{w=0.75}{nw}"
        extend 4nchgnl " ¡Se ven tan abrazables!"
        n 1fllbg "Y además solo para rematar,{w=0.5}{nw}"
        extend 3fspaj " ¡vienen en todos esos colores diferentes también!{w=0.75}{nw}"
        extend 3fchbg " ¡Hablando de variedad!"
        n 6ullaj "Solo asegúrate de mantener esa jaula impecable,{w=0.2} [player] -{w=0.5}{nw}"
        extend 2csqpo " No voy a soportar ninguna {i}bola de polvo{/i} en mi guardia."

    elif persistent._jn_player_pet == "snakes":
        n 1unmemesh "¿H-{w=0.2}huh?{w=0.75}{nw}"
        extend 4ccsemlsbl " A-{w=0.2}ahora espera un segundo,{w=0.2} [player].{w=0.75}{nw}"
        extend 4clremlsbl " ¿{i}Serpientes{/i}?"
        n 1csrunlsbr "..."
        n 4fcsunsbr "Uuuuuu..."
        n 2kcsaj "...Bien.{w=0.75}{nw}"
        extend 2cslbosbr " Supongo que seré directa contigo,{w=0.2} [player]."
        n 1ccsfllsbr "No soy...{w=1}{nw}"
        extend 4ksrsllsbr " {i}increíble{/i} con esas."
        n 2fcsfllsbr "S-{w=0.2}serpientes,{w=0.2} quiero decir."
        n 2fllfll "Simplemente...{w=1}{nw}"
        extend 2cslcal " no concuerdan conmigo.{w=0.75}{nw}"
        extend 4cslsll " No sé por qué."
        n 6fcsgsl "¡P-{w=0.2}pero eso no quiere decir que no {i}puedan{/i} ser lindas,{w=0.1} obviamente!{w=0.75}{nw}"
        extend 3flrpo " Hacer ese tipo de asunciones es simplemente ser ignorante."
        n 3ksrpo "...Y merecen cuidado como cualquier otra mascota."

        if Natsuki.isAffectionate(higher=True):
            n 1fcsaj "Además,{w=0.2} [player] -{w=0.5}{nw}"
            extend 4ccsca " sabes en lo que te metiste."
            n 3fchgn "¡No puedes {i}deslizarte{/i} de tus responsabilidades tan fácil!{w=0.75}{nw}"
            extend 3nchgn " Ehehe."

            if Natsuki.isLove(higher=True):
                n 3fchbll "¡Te amo también,{w=0.2} [player]~!"
        else:

            n 4flraj "¡Así que!{w=0.75}{nw}"
            extend 3fcsposbr " ¡Más te vale no estarte acobardando con los tuyos,{w=0.2} [player]!"
            n 3fcscaesmsbr "¡Es todo lo que digo!"

    elif persistent._jn_player_pet == "something_else":
        n 4tsqbg "¿Oho?{w=0.75}{nw}"
        extend 3tnmbg " Un dueño exótico,{w=0.2} ¿eh?"
        n 3fcsbg "...¿Y por qué eso,{w=0.2} [player]?{w=0.75}{nw}"
        extend 3fsqss " ¿Las mascotas regulares no son suficientemente {i}especiales{/i} para ti?{w=0.75}{nw}"
        extend 3fupfl " ¿Simplemente tenías que destacar?"
        n 3fsqsm "..."
        n 4fnmsm "¿Y bien?{w=0.75}{nw}"
        extend 2fcsbs " ¡Desembucha!"
        n 2fsqcs "..."
        n 2nchgn "Ahaha.{w=0.75}{nw}"
        extend 2cllss " Nah,{w=0.2} supongo que está bien.{w=0.75}{nw}"
        extend 2tnmaj " Aunque hablando en serio,{w=0.2} [player]?"
        n 2clrca "..."
        n 4ccstr "Solo...{w=1}{nw}"
        extend 4csqsl " asegúrate de saber lo que haces.{w=0.75}{nw}"
        extend 4csqaj " ¿Capiche?"

        if Natsuki.isAffectionate(higher=True):
            n 1unmemlsbl "¡N-{w=0.2}no es que crea que automáticamente eres un mal dueño o algo!{w=0.75}{nw}"
            extend 2fcsemlsbl "\n¡Claro que no!"
            n 2fcspol "Solo un {i}verdadero{/i} tonto salta a ese tipo de conclusiones.{w=1}{nw}"
            extend 4csrbol " Pero..."
            n 3ccsajl "{i}He{/i} oído sobre lo demandantes que pueden ser.{w=0.75}{nw}"
            extend 3csqbo " Y créeme."
            n 4fcssslsbl "Realmente no quieres {i}mis{/i} exigencias encima de eso también.{w=0.75}{nw}"
            extend 4fsqsml " Ehehe."

            if Natsuki.isLove(higher=True):
                n 3fchbll "¡Te amo también,{w=0.2} [player]~!"
            else:

                n 6fwlbgl "¡Disfruta,{w=0.2} [player]!"
        else:

            n 6ccsajlsbr "L-{w=0.2}le debes al animal al menos {i}eso{/i},{w=0.2} después de todo.{w=0.75}{nw}"
            extend 3fcscalesm " Recuerda eso."

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_service_animals",
            unlocked=True,
            prompt="Animales de servicio",
            category=["Animales"],
            nat_says=True,
            affinity_range=(jn_affinity.DISTRESSED, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_service_animals:
    if get_topic("talk_service_animals").shown_count > 0:
        if Natsuki.isNormal(higher=True):
            n 4ncsss "Je.{w=0.75}{nw}"
            extend 3nslss " Hombre..."
            n 7ntlaj "Estoy bastante segura de que ya hablé de eso antes,{w=0.75}{nw}"
            extend 7unmbo " pero todavía no puedo sacarme de la cabeza esa visita escolar que tuvimos."
            n 4fsrsssbl "N-{w=0.2}no la de orientación vocacional ni nada de eso.{w=0.75}{nw}"
            extend 4unmaj " ¡Sino esa visita que tuvimos de la caridad para animales de servicio y terapia!"
            n 3fchbg "Vaya que causaron una impresión,{w=0.2} ¿eh?"
            n 3ulraj "Pero en serio -{w=0.5}{nw}"
            extend 4unmfl " ¡es loco cuánto trabajo hacen!{w=0.75}{nw}"
            extend 4tllfl " Como estaba diciendo antes..."
        else:

            n 1ncssl "Je.{w=0.75}{nw}"
            extend 2nlraj " Estoy bastante segura de que hablé de eso antes -{w=0.5}{nw}"
            extend 2csqsl " si es que estabas {i}escuchando{/i} -{w=0.5}{nw}"
            extend 2clrpu " pero todavía sigo pensando en esa visita escolar que tuvimos."
            n 1fsqfl "...Y no,{w=0.5}{nw}"
            extend 4ccsfl " ninguna de carreras ni nada de eso."
            n 4cdlbo "De hecho estaba pensando en esa caridad con los animales de servicio y terapia.{w=0.75}{nw}"
            extend 2cllaj " Todavía es bastante loco para mí cuánto trabajo realmente hacen."
    else:

        if Natsuki.isNormal(higher=True):
            n 7cdlbo "Sabes,{w=0.2} [player]..."
            n 7tdlaj "No creo haberlo mencionado antes,{w=0.75}{nw}"
            extend 7unmbo " pero de hecho solíamos tener visitantes en la escuela a veces."
            n 3ccsss "Je.{w=0.75}{nw}"
            extend 3csqss " ¿Te sorprende?{w=0.75}{nw}"
            extend 1fdrsl " Éramos {i}básicamente{/i} una audiencia cautiva,{w=0.2} después de todo."
            n 1csrfl "No es como si nos dieran la opción de irnos."
            n 3cllaj "Usualmente era solo alguien intentando vendernos alguna carrera después de la escuela,{w=0.75}{nw}"
            extend 3csrbo " o como una visita de la policía local o algún otro festival del aburrimiento."
            n 7utrpu "Pero...{w=0.75}{nw}"
            extend 7clrbg " hubo {i}una{/i} visita que de hecho sí me gustó."
            n 4fcsbg "Apuesto a que no adivinas cuál fue,{w=0.2} [player]."
            n 3fsqsm "Ehehe."
            n 3ullaj "De hecho fue un grupo de voluntarios de una caridad...{w=1}{nw}"
            extend 4unmfl " ¡pero para animales de servicio y terapia!"
            n 1ccsgs "Y oh.{w=0.5}{nw}"
            extend 1ccsfl " Por.{w=0.5}{nw}"
            extend 1csqaj " Dios.{w=0.5}{nw}"
            extend 4csqca " [player]."
            n 4ccstr "¡Son...{w=1}{nw}"
            extend 4fspgsedz " {b}asombrosos{/b}!{w=0.75}{nw}"
            extend 3uchgn " ¡Los amo!"
        else:

            n 1cllpu "Sabes..."
            n 2fslpu "No es que espere que te importe ni nada,{w=0.75}{nw}"
            extend 2cnmsl " pero de hecho sí teníamos visitantes aleatorios en la escuela a veces."
            n 2clrsl "..."
            n 2ccsfl "Sí.{w=0.75}{nw}"
            extend 4csqsl " No te veas tan sorprendido."
            n 4fllem "Difícil encontrar una mejor audiencia cautiva que un grupo de estudiantes.{w=0.75}{nw}"
            extend 2fslem " Obviamente."
            n 2cslpu "Digo...{w=1}{nw}"
            extend 2clrsl " la mayoría eran solo un {i}total{/i} festival del aburrimiento.{w=0.75}{nw}"
            extend 2clraj " Charlas vocacionales,{w=0.5}{nw}"
            extend 2csrfl " esa clase de cosas."
            n 7csrsl "Pero hubo una que {i}sí{/i} me gustó de hecho."
            n 3cllpu "Era un tipo de caridad,{w=0.5}{nw}"
            extend 3nllaj " pero todo su trabajo era sobre entrenar animales de servicio y terapia -{w=0.5}{nw}"
            extend 3cllca " y luego dárselos a gente que los necesitaba."

    if Natsuki.isNormal(higher=True):
        n 7ulrss "Son como animales entrenados especialmente para ayudar a gente que lucha para hacer ciertas cosas por sí mismos -{w=0.5}{nw}"
        extend 7unmfl " ¡o cosas que no pueden hacer del todo!"
        n 2ccsss "Todos saben sobre los perros guía.{w=0.75}{nw}"
        extend 2unmbo " Pero de hecho hay una {i}tonelada{/i} de roles en los que la gente nunca piensa."
        n 4unmaj "¡En serio!"
        n 4ccsss "Hay unos que se supone que ayudan más con la movilidad,{w=0.5}{nw}"
        extend 3cllsssbr " algunos que escuchan cosas si su dueño tiene mal oído..."
        n 3unmaj "¡Incluso ayudar a manejar condiciones médicas o evitar alergias!"
        n 7ccsss "Je.{w=0.75}{nw}"
        extend 7fcssmesm " Hablando de olfaterar cosas."
        n 7tllaj "Pero...{w=1}{nw}"
        extend 7tnmbo " ¿personalmente?"
        n 4unmbg "¡Los que realmente me gustaron fueron los animales de terapia!"
        n 2clrss "Los visitantes no entraron en tanto detalle sobre ellos,{w=0.5}{nw}"
        extend 4csrss " y no están {i}exactamente{/i} en el mismo grupo que los tipos de servicio..."
        n 4unmbo "Pero son como una especie de mascotas extra-mansas para gente pasando por momentos difíciles de algún tipo."
        n 2ullaj "Ya sabes,{w=0.5}{nw}"
        extend 2unmbo " como emocional o mentalmente."
        n 4nchgn "...¡Y vienen en una tonelada de formas y tamaños también!"
        n 3clrbg "Tienes gatos y perros -{w=0.5}{nw}"
        extend 3fcsbg " {i}obviamente{/i} -{w=0.5}{nw}"
        extend 3fchsm " ¡pero hasta animales como esos caballos miniatura pueden ser entrenados para ayudar!"
        n 6fcsbg "Tampoco los encuentras solo pasando el rato en casa,{w=0.2} [player] -{w=0.5}{nw}"
        extend 6unmbg " ¡dijeron que oficinas,{w=0.2} hospicios e incluso hospitales pueden organizar visitas con ellos también!"

        if Natsuki.isAffectionate(higher=True):
            n 3nchgn "Bastante asombroso,{w=0.2} ¿verdad?{w=0.75}{nw}"
            extend 3clrsm " Ehehe..."
            n 4clrslsbl "..."
            n 5ksrbosbl "..."
            n 1kcsflesi "..."
            n 4kllbo "Solo...{w=1}{nw}"
            extend 4kslbo " apesta a veces,{w=0.2} pensándolo ahora.{w=0.75}{nw}"
            extend 4knmbol " ¿Sabes?"
            n 5cslcal "...C-{w=0.2}con Sayori y todo."
            n 5cslfll "Ella...{w=1}{nw}"
            extend 4cdlbol " no estaba ese día que tuvimos la visita.{w=0.75}{nw}"
            extend 4cslbol " No toma un genio para averiguar por qué."
            n 2ccsfllsbl "Es-{w=0.2}es solo que..."

            if Natsuki.isEnamored(higher=True):
                n 2ksrbolsbl "..."
                n 2ksrfllsbr "No puedo evitar pensar si solo tener uno cerca podría haber {i}hecho{/i} algo por ella.{w=0.75}{nw}"
                extend 5knmbolsbr " Uno de esos animales de apoyo."
                n 4ccsemlsbr "Yo...{w=1}{nw}"
                extend 4ccsfllsbr " sé...{w=1}{nw}"
                extend 4cdlbolsbr " que no pueden obrar milagros.{w=0.75}{nw}"
                extend 2ccssrlsbr " N-{w=0.2}no soy {i}ingenua{/i}."
                n 4kslpulsbr "Pero..."
                n 4kslfllsbr "Hubiera sido algo...{w=1}{nw}"
                extend 5knmbolsbr " ¿no?"
                n 5ksrbolsbr "...Tal vez solo esa única cosa podría haber hecho {i}algún{/i} tipo de diferencia."
                n 7ksrsllsbl "..."
                n 3ccsfllsbl "...C-{w=0.2}como sea."
            else:

                n 4cslunlsbl "..."
                n 4ccsemlsbl "...O-{w=0.2}olvídalo.{w=0.75}{nw}"
                extend 2cllfllsbl " Es..."
                n 2cdlsllsbr "...No es realmente algo en lo que quiera pensar justo ahora."
                n 2nslbolsbr "P-{w=0.2}perdón."
                n 2nslbol "..."
                n 4ccsajl "C-{w=0.2}como sea."
        else:

            n 3nchgn "Bastante asombroso,{w=0.2} ¿verdad?{w=0.75}{nw}"
            extend 3fchsm " Ehehe."
            n 4ulrss "Bueno,{w=0.2} de cualquier forma..."

        n 3ulrbo "No fue una visita súper grande ni nada,{w=0.5}{nw}"
        extend 3csrss " así que los voluntarios no se quedaron {i}tanto{/i} tiempo..."
        n 4uchgn "¡Pero sí nos dejaron subir y conocer a los animales que trajeron con ellos!"
        n 3fcssmesm "Sin sorpresas de quién fue escogida para subir primero.{w=0.75}{nw}"
        extend 3fsqsm " Ehehe."
        n 4fcsbg "¡Sip!"
        n 2ullbg "Cuando se trata de ese tipo de animales,{w=0.2} tiene que decirse.{w=0.75}{nw}"
        extend 6fchbg "\n¡Nada le gana a una experiencia real práctica!"
        n 2fchsm "Ahaha.{w=0.75}{nw}"
        extend 2tllss " Bueno,{w=0.2} como sea."
        n 4ullaj "Creo que ya hablé por demasiado tiempo ya,{w=0.5}{nw}"
        extend 6fcssmesm " ¡pero espero que hayas aprendido algo,{w=0.2} [player]!"
        n 3fsqbg "¿Y si no?"
        n 4fcsss "Je.{w=0.75}{nw}"
        extend 4tllss " Bueno..."
        n 7tsqss "Tú eres un animal también,{w=0.2} ¿no?{w=0.75}{nw}"
        extend 7fcssm " No te preocupes demasiado,{w=0.2} [player]..."
        n 3fchgnelg "¡Bastante segura de que puedo entrenarte a {i}ti{/i} igual de bien!"

        if Natsuki.isLove(higher=True):
            $ chosen_tease = jn_utils.getRandomTease()
            n 3fchbll "¡Te amo también,{w=0.2} [chosen_tease]~!"
        else:

            n 3fwlbg "¡De nada,{w=0.2} [player]!"
    else:

        n 7tllbo "Son como animales especialmente entrenados para ayudar a gente con cosas que no podrían hacer normalmente -{w=0.5}{nw}"
        extend 7cllpu " o del todo."
        n 2csqsl "Sí,{w=0.2} no es broma.{w=0.75}{nw}"
        extend 2clrfl " Todos han oído de perros guía.{w=1}{nw}"
        extend 2fcsca " Pero la gente olvida todas las otras cosas con las que animales entrenados pueden ayudar."
        n 4clltr "Movilidad,{w=0.2} problemas de oído...{w=1}{nw}"
        extend 4cllca " condiciones médicas y alergias también,{w=0.2} de hecho."
        n 2cslaj "Supongo que ese tipo de ayuda animal es genial y todo.{w=0.75}{nw}"
        extend 2cnmsl " Pero lo que realmente me resaltó fueron los animales de terapia y apoyo emocional.{w=0.75}{nw}"
        extend 2csrfl " Incluso si {i}no{/i} tuvieron tanto foco."
        n 7clrfl "Supongo que son como mascotas súper-mansas que la gente tiene para ayudarles a pasar por un momento duro."
        n 2fcssl "Je.{w=0.75}{nw}"
        extend 2fsqfr " ¿Te suena familiar,{w=0.2} {i}[player]{/i}?"
        n 2cllfl "Tienes perros y gatos -{w=0.5}{nw}"
        extend 2cslfl " obviamente -{w=0.5}{nw}"
        extend 4nlraj " pero puedes conseguir caballos miniatura y todo tipo de cosas hoy en día."
        n 1ulrfl "Incluso puedes conseguir visitas arregladas a hospitales y hospicios ahora,{w=0.2} así que..."
        n 2cdrbo "Sí.{w=0.75}{nw}"
        extend 2cdrsl " Eso es todo lo que tenía que decir sobre ello."

        if Natsuki.isUpset(higher=True):
            n 1fcssl "Je.{w=0.75}{nw}"
            extend 1fllpu " Y además."
            n 4fslfl "No es como si escucharas mucho más de lo que digo de todas formas.{w=0.75}{nw}"
            extend 4fsqsl " ¿{i}Cierto{/i}?"
        else:

            n 1fcsem "Je.{w=0.75}{nw}"
            extend 1fsrem " Y además..."
            n 4fslsr "Puedo pensar en al menos {i}un{/i} animal al que le vendría bien algo de entrenamiento extra justo ahora...{w=0.75}{nw}"
            extend 4fsqan " {i}[player].{/i}"

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_using_computers_healthily",
            unlocked=True,
            prompt="Usar computadoras saludablemente",
            conditional="store.jn_utils.get_current_session_length().total_seconds() / 3600 >= 8",
            category=["Salud", "Tecnología"],
            nat_says=True,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_using_computers_healthily:
    if get_topic("talk_using_computers_healthily").shown_count > 0:
        n 3tllsl "..."
        n 7tslbo "..."
        n 7tslfl "Dime...{w=1}{nw}"
        extend 7tnmfl " [player]?{w=0.75}{nw}"
        extend 3unmaj " ¿Tienes un minuto?{w=0.75}{nw}"
        extend 3tnmbo " Tengo que hacerte una pregunta."
        n 7tslsl "..."
        n 7tslaj "Entonces...{w=1}{nw}"
        extend 7unmaj " has estado visitándome por un tiempo ya,{w=0.2} ¿eh?{w=0.75}{nw}"
        extend 3ulrbo " Ya sabes,{w=0.2} usando tu computadora y todo."
        n 4csrss "Y estoy bastante segura de que ya pasé por cómo asegurarte de no estar preparándote para un gran dolor más adelante."
        n 4tlraj "Pero...{w=1}{nw}"
        extend 7tnmaj " tengo que preguntar."
        n 3fnmbg "Solo cuánto de eso exactamente tú{w=0.3}{nw}"
        extend 3fsqbg " {i}realmente{/i}{w=0.3}{nw}"
        extend 3fnmbg " recuerdas,{w=0.75}{nw}"
        extend 3fsqsm " [player]?"
        n 4fnmbg "¿Eh?"
        n 4tsqsm "..."
        n 2fcssm "Ehehe.{w=0.75}{nw}"
        extend 2fcsbg " Sip,{w=0.2} justo como pensé.{w=0.75}{nw}"
        extend 2nchgn " ¡Silencio total!"
        n 4fllbg "Bueno [player],{w=0.2} no temas."
        n 6fcssmedz "¡Porque es hora de un pequeño recordatorio sobre cómo {i}no{/i} arruinar tu espalda de parte de tu servidora!"
    else:

        n 7tslsl "..."
        n 7cslpu "...Huh."
        n 7tnmaj "Sabes,{w=0.2} [player]...{w=1}{nw}"
        extend 3tlraj " Recién pensé en algo.{w=0.75}{nw}"
        extend 3unmbo " Sobre cómo de hecho me visitas y todo."
        n 7ulraj "Así que...{w=1}{nw}"
        extend 2tlrfl " tienes que estar en tu escritorio para hablarme,{w=0.5}{nw}"
        extend 2tnmca " ¿verdad?{w=0.75}{nw}"
        extend 4cslss " O usando algún tipo de computadora al menos."
        n 7tslpu "Y has estado aquí por buen rato ya también,{w=0.2} ahora que lo pienso."

        if Natsuki.isEnamored(higher=True):
            n 3unmfll "N-{w=0.2}no es que diga que no lo aprecio ni nada de eso!\n{w=0.75}{nw}"
            extend 3ccsajlsbr "¡C-{w=0.2}claro que sí lo hago!"
            $ chosen_tease = jn_utils.getRandomTease()
            n 5csrbolsbr "Ni siquiera debería tener que recordártelo por ahora,{w=0.2} [chosen_tease]."

        elif Natsuki.isAffectionate(higher=True):
            n 3unmeml "N-{w=0.2}no es que sea un problema,{w=0.5}{nw}"
            extend 3clremlsbl " ¡ni nada de eso!{w=0.75}{nw}"
            extend 3ccspolsbl " D-{w=0.2}deberías saber que no lo es para ahora de todas formas,{w=0.2} [player]."
        else:

            n 3unmeml "N-{w=0.2}no es que diga que es algún tipo de problema ni nada de eso,\n{w=0.5}{nw}"
            extend 4ccsgslsbl " ¡{i}obviamente{/i}!"
            n 2csrbolsbl "..."

        n 4clrpu "Aunque..."
        n 7tnmflsbr "¿No significa eso que estás pasando un montón de tiempo extra sentado con tu computadora todos los días?{w=0.75}{nw}"
        extend 3tsqslsbr " ¿Solo por mi bien?"

        if (
            Natsuki.isAffectionate(higher=True) 
            and (jn_activity.ACTIVITY_MANAGER.hasPlayerDoneActivity(jn_activity.JNActivities.artwork) 
            or jn_activity.ACTIVITY_MANAGER.hasPlayerDoneActivity(jn_activity.JNActivities.coding) 
            or jn_activity.ACTIVITY_MANAGER.hasPlayerDoneActivity(jn_activity.JNActivities.work_applications))
        ):
            $ activity_options = []
            if jn_activity.ACTIVITY_MANAGER.hasPlayerDoneActivity(jn_activity.JNActivities.artwork):
                $ activity_options.append("dibujando")

            if jn_activity.ACTIVITY_MANAGER.hasPlayerDoneActivity(jn_activity.JNActivities.coding):
                $ activity_options.append("programando")

            if jn_activity.ACTIVITY_MANAGER.hasPlayerDoneActivity(jn_activity.JNActivities.work_applications):
                $ activity_options.append("trabajando")

            if len(activity_options) > 0:
                $ activity_mention = random.choice(activity_options)
                n 2ccsfl "Digo...{w=1}{nw}"
                extend 2ulraj " Sé que ya usas tu computadora para un montón de cosas.\n{w=0.75}{nw}"
                extend 4fchbg "¡Como [activity_mention]!"
        else:

            n 2ccsfl "Digo...{w=1}{nw}"
            extend 2tllsl " Supongo que probablemente todavía usas tu computadora para otras cosas ya."

        n 1ccsflsbl "Pero eso aún no cambia el hecho de que vas a estar acumulando un montón de tiempo de pantalla extra gracias a mí."

        if Natsuki.isEnamored(higher=True):
            n 2clrfllsbl "Y lo último de lo que quiero escuchar es que te estás acalambrando todo porque te encorvaste como un saco de papas por horas."
            n 2cllsl "..."
        else:

            n 2ccsaj "Y lo último de lo que quiero escuchar es que te estás quejando de que tu espalda duele porque nadie tuvo el cerebro para decirte que no te encorves como un saco de papas por horas."
            n 2ccspol "N-{w=0.2}no voy a tener {i}eso{/i} en mi conciencia."

        n 1ccsss "Je.{w=0.75}{nw}"
        extend 4fsrss " De hecho..."
        n 2fnmbg "¿Sabes qué,{w=0.2} [player]?{w=0.75}{nw}"
        extend 2fsqsm " Espero que estés sentado."
        n 6fcsbg "Porque voy a asegurarme de que estés usando tu computadora de la manera {i}correcta{/i},{w=0.5}{nw}"
        extend 3fchgn " ¡te guste o no!"

    n 1fcsbg "Muy bien,{w=0.75}{nw}"
    extend 6fcsaj " así que número uno:{w=1}{nw}"
    extend 3unmbg " ¡postura!"
    n 1ccsflsbl "...Y no,{w=0.2} [player].{w=0.75}{nw}"
    extend 4csqtr " Quiero decir postura {i}real{/i}.{w=0.75}{nw}"
    extend 4ccspo " La de estar sentado."
    n 3fnmfl "Ahora siéntate derecho,{w=0.2} y mantén esa espalda tuya contra la silla,{w=0.2} [player].{w=0.75}{nw}"
    extend 3fcsgs " ¡Lo digo en serio!"
    n 4cllfl "En serio -{w=0.5}{nw}"
    extend 4tsqem " a menos que tengas ganas de hacerte amigo de tu quiropráctico más cercano,{w=0.5}{nw}"
    extend 4cslem " confía en mí cuando digo que {i}realmente{/i} no quieres pasar todo tu tiempo encorvado."
    n 2csqss "...O jorobado en tu silla como algún tipo de extraño gremlin de computadora."
    n 6unmaj "Si lo estás haciendo bien,{w=0.5}{nw}"
    extend 3ullaj " entonces deberías tener tus brazos y muslos paralelos al suelo,{w=0.5}{nw}"
    extend 3fcssm " con tus ojos más o menos al tope de tu pantalla.{w=0.75}{nw}"
    extend 3fcsbg " ¡Pan comido!"
    n 4unmfl "Oh,{w=0.2} cierto -{w=0.5}{nw}"
    extend 2clrsssbl " asegúrate de que tus pies aún puedan tocar el piso,{w=0.2} sin embargo.\n{w=0.75}{nw}"
    extend 2fcscasbr "Incluso {i}yo{/i} puedo hacer eso,{w=0.2} [player]."
    n 1fnmaj "Número dos:{w=0.75}{nw}"
    extend 2fcsbg " ¡distancia!"
    n 2clrbg "Es bastante fácil de olvidar,{w=0.5}{nw}"
    extend 4tnmbo " pero si quieres evitar ojos adoloridos entonces tienes que asegurarte de que estás de hecho a una distancia decente de la pantalla también."
    n 2fcsca "¡No justo enfrente o tan lejos que necesites binoculares!"

    if Natsuki.isEnamored(higher=True):
        n 2fcsbglsbr "S-{w=0.2}sé que simplemente no puedes tener suficiente de mí,{w=0.2} [player].{w=0.75}{nw}"
        extend 4cslfllsbr " Pero en serio."
        n 4ccspol "Incluso yo no quiero verte prácticamente presionando tu cara contra la pantalla tampoco."

    elif Natsuki.isAffectionate(higher=True):
        n 2fsrsslsbr "S-{w=0.2}sé que {i}soy{/i} bastante asombrosa,{w=0.5}{nw}"
        extend 4csqflsbr " pero lo último por lo que quiero ser recibida es tu cara justo contra la pantalla tampoco."
    else:

        n 2ccsflsbr "Y-{w=0.2}y además,{w=0.5}{nw}"
        extend 2cslflsbr " lo último que quiero ver es tu cara toda aplastada contra la pantalla,{w=0.2} [player].{w=0.75}{nw}"
        extend 2ccsposbr " No pedí {i}eso{/i}."

    n 2ulraj "Así que...{w=1}{nw}"
    extend 4tsgbg " solo asegúrate de estar sentado a un brazo de distancia de la pantalla.{w=0.75}{nw}"
    extend 4ccsbg " ¡Eso es todo lo que digo!"
    n 3unmpu "No olvides mantener todas tus cosas al fácil alcance sin embargo -{w=0.5}{nw}"
    extend 3ccsbg " a menos que seas un psíquico,{w=0.5}{nw}"
    extend 6csqsm " no llegarás lejos si apenas puedes golpear el teclado."

    if get_topic("talk_using_computers_healthily").shown_count > 0:
        n 7ullaj "Y recuerda,{w=0.2} hay un montón de cosas para ver más allá de la pantalla -{w=0.5}{nw}"
        extend 3fcsbg " ¡así que mejor dale un descanso a tus ojos también!"
    else:

        n 7ullfl "¿Y mientras estás en eso?{w=0.75}{nw}"
        extend 7ullaj " Pasa algo de tiempo mirando a algo {i}más{/i} que la pantalla también,{w=0.5}{nw}"
        extend 7unmbo " ya que estamos."
        n 3fcsbg "Tienes ventanas ahí,{w=0.2} ¿verdad?{w=0.75}{nw}"
        extend 3fsqbg " ¡Así que mejor úsalas!"

    n 7ccsbg "Ahora,{w=0.2} número tres:{w=0.75}{nw}"
    extend 3fchbg " ¡descansos!"
    n 3tllfl "No sé tú [player],{w=0.5}{nw}"
    extend 7tnmbo " ¿pero personalmente?{w=0.75}{nw}"
    extend 7csrem " No puedo soportar estar sentada mirando a una pantalla por horas de corrido."
    n 3cnmem "En serio -{w=0.5}{nw}"
    extend 4cllan " sigo distrayéndome si estoy atascada en frente de mi laptop por mucho tiempo.{w=1}{nw}"
    extend 4fcsem " ¡Es lo peor!"
    n 2fslem "Además encima de eso,{w=0.5}{nw}"
    extend 2csqsl " {i}realmente{/i} no le estás haciendo un favor a tu circulación tampoco."
    n 6fcsbg "...¡Así que levanta tu trasero y haz algunos estiramientos o algo!{w=0.75}{nw}"
    extend 3clraj " O incluso ve por algo de agua si {i}realmente{/i} necesitas una excusa para moverte."
    n 3tnmbo "Realmente,{w=0.2} no importa lo que hagas.{w=0.75}{nw}"
    extend 4ccsca " Es todo sobre levantar tu trasero,{w=0.2} ponerte de pie,{w=0.2} y darle un descanso a tus ojos.{w=0.75}{nw}"
    extend 6ccsbg " ¡Bastante simple!"
    n 3fsqsm "..."
    n 3fsqss "¿Y bien?{w=0.75}{nw}"
    extend 7fcsbg " ¿Aún me sigues,{w=0.2} [player]?"
    n 3flraj "Más te vale.{w=0.75}{nw}"
    extend 3fnmfl " ¡Esta es fácilmente la más importante,{w=0.2} así que escucha!"
    n 4tllfl "No te hagas la idea equivocada,{w=0.2} [player] -{w=0.5}{nw}"
    extend 4tsqfl " obviamente vas a conocer tus límites mejor que yo."
    n 2tlrpu "Pero...{w=1}{nw}"
    extend 2tnmbo " ¿si empiezas a sentirte algo raro o enfermo,{w=0.2} o tus ojos empiezan a doler o algo mientras estás por aquí?"
    n 2cllaj "Solo..."
    n 1cdlsll "..."
    n 4ccsfllsbl "...Solo no seas un tonto total sobre eso.{w=0.75}{nw}"
    extend 4csqfllsbl " ¿Está bien?"
    n 2clrflsbr "Hablo en serio aquí."
    n 2cnmslsbr "Déjalo por la paz en lo que sea que estuvieras haciendo y solo vuelve a ello después.{w=0.75}{nw}"
    extend 1csqbosbr " ¿Entendido?"
    n 3ccstr "Trabajo o alguna vieja tarea polvorienta puede esperar si solo vas a empeorarte tratando de impresionar a alguien."
    n 3csqbo "No,{w=0.2} tu jefe o profesor no va a caer muerto si ese apestoso reporte no está listo hoy."
    n 1ccsss "Je.{w=0.75}{nw}"
    extend 4clrss " Como sea,{w=0.2} piénsalo."
    n 3tnmbo "No es como si fueras a lograr algún tipo de milagro si tratas de forzarte a través de todo."
    n 3ccsaj "Todo lo que vas a lograr es hacerte sentir como la mierda por aún más tiempo.{w=0.75}{nw}"
    extend 3fcsca " Es totalmente inútil."

    if Natsuki.isEnamored(higher=True):
        n 2cllca "...Y además,{w=0.2} [player]."
        n 2cllpulsbl "Sabes que no voy a enojarme ni nada si tienes que cancelar nuestro tiempo juntos..."
        n 4knmbolsbl "¿Cierto?"
        n 4klrbolsbl "..."
        n 2ccsfllesisbl "..."
        n 2cnmsll "...Mira."
        n 1fcspul "Yo...{w=1}{nw}"

        if Natsuki.isLove(higher=True):
            extend 1ncspul " realmente...{w=1}{nw}"

        $ chosen_descriptor = jn_utils.getRandomEndearment() if Natsuki.isLove(higher=True) else player
        extend 4csrbol " me importas,{w=0.2} [chosen_descriptor].{w=0.75}{nw}"
        extend 5cnmbol " Deberías saber eso en serio para ahora."
        n 3ccsajl "...Justo como deberías saber que {i}no{/i} voy a estar impresionada por alguna extraña demostración de macho de aguantarse."
        n 3cnmpol "¿Capiche?"
        n 3cslbol "..."

    elif Natsuki.isAffectionate(higher=True):
        n 2cllflsbr "Y-{w=0.2}y además,{w=0.2} [player].{w=0.75}{nw}"
        extend 2ccssllsbl " No soy {i}tan{/i} egoísta."
        n 4csrajlsbl "{i}Sí{/i} sabes que no me enojaré ni nada si realmente tienes que irte por un rato..."
        n 4cnmsllsbl "¿Verdad?"
        n 1cslbolsbl "..."
    else:

        n 2fcstr "Y-{w=0.2}y además,{w=0.2} [player]."
        n 2clrajsbl "No es como si fuera a enojarme contigo ni nada de eso tampoco si tienes que irte.{w=0.75}{nw}"
        extend 2clrsll " Incluso yo no soy tanto de ser una imb****."
        n 1clrbol "..."

    n 4ccsflsbr "C-{w=0.2}como sea."
    n 4ullaj "He hablado por demasiado tiempo ya,{w=0.5}{nw}"
    extend 2cnmca " así que solo voy a decir esto,{w=0.2} [player]."
    n 7fcsaj "Podrías terminar con una espalda de mierda u ojos asquerosos si no eres cuidadoso..."
    n 3fcspo "...¡Pero eso no va a ser nada comparado al dolor de oído de grado-A que te llevarás si vienes llorando conmigo después!"
    n 3fsqsm "Ehehe."

    if Natsuki.isLove(higher=True):
        $ chosen_tease = jn_utils.getRandomTease()
        n 4fchbll "¡Te amo también,{w=0.2} [chosen_tease]!"
    else:

        $ chosen_descriptor = jn_utils.getRandomTease() if Natsuki.isEnamored(higher=True) else player
        n 4fchgnedz "¡De nada,{w=0.2} [chosen_descriptor]!"

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_staying_active",
            unlocked=True,
            prompt="Mantenerse activo",
            conditional="persistent.jn_total_visit_count >= 5",
            category=["Vida", "Tú", "Salud"],
            nat_says=True,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_staying_active:
    $ already_discussed_topic = get_topic("talk_staying_active").shown_count > 0
    if already_discussed_topic:
        n 3ccsss "Je.{w=0.75}{nw}"
        extend 7csqss " Pues bien,{w=0.2} [player]."
        n 7fcsbg "Creo que es justo la hora para una pequeña actualización."
        n 3fllss "Sabes..."
        n 4fsqss "Sobre todo ese asunto de{w=0.5}{nw}"
        extend 4fsgbg " {i}'mantenerse activo'{/i}{w=0.5}{nw}"
        extend 4fnmbg " del que hablamos antes?"
        n 2fsqsm "..."
        n 2fsqbg "¿Qué?{w=0.75}{nw}"
        extend 1fcsbs " ¿No recuerdas?{w=0.75}{nw}"
        extend 4fcssmesm " ¿Se te olvidó totalmente o algo {i}ya{/i}?"
        n 3fcsbs "Bueno,{w=0.2} ¡qué mal!"
        n 7flrbg "La última vez que revisé,{w=0.5}{nw}"
        extend 3fsqbg " todavía tenías que estar sentado sobre tu trasero para de hecho pasar algo de tiempo conmigo.{w=0.75}{nw}"
        extend 3cllaj " Así que..."
        n 7csqsm "Por lo que a mí respecta?"
        n 6fcsbg "¡Me reservo {i}totalmente{/i} el derecho de interrogarte sobre ello cuando quiera!"

        if Natsuki.isEnamored(higher=True):
            n 3ccsbgl "Además,{w=0.2} [player].{w=0.75}{nw}"
            extend 4clrsslsbl " Ambos sabemos que {i}alguien{/i} tiene que mantener un ojo en ti.{w=0.75}{nw}"
            $ chosen_tease = jn_utils.getRandomTease().capitalize()
            extend 2ccspol " [chosen_tease]."
            n 4fsqbgl "...Y quién podría ser más adecuada para el trabajo que tu servidora,{w=0.2} ¿verdad?{w=0.75}{nw}"
            extend 4fsqsml " Ehehe."
            n 5ccsajl "B-{w=0.2}bueno,{w=0.2} como sea.{w=0.75}{nw}"

        elif Natsuki.isAffectionate(higher=True):
            n 4ccsajl "¡Y-{w=0.2}y además!"
            n 2ccsbg "Alguien tiene que vigilar y asegurarse de que no estés solo flojeando,{w=0.5}{nw}"
            extend 2csqpo " o tirado como un saco de papa por horas."
            n 5ccsaj "C-{w=0.2}como sea.{w=0.75}{nw}"
        else:

            n 4fsqsm "Ehehe."
            n 4fllbg "Bueno,{w=0.2} lo que sea.{w=0.75}{nw}"

        extend 2tlrfl " Es como dije antes aunque -{w=0.5}{nw}"
        extend 2tnmaj " ¿cuando estaba en la escuela?"
        n 5ccsajsbr "Antes de todo esto,{w=0.2} o-{w=0.2}obviaemnte."
    else:

        n 7tllsl "..."
        n 7cllpu "...Huh."
        n 3ullaj "Sabes,{w=0.2} [player]...{w=1}{nw}"
        extend 3tnmsl " He estado pensando.{w=0.75}{nw}"
        extend 4tlrfl " Sobre cómo me visitas y todo."
        n 4csrss "Y bueno...{w=0.75}{nw}"
        extend 1ccsaj " Perdón,{w=0.2} pero solo {i}tiene{/i} que decirse."
        n 2csqfl "Tú {w=0.2}{i}realmente{/i}{w=0.5} necesitas salir más."
        n 2csqsl "..."
        n 2fsqsm "..."
        n 4fchgnesm "¡Pffft-!"
        n 4fchbg "¡No,{w=0.2} en serio!{w=0.75}{nw}"
        extend 3fsqbg " Solo escúchame,{w=0.2} ¿quieres?{w=0.75}{nw}"
        extend 6fcstr " Estoy siendo seria aquí,{w=0.2} sabes."
        n 1fcsaj "Entonces."
        n 2ulraj "No sé tú,{w=0.2} [player].{w=0.75}{nw}"
        extend 2cnmss " ¿Pero al menos cuando yo estaba en la escuela?"
        n 2ccsflsbr "A-{w=0.2}antes de todo {i}esto{/i},{w=0.2} digo."

    n 4unmbo "Era de hecho {i}súper{/i} fácil conseguir un montón de ejercicio solo por estar atorada en la escuela todo el día todas las semanas."
    n 4unmfl "En serio -{w=0.5}{nw}"
    extend 7tsrpu " Estoy de hecho un poco sorprendida de que nunca lo mencionara antes.{w=0.75}{nw}"
    extend 3unmbo " Pero no es como si estuviéramos {i}siempre{/i} atoradas en este estúpido club ni nada."
    n 3tllbo "Claro,{w=0.2} todos teníamos nuestros propios salones y esas cosas.{w=0.75}{nw}"
    extend 7tnmfl " ¿Pero si teníamos algún tipo de lección especial,{w=0.2} o clase de laboratorio?"
    n 7tnmbo "Entonces solo teníamos que empacar nuestras cosas e ir a cualquier salón que tuviera el equipo."
    n 3csqem "...Y podías garantizar que siempre estaba en algún extremo aleatorio del edificio también.{w=0.75}{nw}"
    extend 4csrem " Qué asco."
    n 4clraj "Así que con todo el constante viaje alrededor de los salones,{w=0.5}{nw}"
    extend 2csgfl " ¿{i}y{/i} la pobre excusa de descanso para almorzar que teníamos?"
    n 2cllfl "Bueno..."
    n 1ccsaj "Solo digamos que {i}definitivamente{/i} ibas a mantenerte en forma de una manera u otra."
    n 1ccsss "Je."
    n 2tsqfl "¿Y si eso no lo estaba haciendo por ti,{w=0.2} [player]?"
    n 4csrem "Entonces podías apostar el dinero de tu almuerzo que todas las lecciones de deportes y gimnasia lo harían.{w=0.75}{nw}"
    extend 4csrsl " Te gustara o no."
    n 1ccsemesi "Ugh."
    n 1unmfl "Digo,{w=0.5}{nw}"
    extend 4cllajsbr " no me malentiendas -{w=0.5}{nw}"
    extend 2ccsposbr " ¡no es como si solo me estuviera quejando por el bien de hacerlo!"
    n 2cslss "Y {i}sí{/i} era bastante genial ser capaz de mantenerse en forma decente sin tirar todo mi tiempo y dinero en el gimnasio..."

    if get_topic("talk_skateboarding").shown_count > 0:
        n 4cllbo "...Especialmente si ya estaba tratando de ahorrar para algo más,{w=0.2} como dije antes.{w=0.75}{nw}"
        extend 4cdlss " Con la patineta y todo."

        if get_topic("talk_work_experience").shown_count > 0:
            n 5cllflsbl "Más todas las cosas de colocación laboral más adelante."

        n 2fcstrlsbr "N-{w=0.2}no que lo hiciera menos dolor en el trasero,{w=0.2} obviamente."
    else:

        n 2cslfl "...Incluso si era un completo dolor en el trasero."

    n 2cllca "..."
    n 2tllpu "Pero...{w=1}{nw}"

    if already_discussed_topic:
        extend 2tsqss " ¿qué hay de ti,{w=0.2} [player]?{w=0.75}{nw}"
        extend 4fcsss " Supongo que tengo que recordarte una vez más,{w=0.2} ¿eh?"
    else:

        extend 4tnmbo " ¿qué hay de ti sin embargo,{w=0.2} [player]?"

    n 7ccsaj "No sé si tomas clases ahora o qué,{w=0.5}{nw}"
    extend 3fcsgs " pero no pienses que solo porque no estás marchando alrededor de una escuela todo el día significa que puedes ser un vago total tampoco."
    n 1fsqsm "Ehehe.{w=0.75}{nw}"
    extend 4fcsbs " ¡Sip!"
    n 2fcsgs "Lo que sea que es -{w=0.5}{nw}"
    extend 2flraj " haciendo mandados,{w=0.5}{nw}"
    extend 2fnmbg " partiéndote el lomo en el gimnasio,{w=0.5}{nw}"
    extend 4fsqbg " ¿o esa caminata de diez minutos que siempre pospones?"
    n 4fcssmesm "¡Todos ganan al tener la sangre bombeando por una vez!{w=0.75}{nw}"
    extend 7fcsbg " Es solo sentido común,{w=0.2} [player]."
    n 6fnmbg "Tómalo de mí:{w=0.5}{nw}"
    extend 6ccsbg " ¡puedes prácticamente {i}garantizar{/i} que te tendrá sintiéndote refrescado y despierto en poco tiempo!"

    if Natsuki.isEnamored(higher=True):
        n 2ulrbg "Y hey,{w=0.2} ¿quién sabe?{w=0.75}{nw}"
        extend 4tsgbg " ¿Si {i}realmente{/i} pones suficiente esfuerzo en ello?"
        n 5ccsbglsbr "E-{w=0.2}entonces tal vez no serás el {i}único{/i} poniéndose en forma.{w=0.75}{nw}"
        extend 5csrdvlsbr " Ehehe."

        if Natsuki.isLove(higher=True):
            $ chosen_endearment = jn_utils.getRandomEndearment()
            n 3fcsbgl "¡T-{w=0.2}te amo también,{w=0.2} [player]~!"
        else:

            n 4ccsbglemesbr "¡M-{w=0.2}mejor salta a ello,{w=0.2} [player]!"
    else:

        n 6csqsm "..."
        n 7tsqss "¿Oh?{w=0.75}{nw}"
        extend 7fsgbg " ¿Qué es eso?"
        n 3fnmbs "¿Qué es con esa repentina mirada de venado encandilado,{w=0.2} [player]?{w=0.75}{nw}"
        extend 3fsqsm " Ehehe."
        n 4fcsbg "Bueno no te preocupes.{w=0.75}{nw}"
        extend 4fsqbg " ¿Con {i}mi{/i} ayuda?"

        if Natsuki.isAffectionate(higher=True):
            n 3fchgn "¡Haremos un profesional de la vida activa de ti en poco tiempo!"
            n 6fchbgedz "¡De nada,{w=0.2} [player]!"
        else:

            n 3fcsbs "¡Tendremos esas piernas tuyas moviéndose por una vez en poco tiempo!"
            n 7fcsbgesm "¡Mejor recuerda agradecerme luego,{w=0.2} [player]!"

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_relieving_stress",
            unlocked=True,
            prompt="Aliviar el estrés",
            category=["Vida", "Tú", "Salud"],
            nat_says=True,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_relieving_stress:
    n 1ullaj "Sabes,{w=0.1} lo admitiré,{w=0.1} [player]."
    n 2flrbgsbl "Yo...{w=0.3} media tengo la mecha corta.{w=0.5}{nw}"
    extend 1klrsssbl " Ehehe."
    n 1fnmss "He estado tratando de trabajar en ello sin embargo,{w=0.3}{nw}"
    extend 1fchbg " ¡y me encantaría compartir algunas de las formas en que lidio con el estrés!"
    n 1unmss "Personalmente,{w=0.1} creo que la mejor manera de lidiar con eso si puedes es tratar de crear algo de distancia."
    n 2nslss "Antes de todo...{w=0.3} esto,{w=0.5}{nw}"
    extend 2nllss " si las cosas se ponían un poco demasiado,{w=0.1} solo salía afuera si podía."
    n 1unmbo "Algo de aire fresco y un cambio de escenario realmente puede poner las cosas en contexto.{w=0.5}{nw}"
    extend 4fwdaj " ¡Es locamente efectivo!"
    n 4ulraj "Pero no solo crees distancia física,{w=0.1} sin embargo.{w=0.5}{nw}"
    extend 1fnmpu " ¡Distánciate mentalmente también!"
    n 3ncssr "Si algo te está estresando,{w=0.1} necesitas quitarle tu atención."
    n 3fslpo "No puedo ir afuera realmente ahora,{w=0.5}{nw}"
    extend 1nllsf " así que solo leo algo,{w=0.1} o veo algunos videos tontos."
    n 1fchbg "Pero haz lo que sea que funcione para ti; {w=0.1}¡todos tenemos nuestras propias zonas de confort!"
    n 2fslpo "Y-{w=0.1}y por supuesto,{w=0.1} siempre podrías venir a verme,{w=0.1} ya sabes..."
    n 1fchbgl "¡C-{w=0.1}como sea!"
    n 1unmpu "El punto es siempre tratar de regresar con una mente limpia,{w=0.3}{nw}"
    extend 1nnmss " y no preocuparse por las cosas pequeñas."
    n 4tnmss "Puedes manejar eso,{w=0.1} ¿verdad [player]?"
    n 1uchsm "¡Seguiré trabajando en ello si tú lo haces!"
    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_careful_spending",
            unlocked=True,
            prompt="Gasto cuidadoso",
            category=["Vida", "Tú", "Salud", "Sociedad"],
            nat_says=True,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_careful_spending:
    n 1tllsr "..."
    n 1fllsr "..."
    n 1tnmpu "¿Mmm...?"
    n 4uwdgsesu "¡O-{w=0.1}oh!{w=0.5}{nw}"
    extend 1flrbg " ¡A-{w=0.1}ajá!{w=0.5}{nw}"
    extend 4fsrdvl " ¡Me distraje!"
    n 1unmaj "Solo estaba pensando..."
    n 1flrbo "Es tan fácil gastar más de lo que quieres hoy en día,{w=0.1} ¿sabes?"
    n 2flrpu "Como...{w=0.3} parece que donde sea que mires,{w=0.1} hay una rebaja,{w=0.1} o tratos,{w=0.1} o algún tipo de oferta especial..."
    n 1unmpu "Y cada lugar acepta todo tipo de formas de pagar,{w=0.1} también.{w=0.5}{nw}"
    extend 3fsrpo " ¡Lo hacen súper conveniente!"
    n 3fnmun "Supongo que a lo que quiero llegar es...{w=0.3} trata de ser cuidadoso con tus hábitos de gasto,{w=0.1} ¿vale?"
    n 1uslss "Trata de no comprar basura que no necesitas{w=0.1} -{w=0.3}{nw}"
    extend 1flrbg " ¡piensa cuánto tiraste la última vez que limpiaste!"
    n 4uwdajl "¡E-{w=0.1}eso no es decir que no deberías darte un gusto,{w=0.1} por supuesto!{w=0.5}{nw}"
    extend 4flrssl " ¡Mereces cosas geniales también!"
    n 1fcsss "El dinero no puede comprar la felicidad...{w=0.5}{nw}"
    extend 1fchgn " pero seguro como el infierno hace encontrarla más fácil.{w=0.5}{nw}"
    extend 1uchbselg " ¡Ahaha!"
    n 4nllss "Bueno,{w=0.1} como sea.{w=0.5}{nw}"
    extend 1tnmsg " Solo trata de pensar un poco antes de gastar,{w=0.1} [player]{w=0.1} -{w=0.3}{nw}"
    extend 1uchbs " ¡eso es todo lo que digo!"

    if Natsuki.isAffectionate(higher=True):
        n 3nslbg "Además..."
        n 1fsqsm "Tenemos que ahorrar todo lo que podamos para cuando podamos pasar el rato,{w=0.1} ¿verdad?{w=0.5}{nw}"
        extend 1uchsm " Ehehe."

        if Natsuki.isLove(higher=True):
            n 4uchbgl "¡Te amo,{w=0.1} [player]~!"

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_eating_well",
            unlocked=True,
            prompt="Comer bien",
            category=["Vida", "Tú", "Salud", "Comida"],
            nat_says=True,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_eating_well:
    n 4unmaj "Oye,{w=0.1} [player]..."
    menu:
        n "¿Has comido hoy?"
        "Sí":

            n 1fnmbg "¡Aja!{w=0.5}{nw}"
            extend 3fsqbg " Pero ¿comiste {i}bien{/i},{w=0.1} [player]?"
        "No":

            n 1knmpu "¿Eh?{w=0.2} ¿Qué?{w=0.5}{nw}"
            extend 2knmem " ¡¿Por qué no?!"
            n 1fnmpu "No te estás saltando comidas,{w=0.1} ¿verdad?"
            n 3flrpo "Más te vale que no,{w=0.1} [player]."

    n 1unmpu "Es súper importante asegurarse de que no solo estás comiendo regularmente,{w=0.3}{nw}"
    extend 1fnmpu " ¡sino comiendo decentemente también!"
    n 1fnmsr "La dieta correcta hace toda la diferencia,{w=0.1} [player]."
    n 4ullaj "Así que...{w=0.5}{nw}"
    extend 1nsgaj " trata y haz un esfuerzo con tus comidas,{w=0.1} ¿entendido?"
    n 1fnmaj "¡Y me refiero a un esfuerzo real!{w=0.5}{nw}"
    extend 1ulrss " Trata de prepararlas desde cero si puedes;{w=0.3}{nw}"
    extend 2fsrss " es a menudo más barato que las comidas instantáneas de todos modos."
    n 1unmss "Recorta cosas como la sal y el azúcar y esas cosas también...{w=0.5}{nw}"
    extend 3nslpo " así como cualquier cosa realmente procesada."
    n 1unmaj "Oh {w=0.1}-{w=0.3}{nw}"
    extend 4fnmaj " y como dije,{w=0.1} ¡ten comidas regularmente también!"
    n 1fchbg "No deberías encontrarte picando basura si tienes comidas apropiadas a lo largo del día."
    n 1usqsm "Tu balance bancario y tu cuerpo te lo agradecerán.{w=0.5}{nw}"
    extend 4nchsm " Ehehe."

    if Natsuki.isAffectionate(higher=True):
        n 1fsqsm "Y además..."
        n 3usqss "Tengo que meterte en buenos hábitos por ti mismo antes de que esté ahí para obligarte."
        n 1fchgnelg "¡Ahaha!{w=0.2} ¡Estoy bromeando,{w=0.1} [player]!{w=0.2} ¡Estoy bromeando!"
        n 4fsqsm "...Mayormente."

        if Natsuki.isLove(higher=True):
            n 4uchsm "¡Te amo, [player]~!{w=0.2} Ehehe."
            return

    n 1fllss "Ahora...{w=0.3} ¿dónde estábamos?"
    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_weather_setup_main",
            unlocked=True,
            prompt="Configurando el clima",
            category=["Configuración", "Clima"],
            nat_says=True,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_weather_setup_main:
    if persistent._jn_weather_api_key:
        $ persistent._jn_weather_setup_started = True

    if persistent._jn_weather_setup_started:

        n 4unmajesu "¡Oh!{w=1}{nw}"
        extend 1fcsbg " ¡Sí,{w=0.1} lo recuerdo!"
        n 1ulraj "Entonces..."
        show natsuki 1unmbg at jn_center

        menu:
            n "¿Desde dónde querías empezar,{w=0.1} [player]?"
            "Quiero darte una clave API":


                n 4unmaj "¿Quieres darme una clave API?{w=1}{nw}"
                extend 1fchbg " ¡Seguro!"
                n 3nchbg "Solo te guiaré a través de ello por si acaso,{w=0.1} ¿okay?"


                $ persistent._jn_weather_api_configured = False
                $ persistent._jn_weather_setting = int(jn_preferences.weather.JNWeatherSettings.disabled)

                jump talk_weather_setup_api_key

            "Quiero darte mi ubicación" if persistent._jn_weather_api_key:

                n 4unmaj "¿Quieres ir a través de tu ubicación?{w=1}{nw}"
                extend 1fchbg " ¡Seguro!"
                n 3nchbg "Solo te guiaré a través de ello por si acaso,{w=0.1} ¿okay?"


                $ persistent._jn_weather_api_configured = False
                $ persistent._jn_weather_setting = int(jn_preferences.weather.JNWeatherSettings.disabled)

                jump talk_weather_setup_location

            "¿Puedes probar todo lo que te dije de nuevo?" if persistent._jn_weather_api_key and persistent._jn_player_latitude_longitude:

                n 4unmaj "¿Solo quieres que pruebe todo de nuevo?{w=0.75}{nw}"
                extend 1fchbgeme " ¡A la orden!"


                $ persistent._jn_weather_api_configured = False
                $ persistent._jn_weather_setting = int(jn_preferences.weather.JNWeatherSettings.disabled)

                jump talk_weather_setup_verify
            "Olvídalo":


                n 1tsqpu "Uh...{w=0.5}{nw}"
                extend 2tsrpu " huh."
                n 1fchbg "Bueno,{w=0.1} ¡tú te lo pierdes,{w=0.3} [player]!"
                extend 4fchsm " Ehehe."

                return
    else:


        n 3fslbo "..."
        n 3fcsem "Urgh...{w=1.5}{nw}"
        extend 4fsrem " ¡tan molesto!"
        n 1fbkwr "¡¿Por qué es esto tan difícil de hacer bien...?!"
        n 2fllpo "Estúpido...{w=0.5}{nw}"
        extend 2fcsan " ¡Nnnnnn-!"

        menu:
            "¿Qué pasa, Natsuki?":
                n 4uwdpueqm "¿Eh?{w=0.5}{nw}"
                extend 4uwdajesu " ¡Oh!{w=0.5} ¡[player]!{w=1}{nw}"
                extend 1fllbgsbr " ¡Me alegra que preguntaras!"
            "¿De qué te quejas?":

                n 1fwdemesh "¡...!{w=0.5}{nw}"
                n 2fcsgs "Bueno,{w=0.1} ¡tu actitud,{w=0.1} para empezar!{w=1}{nw}"
                extend 2fslca " Como sea..."

        n 1ullaj "Así que...{w=0.5}{nw}"
        extend 1flrss " No soy realmente de las que se sientan y admiran la vista."
        n 4nsqbo "Pero en serio,{w=0.1} [player]...{w=1}{nw}"
        extend 2fllpo " ¡es súper aburrido allá afuera!"
        n 2nsqpo "Afuera del salón,{w=0.1} quiero decir.{w=1}{nw}"
        extend 1fbkwr " ¡Nada cambia nunca!"
        n 1ulraj "Pero...{w=1}{nw}"
        extend 1fchbg " He estado haciendo unos pequeños ajustes,{w=0.1} y ¡creo que encontré una forma de hacer las cosas un poco más dinámicas!"
        n 3fslsr "Solo no puedo hacer que todo funcione apropiadamente..."
        n 1fcsem "Es solo...{w=1}{nw}"
        extend 1fcssr " realmente me está molestando.{w=1}{nw}"
        extend 2fslan " ¡Odio cuando no puedo hacer que las cosas salgan bien!"

        menu:
            "¿Tal vez pueda ayudar?":
                n 1uwdpu "¿Eh?{w=0.5}{nw}"
                extend 1unmbg " ¡¿En serio?!{w=0.5}{nw}"
                extend 4nchbs " ¡Gracias,{w=0.1} [player]!"
                n 4fllssl "N-{w=0.3}no es que estuviera {i}esperando{/i} ayuda,{w=0.1} ¡{i}obviamente{/i}!"
            "¿Qué tengo que hacer?":

                n 2fcsem "Cielos,{w=0.1} [player]...{w=0.3}"
                extend 2fsqpo " ¿qué hay con la actitud hoy?"
                n 4kslpo "Estoy {i}tratando{/i} de hacer algo lindo aquí..."

        n 1ullaj "Bueno,{w=0.1} como sea..."
        n 4fslss "Lo que estoy {i}tratando{/i} de hacer es añadir algo de atmósfera a este lugar,{w=1}{nw}"
        extend 1fsqsm " y qué mejor manera de hacer eso que..."
        n 1fchbg "¡Algo de clima real!"
        n 1nsqsl "Y no {i}solo{/i} alguna cosa cambiando aleatoriamente..."
        n 2ulraj "Quiero configurar las cosas para que el clima aquí coincida con como es donde tú estás,{w=0.1} [player]."
        n 1fcsbg "Lo sé{w=0.1} -{w=0.5}{nw}"
        extend 4fwlbg " asombroso,{w=0.1} ¿verdad?"
        n 1ullaj "Pero...{w=1}{nw}"
        extend 4nnmbo " necesito que vayas a este sitio web que encontré."
        n 1kchbg "No te preocupes,{w=0.1} no te haré ir a buscarlo.{w=1}{nw}"
        extend 1kchbgess " ¡No soy {i}tan{/i} mala!"
        n 1unmss "Se llama OpenWeatherMap,{w=0.5}{nw}"
        extend 1uchbg " y es {i}súper{/i} genial!{w=1}{nw}"
        extend 3fcssm " Es justo lo que necesito para hacer que esto funcione."
        n 1fllss "Necesitaré un poco de tiempo para tener todo esto configurado,{w=0.1} sin embargo.{w=1}{nw}"
        extend 4ulraj " Así que..."

        menu:
            n "¿Estás bien si empezamos ahora,{w=0.1} [player]?"
            "Seguro":

                n 1uchbg "¡Muy bien!"
                $ persistent._jn_weather_setup_started = True
                jump talk_weather_setup_api_key
            "No puedo justo ahora":

                n 1nnmbo "Oh.{w=1.5}{nw}"
                extend 4nllsssbl " Bueno..."
                n 1nsldv "Solo déjame saber cuando tengas tiempo,{w=0.1} ¿okay?"
                n 3fcsbg "¡Valdrá {i}súper{/i} la pena!"
                return

label talk_weather_setup_api_key:

    n 1nnmss "¡Okaaay!{w=1}{nw}"
    extend 3fchbg " ¡Empecemos!"
    n 1ullaj "Así que como dije{w=0.1} -{w=0.3}{nw}"
    extend 1unmaj " el sitio web se llama OpenWeatherMap.{w=1}{nw}"
    extend 4nnmsm " ¡Puedes ir ahí desde {a=[store.jn_globals.LINK_OPEN_WEATHER_MAP_HOME]}aquí{/a}!"
    n 1ulraj "Entonces..."

    menu:
        n "¿Tienes el sitio web abierto,{w=0.1} [player]?"
        "Sí, tengo el sitio web abierto":

            n 1nchbs "¡Asombroso!{w=0.5}{nw}"
            extend 4nwlbg " ¡Paso uno completo!"
        "No, no pude ir al sitio web":

            n 4tnmaj "¿Eh?{w=1} ¿Por qué no?{w=1}{nw}"
            extend 1tnmsr " ¿Se cayó o algo?"
            n 2tslaj "Bueno...{w=1}{nw}"
            extend 2tnmss " ¿Tal vez podamos intentar esto de nuevo luego?"
            n 1fllsssbr "¡Solo déjame saber cuando estés listo!"

            jump ch30_loop


    n 1nchbg "¡OKay!{w=0.5}{nw}"
    extend 3fcssm " ¡Ahora el paso dos!"
    n 1nllaj "Básicamente necesito algo llamado clave API,{w=1}{nw}"
    extend 1nnmbo " lo cual me dejará usar ese sitio para averiguar cómo es el clima por allá."
    n 3fslbo "Pero no puedo hacer eso yo misma...{w=1.5}{nw}"
    extend 1fchsm " ¡aquí es donde entras tú,{w=0.1} [player]!"
    n 1nlrss "Necesitarás hacer una cuenta antes de que puedas obtener una clave API."
    extend 1kchbgess " ¡Es totalmente gratis sin embargo!"
    n 1ullaj "Puedes crear una cuenta {a=[store.jn_globals.LINK_OPEN_WEATHER_MAP_SIGN_UP]}aquí{/a},{w=1}{nw}"
    extend 1nnmsm " o puedes iniciar sesión usando el menú en la parte superior."
    n 3fcsaj "Solo asegúrate de ir a través de todas las opciones cuidadosamente{w=0.1} -{w=0.5}{nw}"
    extend 3nsqpo " ¡no solo corras a través de ello!"
    n 1unmaj "Oh{w=0.1} -{w=0.5}{nw}"
    extend 1flrss " y asegúrate de confirmar tu correo electrónico una vez la hayas creado,{w=0.1} ¿okay?"
    n 4nchbg "¡{a=[store.jn_globals.LINK_OPEN_WEATHER_MAP_SIGN_UP]}Aquí está{/a} ese enlace una vez más,{w=0.1} solo por si acaso!"
    n 1fnmsm "Ahora..."

    menu:
        n "¿Conseguiste tener una cuenta,{w=0.1} [player]?"
        "Sí, tengo una cuenta configurada":

            n 1fchsm "¡Asombroso!"
            n 3tllss "Probablemente querrás asegurarte de guardar tus detalles de inicio de sesión en algún lugar seguro,{w=0.5}{nw}"
            extend 4fchsm " sooolo por si acaso."
            n 1fchts "¡No olvides confirmar tu dirección de correo también!"
            n 1fsqsm "Ahora,{w=0.1} aquí viene la parte retadora..."
        "Ya tenía una cuenta configurada":

            n 1fchsm "¡Asombroso!{w=0.5}{nw}"
            extend 3fwlbg " ¡El resto de esto debería ser pan comido!"




    n 1usqsm "¿Estás listo,{w=0.1} [player]?"
    n 1fchsm "¡Necesitas obtener tu clave API y enviármela!"
    n 4ullss "Puedes encontrar tus claves {a=[store.jn_globals.LINK_OPEN_WEATHER_MAP_API_KEYS]}aquí{/a},{w=1}{nw}"
    extend 1unmaj " o puedes ir ahí usando el menú como antes."
    n 3tsqsm "¿Entendiste todo eso?"
    n 3fsqsm "Ehehe.{w=0.5}{nw}"
    extend 4fchbg " ¡Entonces dale,{w=0.1} [player]!"

    $ player_input_valid = False


    while not player_input_valid:

        $ player_input = renpy.input("Introduce tu clave API (o escribe Olvídalo para regresar):")

        if not player_input or player_input == "":
            n 3tsqsm "¿{i}Pensé{/i} que pedí una {i}clave API{/i},{w=0.1} [player]?"
            extend 4fchbl " ¡Intenta de nuevo!"

        elif player_input.replace(" ", "").lower() == "olvídalo" or player_input.replace(" ", "").lower() == "olvidalo":

            n 4tnmaj "¿Eh?{w=0.2} ¿No quieres continuar?"
            n 1tllbo "Está bien,{w=0.1} supongo."
            n 1fcsbg "Solo déjame saber cuando estés listo,{w=0.1} ¿okay?"

            jump ch30_loop
        else:


            $ player_input_valid = True
            $ persistent._jn_weather_api_key = player_input
            n 1uchbg "¡Muy bien!{w=0.2} ¡Lo tengo!"

            jump talk_weather_setup_location

label talk_weather_setup_location:
    n 1fsqbg "Ahora por la pieza final del rompecabezas..."
    n 4uchss "...¡Tu ubicación,{w=0.1} obviamente!"
    n 1ullaj "Hay un par de maneras de hacer esto,{w=1}{nw}"
    extend 1nnmsm " pero pensé que sería mejor solo preguntar."
    n 4ulraj "Así que..."

    menu:
        n "¿Cómo te gustaría decirme, [player]?"
        "¿Puedes intentar localizarme a través del internet?":

            n 1fchsm "Seguro, ¡puedo darle un intento!{w=1}{nw}"
            extend 1fcssm " Solo dame un segundo aquí...{w=1}{nw}"

            $ ip_latitude_longitude = jn_atmosphere.getLatitudeLongitudeByIpAddress()
            if not ip_latitude_longitude:

                n 2fslpu "...Huh."
                n 2knmpo "¡{i}Traté{/i} de buscarte, pero no puede encontrar nada!"
                n 2flrpo "..."
                n 1tlraj "Buneo..."
                extend 1tllbgsbl " parece que vamos a tener que hacer las cosas a la antigua,{w=0.1} [player]."

                jump talk_weather_setup_manual_coords
            else:


                n 4fsgss "¡Ajá!{w=0.5}{nw}"
                extend 1uchbg " ¡Creo que lo tengo!"
                n 3nwlbg "Ahora...{w=0.3} ¿quieres ver algo asombroso, [player]?{w=1}{nw}"
                extend 3fsqsm " Sé que quieres."
                n 1ncsbo "...{w=1}{nw}"

                python:

                    show_map_success = False
                    try:
                        jn_open_google_maps(ip_latitude_longitude[0], ip_latitude_longitude[1])
                        show_map_success = True

                    except Exception as exception:
                        store.jn_utils.log(exception.message, jn_utils.SEVERITY_ERR)

                if show_map_success:
                    n 1fchbg "¡Ta-da!{w=0.5} ¡Te encontré!"
                    n 1fsqsm "..."
                    n 3tsqsm "¿Y bien?{w=1}{nw}"
                    extend 3tsqss " ¿Estoy en lo correcto o qué, [player]?"
                    menu:
                        "Sí, me encontraste":
                            n 4fcsbg "¡Como una pro!"
                            extend 1fcssm " Ehehe."
                            n 1fllss "Solo notaré eso muy rápido..."

                            $ persistent._jn_player_latitude_longitude = ip_latitude_longitude
                            jump talk_weather_setup_verify
                        "No, eso no está bien":

                            n 2fnmgs "¿Qué?{w=0.2} ¡¿Estás bromeando?!"
                            n 2flrsl "Ugh..."
                            n 4nlrpu "Y estaba tan orgullosa de mí misma por averiguar eso,{w=0.1} también..."
                            n 1nnmss "Bueno,{w=0.1} parece que vamos a tener que hacer las cosas a la antigua."

                            jump talk_weather_setup_manual_coords
                else:

                    n 4fnmaj "¿Eh?{w=0.2} ¿Qué car...??"
                    n 1nnmpu "Huh.{w=0.2} Raro."
                    n 1nlrss "Bueno,{w=0.1} {i}iba{/i} a mostrarte algo genial,{w=0.5}{nw}"
                    extend 3nslpo " pero parece que algo salió mal."
                    n 4nlrss "Oye,{w=0.1} [player]...{w=0.3}"
                    extend 1flrbg " ¿podrías buscar estas coordenadas y decirme si lo tengo bien?"
                    n 4tslbo "Estoy {i}bastante{/i} segura de que tu latitud es [ip_latitude_longitude[0]],{w=0.1} y tu longitud es [ip_latitude_longitude[1]]."
                    n 1nllbo "..."
                    n 4tnmss "Bueno,{w=0.3} ¿[player]?"
                    menu:
                        n "¿Cómo nos vemos?"
                        "Sí, eso se ve bien para mí":

                            n 1kchbg "¡Uff!"
                            extend 2nsldv " Estaba medio preocupada de que tendría que ponerme un poco más creativa..."

                            $ persistent._jn_player_latitude_longitude = ip_latitude_longitude
                            jump talk_weather_setup_verify
                        "No, eso no está bien":

                            n 4fcsan "Uuuuuuu..."
                            n 2nslpo "Bien.{w=1}{nw}"
                            extend 2usqpo " Parece que vamos a tener que hacer las cosas a la antigua."

                            jump talk_weather_setup_manual_coords
        "Quiero decirte dónde estoy yo mismo":

            n 1uchgn "¡Bueno, tú eres el jefe!"

            jump talk_weather_setup_manual_coords
        "Olvídalo":

            n 2fllpo "Bueno...{w=1}{nw}"
            extend 4nslpo " bien."
            n 1fchbg "Solo déjame saber cuando quieras pasar por todo esto de nuevo,{w=0.1} ¿okay?"

            jump ch30_loop

label talk_weather_setup_manual_coords:
    n 1ulraj "Entonces,{w=0.3}{nw}"
    extend 1nnmbo " voy a necesitar saber unas cuantas cosas para averiguar dónde estás."
    n 1flrss "Empecemos con lo básico{w=0.1} -{w=0.5}{nw}"
    extend 4fchsm "¡hemisferios!"
    n 1unmaj "¿Vives en el hemisferio {b}norte{/b} o {b}sur{/b}?"
    n 3nllss "Solo en caso de que no supieras,{w=0.1} básicamente solo significa si vives al {b}norte{/b} o {b}Sur{/b} del {b}ecuador{/b}."
    n 1nllaj "Así que..."
    show natsuki 1tsqsm at jn_center
    menu:
        n "¿En cuál vives,{w=0.1} [player]?"
        "El hemisferio norte":

            $ player_in_southern_hemisphere = False
            $ persistent.hemisphere_north_south = "North"

            n 1unmaj "¿El hemisferio norte?{w=1}{nw}"
            extend 1flrbg " ¡Bueno hey!{w=1}{nw}"
            extend 4fchbg " ¡Justo como yo!"
        "El hemisferio sur":

            $ player_in_southern_hemisphere = True
            $ persistent.hemisphere_north_south = "South"

            n 1unmaj "¿El hemisferio sur?{w=1}{nw}"
            extend 4fchbg " ¡Entendido!"

    n 1uchbg "¡Okey,{w=0.1} ahora hora de los otros dos!"
    n 1tnmss "¿Vives en el hemisferio {b}este{/b} u {b}oeste{/b}?"
    n 1ulraj "Esta es un poco más engañosa,{w=0.1} pero encuentro que ayuda pensar en ello de esta manera:"
    n 4nnmbo "Si tomamos un mapa mundial y lo cortamos a la mitad {b}verticalmente{/b} por el medio..."
    show natsuki 1unmaj at jn_center
    menu:
        n "¿Vivirías en la {b}mitad este{/b},{w=0.1} o la {b}mitad oeste{/b}?"
        "La mitad este":

            $ player_in_western_hemisphere = False
            $ persistent._jn_hemisphere_east_west = "East"

            if not player_in_southern_hemisphere:
                n 1unmbg "¡Wow!{w=1}{nw}"
                extend 1fchbg " ¡Justo como yo de nuevo,{w=0.1} [player]!"
                n 2tslss "Realmente es un mundo pequeño,{w=0.1} ¿eh?"
            else:

                n 1fchbg "¡Bueno hey!{w=0.5} ¡Justo como yo!"
        "La mitad oeste":

            $ player_in_western_hemisphere = True
            $ persistent._jn_hemisphere_east_west = "West"

            n 1fchbg "La mitad oeste.{w=0.5} ¡Entendido!"


    n 4fllss "Ahora con eso fuera del camino,{w=0.1} ¡solo necesito tus coordenadas!"
    n 3fsqsm "Y por esas,{w=0.5}{nw}"
    extend 1fchsm " ¡quiero decir tu {b}latitud{/b} y {b}longitud{/b}!"
    n 1ullaj "Siempre usé {a=[store.jn_globals.LINK_LAT_LONG_HOME]}este{/a} sitio web para buscar las mías para la tarea,{w=0.1} pero puedes usar tu teléfono o lo que sea también."
    n 4unmaj "Oh,{w=0.3}{nw}"
    extend 1fnmbo " y no te preocupes por hacerla positiva o negativa.{w=1}{nw}"
    extend 3fcssm " ¡Yo me encargaré de eso!"
    n 1ullss "Empezaremos con tu {b}latitud{/b} primero."
    n 1fchsm "Así que...{w=0.3} ¡dale!"
    $ player_latitude = renpy.input(prompt="Introduce tu {b}latitud{/b}:", allow="0123456789.")


    n 1fchbg "¡Muy bien!{w=0.5}{nw}"
    extend 1nchsm " Ahora finalmente,{w=0.1} ¡solo necesito tu {b}longitud{/b}!"
    n 3fcssm "Justo como la última vez,{w=0.1} puedo averiguarlo sin ningún símbolo positivo o negativo."
    n 1fchsm "¡Dale,{w=0.1} [player]!"
    $ player_longitude = renpy.input("Introduce tu {b}longitud{/b}:", allow="0123456789.")


    python:
        if player_in_southern_hemisphere:
            player_latitude = "-" + player_latitude

        if player_in_western_hemisphere:
            player_longitude = "-" + player_longitude

        player_latitude = float(player_latitude)
        player_longitude = float(player_longitude)

    n 3fcssm "¡OKay!"
    extend 1fchsm " ¡Creo que casi estamos ahí,{w=0.1} [player]!"
    extend 1fcsbg " Déjame abrir un mapa muy rápido...{w=1}{nw}"

    python:

        show_map_success = False
        try:
            jn_open_google_maps(player_latitude, player_longitude)
            show_map_success = True

        except Exception as exception:
            store.jn_utils.log(exception.message, store.jn_utils.SEVERITY_ERR)

    if show_map_success:
        n 1uchgn "¡Ta-da!"
        n 4fnmbg "¿Qué tal eso,{w=0.1} [player]?{w=1}{nw}"

        menu:
            n "Suficientemente cerca,{w=0.1} ¿verdad?"
            "Sí, eso es suficientemente cerca":

                n 1fchbg "¡Finalmente!{w=1}{nw}"
                extend 4nchsm " Solo notaré todo eso muy rápido..."

                $ persistent._jn_player_latitude_longitude = (player_latitude, player_longitude)
                jump talk_weather_setup_verify
            "No, eso no está para nada bien":

                n 1tnmem "¿Qué?{w=0.2} ¡¿En serio?!"
                n 3fcsem "Ugh..."
                n 4fcsaj "Vamos...{w=0.5} a intentar de nuevo,{w=0.1} ¿bien?{w=1}{nw}"
                extend 2fnmpo " ¡Realmente quiero hacer que esto funcione!"

                jump talk_weather_setup_manual_coords
    else:

        n 1fllaj "Urgh...{w=0.3} ¿en serio?{w=0.2} ¡Esto es {i}tal{/i} dolor!"
        n 1nlrsl "No parece que pueda mostrarte donde creo que estás en un mapa,{w=0.1} así que solo preguntaré para asegurarme."
        n 1nnmss "He hecho algunas revisiones para sacar las coordenadas,{w=0.1} y de lo que dijiste..."
        n 4nnmaj "Tu latitud general sería [player_latitude],{w=0.1} y tu longitud general sería [player_longitude]."
        menu:
            n "¿Es [player_latitude], [player_longitude] correcto?"
            "Sí, eso es correcto":

                n 3fcsem "¡Finalmente!{w=1}{nw}"
                extend 3kslpo " Cielos..."

                $ persistent._jn_player_latitude_longitude = (player_latitude, player_longitude)
                jump talk_weather_setup_verify
            "No, eso todavía no está bien":

                n 3tnmem "¿Qué?{w=0.2} ¡¿En serio?!"
                n 3fcsem "Ugh..."
                n 1fcsaj "Vamos...{0.5} a intentar de nuevo,{w=0.1} ¿bien?{w=1}{nw}"
                extend 4fnmpo " ¡Realmente quiero hacer que esto funcione!"

                jump talk_weather_setup_manual_coords
            "Olvídalo":

                n 3fllpo "Cielos...{w=1}{nw}"
                extend 1tlrss " qué lío,{w=0.1} ¿eh?"
                n 1fcspo "..."
                n 1nllaj "Bueno,{w=0.1} gracias de todos modos.{w=1}{nw}"
                extend 1nnmaj " Siempre podemos intentar de nuevo luego,{w=0.5}{nw}"
                extend 4tnmss " ¿verdad?"

                jump ch30_loop

label talk_weather_setup_verify:
    n 1nchbg "¡Okaaay!{w=1}{nw}"
    extend 4fnmsm " ¡Creo que casi terminamos ahora,{w=0.1} [player]!"
    n 1ncsbo "Déjame solo revisar que todo esté en orden aquí...{w=1.5}{nw}"

    if jn_atmosphere.getWeatherFromApi():
        n 1fchbg "¡Sí!"
        extend 1uchbs " ¡Está funcionando,{w=0.5} está funcionando!{w=1}{nw}"
        extend 4nchsml " Ehehe."
        n 1nchbgl "¡Muchas gracias,{w=0.1} [player]!{w=1}{nw}"
        extend 3uchgnledz " ¡Esto va a ser {i}súper{/i} asombroso!"
        $ Natsuki.calculatedAffinityGain()

        python:
            persistent._jn_weather_api_configured = True
            persistent._jn_weather_setting = int(jn_preferences.weather.JNWeatherSettings.real_time)
            jn_atmosphere.updateSky()
    else:

        n 1fcsaj "Oh,{w=0.5}{nw}"
        extend 2fllan " ¡por {i}favor!{/i}"
        n 1fcsem "Ugh..."
        n 3fslem "Y estaba tan entusiasmada sobre ello,{w=0.1} también..."
        n 1fcsem "Lo siento,{w=0.1} [player].{w=1}{nw}"
        extend 4knmemsbl " ¡No puedo hacer que funcione!"
        n 2fsrem "Hablando de una decepción..."
        n 2nsrposbl "..."
        n 1unmgsesu "¡Ah!{w=0.5}{nw}"
        extend 1fnmgs " ¡Recién pensé en algo!"
        n 4tnmpueqm "¿Tuviste que hacer una nueva cuenta para OpenWeatherMap,{w=0.2} [player]?{w=0.75}{nw}"
        extend 4tslbo " O como,{w=0.2} ¿hiciste una nueva clave API?"
        n 1tnmss "Yo...{w=1}{nw}"
        extend 4fsrdvsbr " medio me distraje un poco cuando me dijiste antes.{w=0.75}{nw}"
        extend 1nlrajsbr " Así que..."
        show natsuki 2tnmslsbr at jn_center

        menu:
            n "¿Recuerdas?{w=0.3} Como,{w=0.2} ¿del todo?"
            "Creé una nueva cuenta":

                $ new_account_or_key = True
            "Creé una nueva clave API":

                $ new_account_or_key = True
            "Ya tenía una cuenta, y usé una clave API existente":

                $ new_account_or_key = False
                n 2tslpusbr "...Huh."
                n 1tslsr "Estoy...{w=0.75}{nw}"
                extend 1kcsemesisbl " medio perpleja entonces,{w=0.2} de hecho."
                n 3tsrsl "Digo..."
                n 4tnmpueqm "¿Tal vez solo me diste la clave incorrecta...?"
                extend 1fchbgsbl " ¿O tu internet no lo siente hoy?"
                n 1nslsssbl "No lo sé."
                n 1fllsssbl "Solo...{w=0.5}{nw}"
                extend 4knmsssbr " déjame saber si quieres intentar de nuevo,{w=0.2} ¿okay?"
                n 1knmcaesssbr "¡Será asombroso!{w=0.5}{nw}"
                extend 2knmpolesssbr " ¡L-{w=0.3}lo prometo!"

        if new_account_or_key:
            n 1tslbo "Así que lo hiciste,{w=0.2} ¿eh...?"
            n 4fslpuesp "..."
            n 1unmgsesu "¡Oh!{w=0.5}{nw}"
            extend 1fsrdvsbl " ¡Cierto!"
            n 2fsrsssbl "Olvidé decir..."
            n 2fsldvsbr "Podría tomar un día o algo así para que tu clave API se {i}active{/i} de hecho para que pueda usarla..."
            n 1kchsssbr "Ehehe.{w=0.5}{nw}"
            extend 1fchblsbl " ¡Ups!"
            n 1fllsssbl "Solo...{w=0.5}{nw}"
            extend 4knmsssbr " déjame saber cuando quieras intentar de nuevo,{w=0.2} ¿okay?"
            n 4fnmcasbr "¡Realmente quiero hacer que todo esto funcione!"
            n 1fcstr "Porque cuando lo haga,{w=0.2} puedes apostar que va a ser{w=0.3}{nw}"
            extend 4fspgsledz " ¡{i}asombroso{/i}!"

    jump ch30_loop


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_favourite_season",
            unlocked=True,
            prompt="¿Cuál es tu estación favorita?",
            category=["Clima", "Naturaleza"],
            player_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )
label talk_favourite_season:
    n 1unmbo "¿Huh?{w=0.2} My favorite season?"


    if not persistent.jn_player_favourite_season:
        n 4tllss "Eso es un poco repentino,{w=0.1} ¿no crees?"
        n 1tnmss "Bueno...{w=0.3} como sea.{w=0.3}{nw}"
        extend 4fnmaw " ¡Qué pregunta difícil, [player]!"
        n 3fsrsl "Creo que si tuviera que elegir..."
        n 1fchts "¡Sería el verano!{w=0.2} ¡Obvio!"
        n 3fsqss "¿Por qué?{w=0.5}{nw}"
        extend 1fchgn " ¡Solo piénsalo,{w=0.1} [player]!"
        n 4ullbg "Largos viajes a la playa...{w=0.5}{nw}"
        extend 4ncssm " helado en la sombra...{w=0.5}{nw}"
        extend 4ksrss " paseos tranquilos al atardecer hacia las tiendas..."
        n 1flleml "Q-{w=0.1}Quiero decir,{w=0.3}{nw}"
        extend 1fllbgl " ¿qué podría no gustarme?"
        n 1fchbg "¡Simplemente puedo disfrutar la vida allá afuera sin tener que preocuparme por el clima!"
        n 1usqsg "No creo que tenga que explicarlo más,{w=0.1} ¿verdad?{w=0.5}{nw}"
        extend 4uchsm " Jajaja."
        n 1unmaj "Aunque... {w=0.3}¿qué hay de ti, {w=0.1}[player]?"
        menu:
            n "¿Cuál es tu estación favorita?"
            "Primavera":

                n 1fnmss "¿Oh?{w=0.2} Primavera,{w=0.1} ¿eh?"
                n 3tllsr "Mmm..."
                n 1unmss "Digo,{w=0.1} medio lo entiendo.{w=0.2} Es la señal de que el invierno por fin se largó,{w=0.1} ¿no?"
                n 1ulrss "Y supongo que ver las flores brotar de nuevo es algo lindo."
                n 3fsqan "¡Pero la lluvia!{w=0.2} ¡Por Dios!{w=0.5}{nw}"
                extend 1fcspu " ¡Simplemente nunca para!"
                n 3fllpo "Que llegue ya el verano,{w=0.1} digo yo."

                $ persistent.jn_player_favourite_season = "Spring"
            "Verano":

                n 1fsgbg "¡Aha!{w=0.2} ¡Lo sabía!"
                n 4fsqbg "Nadie puede resistirse a un poco de diversión bajo el sol, {w=0.1}¿no es cierto?"
                n 1fnmbg "Me alegra que ambos estemos de acuerdo, {w=0.1}[player].{w=0.5}{nw}"
                extend 3fchsm "¡Jejeje!"

                $ persistent.jn_player_favourite_season = "Summer"
            "Otoño":

                n 1unmaj "¿Otoño? {w=0.5}{nw}"
                extend 4nllaj "¡No es mala elección, {w=0.1}de hecho!"
                n 1ullsm "Me gusta cuando todavía hace suficiente calor durante el día para salir y hacer cosas..."
                n 4ucsss "Pero también tienes ese aire fresco de la mañana que te despierta."
                n 1ullaj "Las hojas al caer también son súper lindas."
                n 2fcsan "Es solo que...{w=0.5}{nw}"
                extend 4fsrsr " todo se arruina cuando llega la lluvia,{w=0.1} ¿sabes?"
                n 2fsqsr "Caminar entre todas esas hojas pastosas es simplemente asqueroso. {w=0.5}{nw}"
                extend 1fcssf "¡No, gracias!"

                $ persistent.jn_player_favourite_season = "Autumn"
            "Invierno":

                n 1tnmsf "¿Eh?{w=0.2} ¿En serio?"
                n 1tnmaj "¡El invierno es lo último que esperaba que dijeras,{w=0.1} [player]!"
                n 4tlrbo "Aunque...{w=0.3} lo entiendo, un poco."
                n 1fcsbg "¡Es la época perfecta del año para acurrucarse y pasar un buen rato leyendo!"
                n 2fslss "Especialmente porque no hay mucho que puedas hacer afuera,{w=0.1} de todas formas."

                $ persistent.jn_player_favourite_season = "Winter"
    else:


        n 1tllbo "Espera... {w=0.5}{nw}"
        extend 4tnmss "¿no habíamos hablado de esto antes, {w=0.1}[player]?"
        n 1nlrpu "Bueno,{w=0.1} como sea..."
        n 1ucsbg "Todavía amo el verano,{w=0.1} como sabes{w=0.1} -{w=0.3}{nw}"
        extend 3fcsbg " ¡y nada va a cambiar eso pronto!"
        n 4tsqsg "¿Qué hay de ti,{w=0.1} [player]?"
        menu:
            n "¿Sigues firme con el [persistent.jn_player_favourite_season]?"
            "Sí":
                n 1fcsbg "Ehehe.{w=0.2} Eso pensé,{w=0.1} [player]."

                if persistent.jn_player_favourite_season == "Summer":
                    n 1uchbg "¡Ya escogiste la mejor estación,{w=0.1} después de todo!"
                else:

                    n 4fllss "Bueno...{w=0.3} ¡me temo que no vas a persuadirme!{w=0.5}{nw}"
                    extend 1uchbg " ¡Ahaha!"
            "No":

                n 3tsgbg "¿Oh?{w=0.2} Cambiamos de opinión,{w=0.1} ¿eh?"
                n 3tsqss "¿Y bien?{w=0.5}{nw}"
                extend 1fchbg "¡Dime entonces,{w=0.1} [player]!"
                menu:
                    n "¿Cuál es tu estación favorita?"
                    "Primavera":

                        $ new_favourite_season = "Spring"
                    "Verano":

                        $ new_favourite_season = "Summer"
                    "Otoño":

                        $ new_favourite_season = "Autumn"
                    "Invierno":

                        $ new_favourite_season = "Winter"

                $ season_preference_changed = False
                if persistent.jn_player_favourite_season == new_favourite_season:
                    n 1fnmgs "¡Oye!{w=0.2} ¡[player]!"
                    n 3fsqpo "¿Creí que dijiste que habías cambiado de opinión?"
                    n 3fllem "¡No has cambiado de opinión para nada!{w=0.2} ¡Dijiste [persistent.jn_player_favourite_season] la última vez,{w=0.1} también!"
                    $ chosen_tease = jn_utils.getRandomTease()
                    n 1fcsem "Cielos...{w=0.5}{nw}"
                    extend 2fnmpo " ¡eres tan bromista a veces,{w=0.1} [chosen_tease]!"

                    if Natsuki.isAffectionate(higher=True):
                        n 2flrpol "N-{w=0.1}no es que me {i}desagrade{/i} ese lado tuyo,{w=0.1} o-{w=0.1}o algo así."
                    else:

                        n 1fsqsm "Pero...{w=0.3} creo que puedo {i}capear{/i} el temporal."
                        n 4fsrss "Por ahora."
                else:

                    $ persistent.jn_player_favourite_season = new_favourite_season
                    $ season_preference_changed = True

                if season_preference_changed and persistent.jn_player_favourite_season == "Spring":
                    n 1usqss "¿Ooh?{w=0.2} ¿Favoreciendo la Primavera ahora,{w=0.1} [player]?"
                    n 1nlrbo "Podría vivir sin tanta lluvia,{w=0.1} pero lo entiendo."
                    n 3flrpu "Hmm...{w=0.3} Primavera..."
                    n 1tlrbo "Me pregunto...{w=0.5}{nw}"
                    extend 4tnmss " ¿cultivas algo,{w=0.1} [player]?"
                    n 1fchsm "Ahaha."

                elif season_preference_changed and persistent.jn_player_favourite_season == "Summer":
                    n 1fchbs "¡Ajá!{w=0.2} ¿Ves?"
                    n 4fsqbs "Sabías que yo tenía razón todo el tiempo,{w=0.1} ¿no?"
                    n 3usqsg "Ni siquiera intentes negarlo,{w=0.1} [player].{w=0.5}{nw}"
                    extend 1fchbg " ¡El Verano es lo mejor!"
                    n 1uchsm "Solo me alegra que hayas entrado en razón.{w=0.2} ¡Esa es la cosa importante!"

                elif season_preference_changed and persistent.jn_player_favourite_season == "Autumn":
                    n 4usqsm "¿Oh?{w=0.2} Has {i}caído{/i} por el Otoño,{w=0.1} ¿eh?"
                    n 1fchsm "Ehehe."
                    n 1ullss "Admitiré,{w=0.1} es una estación linda,{w=0.1} con todas las hojas doradas y esas cosas..."
                    n 2nslss "Siempre y cuando el clima se mantenga cálido,{w=0.1} de todos modos."

                elif season_preference_changed and persistent.jn_player_favourite_season == "Winter":
                    n 1tllss "Invierno,{w=0.1} ¿eh?{w=0.2} No estaba esperando eso."
                    n 3tnmbo "¿Prefieres estar adentro ahora o algo así,{w=0.1} [player]?"
                    n 4flrss "Bueno,{w=0.1} si prefieres estar todo acogedor adentro..."
                    n 1fsqsm "¡Entonces más te vale no estar flojeando con tu lectura,{w=0.1} [player]!{w=0.5}{nw}"
                    extend 1fchsm " Ehehe."




    python:
        spring_sweater = jn_outfits.getWearable("jn_clothes_bee_off_shoulder_sweater")
        summer_sweater = jn_outfits.getWearable("jn_clothes_creamsicle_off_shoulder_sweater")
        autumn_sweater = jn_outfits.getWearable("jn_clothes_autumn_off_shoulder_sweater")
        winter_sweater = jn_outfits.getWearable("jn_clothes_nightbloom_off_shoulder_sweater")

    if (
        (
            not spring_sweater.unlocked
            or not summer_sweater.unlocked
            or not autumn_sweater.unlocked
            or not winter_sweater.unlocked
        )
        and Natsuki.isHappy(higher=True)
        and persistent.jn_custom_outfits_unlocked
    ):
        n 1flrpu "..."
        n 1ulraj "De hecho,{w=0.3}{nw}"
        extend 3fnmss " ¿sabes qué?"
        n 1fcsss "Dame un segundito.{w=0.75}{nw}"
        extend 3uchgnl " ¡Tengo {i}justo{/i} la cosa!{w=1}{nw}"

        show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
        $ jnPause(1)
        play audio zipper
        $ jnPause(2)

        python:
            import copy

            spring_sweater.unlock()
            summer_sweater.unlock()
            autumn_sweater.unlock()
            winter_sweater.unlock()
            temporary_outfit = copy.copy(jn_outfits.getOutfit(Natsuki.getOutfitName()))

            if persistent.jn_player_favourite_season == "Spring":
                temporary_outfit.clothes = spring_sweater

            elif persistent.jn_player_favourite_season == "Summer":
                temporary_outfit.clothes = summer_sweater

            elif persistent.jn_player_favourite_season == "Autumn":
                temporary_outfit.clothes = autumn_sweater

            else:
                temporary_outfit.clothes = winter_sweater

            jn_outfits.saveTemporaryOutfit(temporary_outfit)

        play audio clothing_ruffle
        $ jnPause(2)
        play audio zipper
        $ jnPause(1)
        show natsuki 1fsqsm at jn_center
        hide black with Dissolve(1.25)

        n 1fsqsm "..."
        n 1tsqssl "...¿Y bien,{w=0.2} [player]?{w=1}{nw}"
        extend 1tcsssl " Tienes que admitir..."
        n 3fsqss "¿Cualquiera sea tu preferencia?"
        n 4fcsbgedz "Mi moda {i}siempre{/i} está en temporada."
        n 1fchsml "Ehehe."

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_time_management",
            unlocked=True,
            prompt="Gestión del tiempo",
            category=["Vida"],
            nat_says=True,
            affinity_range=(jn_affinity.AFFECTIONATE, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_time_management:
    n 1ullaj "Oye,{w=0.1} [player]..."
    n 1unmaj "¿Tienes días malos a veces?{w=0.2} ¿Donde te cuesta trabajo terminar algo?"
    n 3flrpo "¿O solo te distraes súper fácilmente?"
    n 4unmbo "¿Para ser honesta?{nw}"
    extend 3fllss "{w=0.2} Yo batallé con eso por un tiempo.{nw}"
    extend 3fbkwr "{w=0.2} ¡Especialmente cuando cosas como las tareas son tan aburridas!"
    n 1nllaj "Pero...{w=0.5}{nw}"
    extend 1fllbg " averigué una manera de gestionar eso{w=0.1} -{w=0.1} ¡y tú deberías saberlo también,{w=0.1} [player]!"
    n 1fchbg "¡Bloques de tiempo!"
    n 3nsqpo "Y no,{w=0.1} no es tan literal como suena."
    n 1nnmaj "La idea es que apartas un periodo durante el día que quieras trabajar{w=0.1} -{w=0.1} como el día escolar,{w=0.1} o unas cuantas horas en la tarde."
    n 4fnmbg "Luego por cada hora en ese periodo,{w=0.1} ¡la divides!"
    n 1ulraj "Así que por cualquier hora dada,{w=0.1} pasas la mayoría trabajando,{w=0.1} y el resto en algo como una pausa."
    n 1unmss "La idea es que se vuelve mucho más fácil mantenerse enfocado y motivado ya que siempre tienes un respiro por venir."
    n 1uchsm "Personalmente,{w=0.1} encuentro que una división 50/10 funciona mejor para mí."
    n 2nllbo "Así que paso 50 minutos de cada hora estudiando,{w=0.3}{nw}"
    extend 1uchsm " y 10 minutos haciendo lo que quiera."
    n 4usqbg "¡Te sorprenderías de cuánto tiempo de manga puedo meter ahí!"
    n 1unmaj "Aunque no tomes mi horario como una regla.{w=0.5}{nw}"
    extend 1fchbg " ¡Encuentra un balance que funcione para ti, [player]!"
    n 3fslbg "Aunque te debería recordar...{w=0.3} la palabra clave aquí es {i}balance{/i}."
    n 1fsqsr "No voy a estar impresionada si trabajas demasiado...{w=0.5}{nw}"
    extend 4fnmpo " ¡O solo echas la flojera!"
    if Natsuki.isAffectionate(higher=True):
        n 1ullbo "Aunque...{w=0.3} ahora que lo pienso..."
        n 3tsqsm "Tal vez debería hacer bloques de tiempo con nuestro tiempo juntos,{w=0.1} [player]."
        extend 1uchbselg " ¡Ahaha!"

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_sweet_tooth",
            unlocked=True,
            prompt="¿Te gusta lo dulce?",
            category=["Salud", "Comida"],
            player_says=True,
            affinity_range=(jn_affinity.DISTRESSED, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_sweet_tooth:
    n 4unmbo "¿Eh?{w=0.2} ¿Que si me gusta lo dulce?"


    if Natsuki.isAffectionate(higher=True):
        n 3fspbg "¡Puedes apostar que sí!"
        n 4nsqts "¿Qué más esperabas,{w=0.1} [player]?"
        extend 1fchsm "{w=0.2} Ehehe."

    elif Natsuki.isNormal(higher=True):
        n 3fllss "Bueno,{w=0.1} sí.{w=0.2} ¡Por supuesto que sí!"
    else:

        n 1nnmsl "Bueno...{w=0.3} sí.{w=0.2} ¿Por qué no?"

    n 1nllaj "Las cosas horneadas están bien,{w=0.1} pero encuentro que se vuelven medio empalagosas en poco tiempo."
    n 1ullaj "Pero para ser completamente honesta,{w=0.1} ¿si tuviera opción?{w=0.5}{nw}"
    extend 2unmbo " Solo dame un montón de dulces cada vez."

    if Natsuki.isNormal(higher=True):
        n 1uwdaj "¡Hay tanta más variedad!{w=0.2} Como...{w=0.3} ¡siempre hay algo para lo que sea que tenga ganas!"
        n 2tllss "Aunque creo que si tuviera que escoger un favorito,{w=0.3}{nw}"
        extend 1fllss " serían esos ácidos."
        n 1fchbg "Solo esa mezcla perfecta de dulce y agrio,{w=0.1} ¿sabes?"
        n 3flraj "Cielos...{w=0.5}{nw}"
        extend 1fchts " ¡Puedo sentir mi lengua hormigueando ya solo de pensar en ellos!"
        n 1fsrts "..."
        n 3flleml "¡C-{w=0.1}como sea!"
        n 1fcseml "Aunque no es como si estuviera comiendo golosinas todo el tiempo."
        n 2fllpo "Tengo cosas mucho mejores en qué gastar mi dinero."
        n 1fnmss "Y...{w=0.3} no es exactamente saludable tampoco.{w=0.5}{nw}"
        extend 1fchsm " Ahaha."


    if Natsuki.isAffectionate(higher=True):
        n 1fsqsm "Aunque tengo que decir,{w=0.1} [player]."
        n 1fsqssl "Estoy bastante segura de que a ti también te gusta lo dulce."
        n 2fsrbgl "Explicaría por qué estás pasando tanto tiempo conmigo,{w=0.1} d-{w=0.1}después de todo."
        n 1fchbgl "¡Ahaha!"

    elif Natsuki.isNormal(higher=True):
        n 1fllbg "Podría ir por unos dulces justo ahora,{w=0.1} de hecho.{w=0.5}{nw}"
        extend 1fslss " Pero...{w=0.3} creo que me aguantaré."
        n 4usqbg "Alguien tiene que ser un modelo a seguir para ti,{w=0.1} [player].{w=0.2} ¿Tengo razón?"
        n 1fchsm "Ehehe."
    else:

        n 1nnmbo "..."
        n 1nlrbo "Habiendo dicho eso..."
        n 2flrsr "Yo...{w=0.3} realmente podría usar algo de chocolate justo ahora."
        n 2fsqsr "Dejaré que {i}tú{/i} averigües por qué,{w=0.1} [player]."

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_player_appearance",
            unlocked=True,
            prompt="Mi apariencia",
            category=["Tú"],
            player_says=True,
            affinity_range=(jn_affinity.ENAMORED, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_player_appearance:

    if persistent.jn_player_appearance_declined_share:
        n 4unmaj "¿Eh?{w=0.2} ¿Tu apariencia?"
        n 1ullaj "Si mal no recuerdo,{w=0.1} [player]{w=0.1} -{w=0.3}{nw}"
        extend 2tnmbo " dijiste que no querías compartirla conmigo antes."
        n 1tlrbo "Huh. Bueno..."
        menu:
            n "¿Cambiaste de opinión,{w=0.1} [player]?"
            "Sí, quiero compartir mi apariencia":

                n 3fcsbg "¡A-{w=0.1}aha!{w=0.2} Sabía que entrarías en razón eventualmente,{w=0.1} [player].{nw}"
                extend 3fchgn "{w=0.2} ¡No perdamos tiempo!"
            "No, todavía no quiero compartir mi apariencia":

                n 1nllsl "Oh..."
                n 4unmaj "Bueno,{w=0.1} es tu decisión,{w=0.1} [player]."
                n 1unmss "Solo déjame saber si cambias de opinión de nuevo,{w=0.1} ¿está bien?"
                return


    elif persistent.jn_player_appearance_eye_colour is not None:
        n 1unmaj "¿Eh?{w=0.2} ¿Tu apariencia?"
        n 2tllbo "Pero...{w=0.3} estaba segura de que ya compartiste eso conmigo,{w=0.1} [player]."
        n 4uspgs "¡Ooh!{w=0.5}{nw}"
        extend 1unmbg " ¿Te teñiste el cabello o algo?"
        n 2fllbg "O...{w=0.3} ¿tal vez cometiste un error la última vez?"
        n 2tslbg "Bueno...{w=0.5}{nw}"
        extend 1unmbg " como sea."
        menu:
            n "¿Querías compartir tu apariencia de nuevo,{w=0.1} [player]?"
            "Sí, mi apariencia ha cambiado":

                n 1fcssm "¡Aha!{w=0.2} ¡Eso pensé!"
                n 2fchgn "¡No puedo esperar a averiguar cómo!"
            "No, mi apariencia no ha cambiado":

                n 1tnmsr "H-{w=0.1}huh?{w=0.2} ¿Solo tomándome el pelo,{w=0.1} verdad?"
                n 2tsrsf "Okaaay..."
                n 1tnmss "Solo déjame saber si de hecho {i}sí{/i} cambias algo entonces,{w=0.2} ¿okay?"
                return
    else:


        n 1tlrbo "Huh..."
        n 1tnmbo "Sabes,{w=0.1} [player].{w=0.2} Recién me di cuenta de algo."
        n 4unmaj "Has visto mucho de mí,{w=0.1} ¿verdad?{w=0.5}{nw}"
        extend 2fslssl " P-{w=0.1}por pasar tiempo conmigo aquí,{w=0.1} quiero decir."
        n 1ullaj "Así que...{w=0.3} medio sabes exactamente con quién estás tratando."
        n 4uwdgs "¡Pero yo no tengo ni idea de con quién estoy tratando {i}yo{/i}!"
        n 3fsqsm "¿Y honestamente?{w=0.2} Deberías conocerme para ahora.{w=0.5}{nw}"
        extend 3fsqbg " ¡De hecho estoy bastante curiosa!"
        n 1nchbg "¡No te preocupes sin embargo{w=0.1} -{w=0.1} cualquier cosa que me digas se queda estrictamente entre nosotros,{w=0.1} obviamente!"
        n 1fllsfl "N-{w=0.1}no como si a alguien más le importara {i}tanto{/i},{w=0.1} de todos modos."
        n 4unmsm "Así que...{w=0.3} ¿qué tal,{w=0.1} [player]?"
        menu:
            n "¿Quieres compartir tu apariencia conmigo, [player]?"
            "¡Seguro!":

                n 1uchbsl "¡Sí!{w=0.5}{nw}"
                extend 2fcsbgl " Q-{w=0.1}quiero decir ¡bien!{w=0.5}{nw}"
                n 1fchbg "Empecemos entonces,{w=0.1} ¿deberíamos?"
            "No me siento cómodo compartiendo eso":

                n 1unmsl "Oh..."
                n 1ullaj "Eso es un poco decepcionante de escuchar,{w=0.1} si estoy siendo honesta."
                n 2nchss "Pero lo entiendo totalmente,{w=0.1} [player].{w=0.2} Así que no te preocupes,{w=0.1} ¿okay?"
                n 2fsqss "¡Más te vale dejarme saber si tienes ganas de decirme luego sin embargo!"
                $ persistent.jn_player_appearance_declined_share = True
                return

    n 1uchgn "¡Okaaay!{w=0.2} Empecemos con...{w=0.5}{nw}"
    extend 1fchbg " ¡tus ojos!"
    n 4unmbg "Dicen que los ojos son la ventana al alma,{w=0.1} así que solo hace sentido empezar ahí,{w=0.1} ¿verdad?"
    n 4flldvl "..."
    n 1fcseml "¡C-{w=0.1}como sea...!"


    menu:
        n "¿Cómo describirías tu color de ojos,{w=0.1} [player]?"
        "Ámbar":

            n 4unmaj "¡Ooh!{w=0.2} No creo haber visto a alguien con ojos ámbar antes."
            n 1fchbg "¡Eso es asombroso,{w=0.1} [player]!{w=0.2} Apuesto a que esos te ayudan a resaltar,{w=0.1} ¿verdad?"
            $ persistent.jn_player_appearance_eye_colour = "Amber"
        "Azul":

            n 4unmbg "Ojos azules,{w=0.1} ¿eh?{w=0.2} ¡Genial!"
            n 1fsgsm "¡Realmente me gusta cuan llamativos son!"
            $ persistent.jn_player_appearance_eye_colour = "Blue"
        "Café":

            n 4unmaj "Ojos cafés,{w=0.1} ¿eh?{w=0.5}{nw}"
            extend 1fchsm " ¡No me estoy quejando!"
            n 3tsqss "Lindos y naturales,{w=0.1} ¿tengo razón?{w=0.5}{nw}"
            extend 1uchsm " Ahaha."
            $ persistent.jn_player_appearance_eye_colour = "Brown"
        "Gris":

            n 4unmaj "¿Oh?{w=0.2} ¿Ojos grises?{w=0.2} ¡Súper genial, [player]!"
            n 1tllss "¡No creo haber visto a nadie con ojos grises antes!"
            $ persistent.jn_player_appearance_eye_colour = "Grey"
        "Verde":

            n 4fsgbg "¡Aha!{w=0.2} Te tenía figurado con ojos verdes,{w=0.1} [player]."
            n 1fsqbg "Apuesto a que estás orgulloso de ellos,{w=0.1} ¿no?{w=0.5}{nw}"
            extend 1uchsm " Ehehe."
            $ persistent.jn_player_appearance_eye_colour = "Green"
        "Avellana":

            n 4unmaj "¡Ooh!{w=0.2} Avellana,{w=0.1} ¿eh?{w=0.5}{nw}"
            extend 1fsqbg " ¡Con clase!"
            n 1tslsm "Hmm...{w=0.3} Me pregunto si los tuyos son más cercanos al verde o al café,{w=0.1} [player]?"
            $ persistent.jn_player_appearance_eye_colour = "Hazel"
        "Mixto":

            n 4unmaj "¡Wow!{w=0.2} ¿Tienes dos colores diferentes o algo así,{w=0.1} [player]?"
            n 1fchbg "¡Ahora si eso no es único,{w=0.1} no sé qué es!"
            $ persistent.jn_player_appearance_eye_colour = "Mixed"
        "Otro":

            n 4unmaj "¿Oh?{w=0.2} Algo un poco fuera de lo común,{w=0.1} ¿eh?"
            n 1tlrss "...¿O tal vez solo usas lentes de contacto mucho?{w=0.5}{nw}"
            extend 1unmsg " Bueno,{w=0.1} como sea."
            n 1ncsss "Estoy segura de que se ven bien de cualquier forma."
            $ persistent.jn_player_appearance_eye_colour = "Other"

    n 1uchbg "¡Muy bien!{w=0.2} ¡Ese es uno menos!"
    n 3ullaj "Así que siguiente,{w=0.1} tenemos...{w=0.5}{nw}"
    extend 1fchsm " ¡tu cabello,{w=0.1} por supuesto!"
    n 1nnmsm "Solo empezaremos con el largo por ahora."
    n 4ullss "Ahora..."


    menu:
        n "¿Cómo describirías el largo de tu cabello,{w=0.1} [player]?"
        "Corto":

            n 4ncsss "Ah,{w=0.1} el enfoque de bajo mantenimiento{w=0.1} -{w=0.1} ya veo,{w=0.1} ya veo.{w=0.5}{nw}"
            extend 1fchbg " ¡De moda!"
            n 1unmaj "Para ser honesta sin embargo,{w=0.1} lo entiendo totalmente."
            n 3fslpo "No tengo idea de cómo siquiera mantienes el cabello largo viéndose bien..."
            n 3nslpo "Solo parece como demasiado esfuerzo para mí."
            $ persistent.jn_player_appearance_hair_length = "Short"
        "Largo medio":

            n 4fcsbg "¡Ajá!{w=0.2} El balance perfecto,{w=0.1} ¿estoy en lo cierto?"
            n 1fllss "Solo lo suficientemente largo para prácticamente cualquier estilo..."
            n 1fchgn "¡Y aun así suficientemente corto para ajustarse a un día flojo!{w=0.5}{nw}"
            extend 1nchsm " Ehehe."
            n 3flrbgl "¡Me alegra que pensemos de la misma manera,{w=0.1} [player]!"
            $ persistent.jn_player_appearance_hair_length = "Mid-length"
        "Largo":

            n 4unmbg "¡Ooh!{w=0.2} Dejándolo correr libremente,{w=0.1} ¿estamos?"
            n 1fcssm "Apuesto a que cuidas súper bien del tuyo."
            n 3fsqsm "Podría incluso tener que pedir prestados tus productos,{w=0.1} [player].{w=0.5}{nw}"
            extend 1nchsm " ¡Ehehe!"
            $ persistent.jn_player_appearance_hair_length = "Long"
        "No tengo cabello":

            n 4fnmaj "Oye{w=0.1} -{w=0.1} ¡no hay nada malo con eso!{nw}"
            extend 1fsqbg "{w=0.2} ¿Quieres saber por qué?"
            n 3fchgn "Porque solo significa que eres aerodinámico,{w=0.1} [player].{w=0.5}{nw}"
            extend 3uchsmelg " ¡Ahaha!"
            $ persistent.jn_player_appearance_hair_length = "None"

    n 1uchbs "¡Okay!{w=0.5}{nw}"
    extend 1unmbg " Realmente estoy empezando a tener una imagen ahora."
    n 4fwdgs "¡Tenemos que mantener la bola rodando,{w=0.1} [player]!"


    if persistent.jn_player_appearance_hair_length == "None":
        n 1fllss "Dijiste que no tenías cabello,{w=0.1} ¿verdad?{w=0.5}{nw}"
        extend 4fllbg " Así que pienso que es medio inútil hablar sobre el color de cabello."
        n 3fslbo "Ahora,{w=0.1} veamos...{w=0.3} qué más..."
    else:

        n 1fchsm "¡Ahora por tu color de cabello!"
        n 4unmbg "Entonces,{w=0.1} [player]..."
        menu:
            n "¿Cómo describirías tu color de cabello?"
            "Castaño rojizo":

                n 4unmaw "¡Ooh!{w=0.2} Castaño rojizo,{w=0.1} ¿eh?{w=0.5}{nw}"
                extend 1fwdaw " ¡Eso es asombroso,{w=0.1} [player]!"
                n 1fchbg "¡Es un color tan cálido!"
                $ persistent.jn_player_appearance_hair_colour = "Auburn"
            "Negro":

                n 4tsgsm "Negro,{w=0.1} ¿eh?{w=0.5}{nw}"
                extend 1nchgn " ¡Lindo!"
                n 1usqsg "Apuesto a que te sientes súper hábil,{w=0.1} ¿eh [player]?"
                $ persistent.jn_player_appearance_hair_colour = "Black"
            "Rubio":

                n 4fnmbg "¡Ajá!{w=0.2} Un rubio,{w=0.1} ¿lo somos?{w=0.5}{nw}"
                extend 3fsqts " {w=0.3}...Eso explica mucho."
                n 1fchgnelg "¡Ahaha!"
                n 1uchbs "¡Estoy bromeando,{w=0.1} [player]!{w=0.2} ¡Solo estoy bromeando!"
                n 3fllbg "De hecho estoy un poco celosa.{w=0.5}{nw}"
                extend 4fsqsm " Solo un poco."
                $ persistent.jn_player_appearance_hair_colour = "Blond"
            "Castaño":

                n 4unmaj "¿Cabello castaño,{w=0.1} [player]?{w=0.5}{nw}"
                extend 1nchsm " ¡Estoy a favor!"
                n 4nsgss "No muy sutil y no muy llamativo,{w=0.1} ¿sabes?{w=0.2} ¡Es justo!"
                $ persistent.jn_player_appearance_hair_colour = "Brown"
            "Gris":

                n 4unmaj "Ooh...{w=0.5}{nw}"
                extend 1ullaj " Tengo que decir...{w=0.5}{nw}"
                extend 1kllbg " ¡No estaba esperando eso!"
                n 2fsqsr "Solo espero que eso no sea por estrés,{w=0.1} [player]..."
                n 2fllbg "...O al menos estrés por mí,{w=0.1} de todos modos.{w=0.5}{nw}"
                extend 1fchsm " Ehehe."
                $ persistent.jn_player_appearance_hair_colour = "Grey"
            "Rojo":

                n 4fchsm "Ehehe.{w=0.5}{nw}"
                extend 1usqsm " Así que eres pelirrojo,{w=0.1} [player]?"
                n 3flrajl "No que haya nada malo con eso,{w=0.1} ¡o-{w=0.1}obviamente!"
                n 1fchbg "Apuesto a que eso te da algo de atención,{w=0.1} ¿eh?"
                n 3fsrpo "Mas te vale ser del tipo bueno,{w=0.1} sin embargo."
                $ persistent.jn_player_appearance_hair_colour = "Red"
            "Blanco":

                n 4unmbg "Cabello blanco,{w=0.1} ¿eh?{w=0.5}{nw}"
                extend 1uchsm " ¡Genial!"
                $ persistent.jn_player_appearance_hair_colour = "White"
            "Otro":

                n 4unmaj "¿Oh?{w=0.5}{nw}"
                extend 1fsqsm " Parece que somos más similares en gustos de lo que pensé!"
                n 4fsrss "Aunque probablemente debería clarificar...{w=0.5}{nw}"
                extend 1uchgn " el mío es todo natural,{w=0.1} [player]!{w=0.2} Ahaha."
                $ persistent.jn_player_appearance_hair_colour = "Other"


    n 1unmbg "¡Muy bien!{w=0.2} Creo que casi termino de interrogarte ahora,{w=0.1} [player]."
    n 4fsqsm "Ehehe."
    n 1flrsl "Así que...{w=0.3} no te burles de mí cuando pregunte esto,{w=0.1} pero tengo que saber."
    n 1ulrbo "Exactamente..."

    $ player_input_valid = False
    while not player_input_valid:
        $ player_input = int(renpy.input(prompt="¿Qué tan alto eres en {i}centímetros{/i},{w=0.2} [player]?", allow="0123456789"))


        if player_input > 75 and player_input <= 300:
            $ player_input_valid = True
            $ persistent.jn_player_appearance_height_cm = player_input

            if player_input < 149:
                n 4unmgs "H-{w=0.1}huh?{w=0.2} ¿En serio?"
                n 1unmaj "¿Eres incluso más bajo que yo?"
                n 3flldv "Bueno,{w=0.1} ¡no estaba esperando eso!"
                n 1fnmbg "No te preocupes,{w=0.1} [player].{w=0.2} Ambos estamos en el mismo bando,{w=0.1} ¿verdad?{w=0.5}{nw}"
                extend 1fchbg " Ehehe."

            elif player_input == 149:
                n 4unmgs "¿En serio?{w=0.2} ¿Somos de la misma altura?"
                n 1uchbg "¡Eso es asombroso,{w=0.1} [player]!"

                if persistent.jn_player_appearance_hair_length == "Medium" and persistent.jn_player_appearance_hair_colour == "Other":
                    n 2fllbg "Con el cabello y todo lo demás también..."
                    n 1uchgn "¡Es como si fuéramos prácticamente gemelos!"

            elif player_input > 149 and player_input < 166:
                n 4unmaj "¿Oh?{w=0.2} ¿Un poco en el lado bajo,{w=0.1} [player]?"
                n 1fcsss "¡No te preocupes, no te preocupes!{w=0.5}{nw}"
                extend 2fllpo " Y-{w=0.1}yo no soy una para juzgar,{w=0.1} después de todo."

            elif player_input >= 166 and player_input < 200:
                n 4unmaj "¿Sobre la altura promedio,{w=0.1} [player]?"
                n 1nchsm "¡Sin quejas de mi parte!"

            elif player_input >= 200 and player_input < 250:
                n 4unmaj "¿Oh?{w=0.2} ¿En el lado alto [player],{w=0.1} lo estamos?"
                n 1fllbg "Supongo que ya sé a quién llevar de compras,{w=0.1} ¿verdad?{w=0.5}{nw}"
                extend 1nchsm " Ehehe."
            else:

                n 4unmgs "W-{w=0.1}woah!{w=0.2} ¿Qué diablos,{w=0.1} [player]?{w=0.2} ¿En serio?"
                n 1fbkwr "¡Eso es locamente alto!"
                n 3tlrem "Aunque...{w=0.3} de hecho...{w=0.5}{nw}"
                extend 3knmpo " Espero que eso no sea de hecho inconveniente para ti,{w=0.1} sin embargo."
        else:

            n 3fllpo "[player]...{w=0.3} por favor.{w=0.2} Toma esto en serio,{w=0.1} ¿está bien?"

    n 1uchsm "¡Okaaay!{w=0.2} Creo que eso es todo."
    n 1unmbg "¡Muchas gracias,{w=0.1} [player]!"
    n 4fllbg "Sé que no fue mucho,{w=0.3}{nw}"
    extend 1uchgn " ¡pero siento que te conozco mucho mejor ahora!"

    if Natsuki.isLove(higher=True):
        n 4flldvl "Sabes,{w=0.1} [player]?{w=0.2} Solo puedo imaginarlo ahora."
        n 1fnmssl "Conociéndote en persona en algún lugar allá afuera,{w=0.1} por la primera vez..."
        python:

            if persistent.jn_player_appearance_eye_colour == "Other":
                eye_colour_descriptor = "calm"

            else:
                eye_colour_descriptor = persistent.jn_player_appearance_eye_colour.lower()


            if persistent.jn_player_appearance_hair_colour == "Other":
                hair_colour_descriptor = "shiny"

            else:
                hair_colour_descriptor = persistent.jn_player_appearance_hair_colour.lower()


        if persistent.jn_player_appearance_hair_length != "None":
            $ hair_length_descriptor = persistent.jn_player_appearance_hair_length.lower()
            n 4fsqsml "Viendo tu cabello [hair_colour_descriptor] [hair_length_descriptor] en la distancia y cazándote..."
        else:

            n 4fsqsml "Viéndote en la distancia y cazándote..."


        if persistent.jn_player_appearance_height_cm < 149:
            n 2fllssl "Mirando hacia abajo en tus ojos [eye_colour_descriptor]..."

        elif persistent.jn_player_appearance_height_cm == 149:
            n 2fllssl "Mirando directamente en tus ojos [eye_colour_descriptor]..."

        elif persistent.jn_player_appearance_height_cm > 149:
            n 2fllssl "Mirando hacia arriba en tus ojos [eye_colour_descriptor]..."

        n 1fchunl "Uuuuuu..."
        n 1fsqunl "...{w=0.5}{nw}"
        extend 2fllajl " ¡E-ejem!{w=0.2} Como sea..."
        $ chosen_endearment = jn_utils.getRandomEndearment()
        n 1kllsml "En serio.{w=0.2} Gracias,{w=0.1} [chosen_endearment]."
        n 1kcsbgl "Esto seriamente significó mucho para mí."

    elif Natsuki.isEnamored():
        n 4fsldvl "...Y ahora sé exactamente a quién debería estar buscando."
        n 4fsqssl "Así que más te vale tener cuidado,{w=0.1} [player]."
        n 1fcsbgl "Ehehe."

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_drinking_alcohol",
            unlocked=True,
            prompt="¿Bebes alcohol?",
            category=["Comida", "Salud"],
            player_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_drinking_alcohol:
    n 1tnmss "¿Que si bebo alcohol?"
    extend 1tllss " Bueno...{w=0.3} no puedo decir que lo haya probado alguna vez."
    n 2nllsr "Solo no pienso que sea algo para mí."
    n 1ullpu "Habiendo dicho eso,{w=0.1} conocí gente que {i}sí{/i} bebía..."
    n 1kcspu "Pero...{w=0.3} realmente...{w=0.3} preferiría no entrar en eso,{w=0.1} [player]."
    n 1ncssr "Lo siento."
    n 2tlrpu "..."
    n 4uwdajesu "¡Oh!{w=0.5}{nw}"
    extend 4fllss " ¡Eso me recuerda,{w=0.1} de hecho!"
    n 1fnmbg "Apuesto a que no sabías,{w=0.1} pero ¿adivina quién aleatoriamente trajo un poco al club un día?"
    n 1fchgn "¡...Yuri!"
    n 4tnmbg "¿Sorprendido?{w=0.5}{nw}"
    extend 1fcsss " Lo sé,{w=0.1} ¿verdad?"
    n 3tllss "Digo...{w=0.3} ¡fue completamente de la nada!"
    n 1uchbs "Ella solo lo sacó de su bolso como si fuera un libro o algo así."
    n 4unmbo "Ni siquiera eran cosas de supermercado cualquiera tampoco...{w=0.5}{nw}"
    extend 1uwdaj " ¡se veía súper caro también!"
    n 3kllss "Honestamente,{w=0.1} no pude evitarlo.{w=0.2} Solo estallé en risa."
    n 1ullun "Creo que fue solo lo casual que ella estaba siendo sobre todo eso,{w=0.1} realmente."
    n 4nnmsl "Monika no se veía impresionada,{w=0.1} sin embargo..."
    n 1klrsl "Y Sayori...{w=0.3} ella solo se puso realmente molesta.{w=0.5}{nw}"
    extend 2klrpu " ¡Estaba gritando y todo!"
    n 1kcspu "Parecía que Yuri puso mucho pensamiento en escoger algo,{w=0.1} pero solo le dieron un mal rato por eso..."
    n 1kcssr "Digo...{w=0.5}{nw}"
    extend 1kllsr " Sé que no debimos haberlo tenido ahí para nada,{w=0.1} y Yuri debió haber sabido mejor."
    n 2fslsr "Pero ella no merecía todo...{w=0.5}{nw}"
    extend 2kslsr " eso."
    n 1kslaj "Creo que ella solo estaba tratando de ser linda,{w=0.1} ¿sabes?"
    n 4unmsr "Está todo en el pasado ahora,{w=0.1} obviamente.{w=0.5}{nw}"
    extend 2kslsr " Pero...{w=0.3} eso no significa que no me siga sintiendo mal por eso a veces."
    n 1kcssr "..."

    if Natsuki.isAffectionate(higher=True):
        n 1kllsr "Oye...{w=0.5}{nw}"
        extend 4knmpu " ¿[player]?"
        n 1klrsr "¿Puedes prometerme algo?"
        n 2fcssr "Es tonto,{w=0.1} pero no me importa."
        n 1nnmsl "Realmente no me importa si bebés o no."
        n 2klrpu "Pero...{w=0.3} ¿si lo haces?"
        n 4ksqsr "Por favor solo tómalo todo con moderación,{w=0.1} ¿está bien?"
        n 2kllsr "H-...{w=0.5}{nw}"
        extend 2fcsan " visto...{w=0.5}{nw}"
        extend 1fcssr " lo que puede hacerle a la gente."
        n 1kslsr "...De primera mano."
        n 4ksqsl "Te mereces mejor que eso,{w=0.1} [player].{w=0.5}{nw}"
        extend 4kslun " Tú {i}eres{/i} mejor que eso."

        if Natsuki.isLove(higher=True):
            n 1kcsun "..."
            n 1ksqsml "Te amo,{w=0.1} [player]."
            n 3fcssrl "{i}Nunca{/i}{w=0.3} voy a dejar que una botella se interponga entre nosotros."
    else:

        n 4unmsr "Oye,{w=0.1} ¿[player]?"
        n 1nllaj "Realmente no me importa tanto si bebes o no."
        n 2ncssr "Solo...{w=0.3} ve despacio con esa cosa."
        n 2flleml "¡P-{w=0.1}pero solo porque no voy a limpiar tu desastre!"
        n 2fllss "Ahaha..."
        n 1kllsr "..."

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_driving",
            unlocked=True,
            prompt="¿Sabes manejar?",
            category=["Transporte"],
            player_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_driving:

    $ already_discussed_driving = get_topic("talk_driving").shown_count > 0 or get_topic("talk_are_you_into_cars").shown_count > 0
    $ chosen_tease = jn_utils.getRandomTease()

    if already_discussed_driving:
        n 4tnmboeqm "...¿Eh?{w=0.75}{nw}"
        extend 1tllsssbr " ¡Ya te dije que no puedo manejar,{w=0.2} [chosen_tease]!"
        n 1fchgnelg "Todavía no tengo licencia,{w=0.2} ¿recuerdas?"
        n 3tllaj "E incluso si quisiera,{w=0.5}{nw}"
        extend 3nslposbl " no creo que podría permitírmelo..."
    else:

        n 1fchdvesm "¡Pffft!{w=0.5}{nw}"
        extend 1uchbselg " ¡Ahaha!"
        n 3fchgn "¿Qué tipo de pregunta es esa,{w=0.1} [player]?"
        n 1tllss "¡Por supuesto que no sé manejar,{w=0.1} [chosen_tease]!{w=0.5}{nw}"
        extend 4fchgn " ¡Ni siquiera tengo licencia!"
        n 2kllpo "Digo...{w=0.3} incluso si quisiera aprender,{w=0.1} no creo que podría permitírmelo."

    n 1uskgs "¡Las lecciones son súper caras hoy en día!"
    n 3fslem "Y luego están las pruebas,{w=0.1} seguro,{w=0.1} combustible,{w=0.1} estacionamiento...{w=0.5}{nw}"
    extend 1fsqaj " es realmente bastante asqueroso qué tan rápido se suma todo."
    n 1nlraj "Creo que preferiría quedarme con el transporte público y mis propios dos pies."
    n 4unmaj "Pero ¿qué hay de ti,{w=0.1} [player]?"
    show natsuki 1tnmss at jn_center


    if persistent.jn_player_can_drive is None:
        menu:
            n "¿Sabes manejar?"
            "Sí, y lo hago actualmente":

                n 1uwdaj "Wow..."
                extend 3fsraj " ...{w=0.3}presumido."
                n 1fsqpo "..."
                n 1fchbg "¡Relájate,{w=0.1} [player]!{w=0.2} ¡Cielos!{w=0.5}{nw}"
                extend 1nchsm " Solo estoy jugando contigo."
                n 4unmbg "Eso es asombroso sin embargo{w=0.1} -{w=0.1} simplemente no puedes vencer la conveniencia de un auto,{w=0.1} ¿verdad?"

                if Natsuki.isAffectionate(higher=True):
                    n 1fllbg "Pero probablemente debería advertirte..."
                    n 3fsgsm "Yo escojo las canciones para nuestra lista de reproducción de viaje."
                    extend 3uchbgelg " ¡Ahaha!"
                else:

                    n 2fllbg "Solo recuerda,{w=0.1} [player]..."
                    n 4fsgsm "¡Pido copiloto!{w=0.5}{nw}"

                $ persistent.jn_player_can_drive = True
                return
            "Sí, pero no manejo ahora mismo":

                n 4unmaj "¿Oh?{w=0.2} ¿Algo anda mal con tu auto,{w=0.1} [player]?"
                n 2tllbo "¿O tal vez...{w=0.3} simplemente no tienes uno en el momento?"
                n 1nnmsm "Bueno,{w=0.1} no soy de juzgar.{w=0.2} Estoy segura de que te las arreglas bien."
                n 2flrss "Además,{w=0.1} estás ayudando al medio ambiente también,{w=0.1} ¿verdad?"

                if Natsuki.isAffectionate(higher=True):
                    n 1fsgsm "Considerado como siempre,{w=0.1} [player]."
                    extend 4nchsm " Ehehe."

                $ persistent.jn_player_can_drive = True
                return
            "No, no sé manejar":

                n 2klrsl "Oh..."
                n 1flrss "Bueno,{w=0.3}{nw}"
                extend 1fchbg " ¡ánimo,{w=0.1} [player]!{w=0.2} No es el fin del mundo."
                n 1usgsg "No te preocupes -{w=0.3}{nw}"
                extend 1fsgsm " ¡te enseñaré cómo usar el autobús!"
                n 4uchsm "Ehehe."

                if Natsuki.isEnamored(higher=True):
                    n 1fllsm "Y además..."
                    n 3fllssl "Eso solo significa que podemos acurrucarnos en el asiento juntos,{w=0.1} [player]."
                    n 1fcsbgl "Un sueño hecho realidad para ti,{w=0.1} ¿verdad?"
                    n 4flldvl "Ehehe."
                else:

                    n 4fchbg "¡Para eso son los amigos, [player]!"

                $ persistent.jn_player_can_drive = False
                return


    elif persistent.jn_player_can_drive:
        menu:
            n "¿Estás manejando mucho?"
            "Sí, manejo frecuentemente":

                n 1fnmbg "Ah,{w=0.1} así que estás como en casa en las carreteras,{w=0.1} ¿verdad?"
                n 4ullss "Me parece justo supongo -{w=0.1} ¡solo recuerda manejar seguro,{w=0.1} [player]!"
            "Solo manejo a veces":

                n 4ullss "Bueno oye,{w=0.1} al menos estás ahorrando en combustible,{w=0.1} ¿verdad?{w=0.5}{nw}"
                extend 1ullsm " Eso no suena como algo malo para mí."
                n 1fchsm "¡Además,{w=0.1} solo significa que puedes ahorrar el kilometraje para los que disfrutes!"
            "No, no estoy manejando mucho":

                n 4unmaj "¿Oh?{w=0.5}{nw}"
                extend 1tllbg " ¡Eso suena como un bono para mí,{w=0.1} honestamente!"
                n 1tnmbg "Solo asegúrate de que todavía sales si no estás manejando mucho sin embargo,{w=0.1} ¿okay?"
            "No, ya no puedo manejar":

                n 4tnmsl "Oh...{w=0.3} ¿pasó algo?"
                n 3kllsl "Lamento...{w=0.3} escuchar eso,{w=0.1} [player]."
                n 1fsgsm "Pero al menos eso significa más tiempo para pasar el rato conmigo,{w=0.1} ¿verdad?{w=0.5}{nw}"
                extend 1fchbg " Ahaha."
                $ persistent.jn_player_can_drive = False

        return
    else:


        menu:
            n "¿Algo nuevo pasando contigo en el frente de manejo?"
            "¡Estoy aprendiendo a manejar!":

                n 4fnmss "¡Ooh!{w=0.5}{nw}"
                extend 1fchbg " ¡Bien,{w=0.1} [player]!"
                n 1fchsm "No te preocupes por la prueba,{w=0.1} ¿está bien?{w=0.2} ¡Estoy segura de que lo harás bien!"

                if Natsuki.isAffectionate(higher=True):
                    n 4uchsm "I believe in you,{w=0.1} [player]!"
            "¡Pasé mi prueba!":

                n 4uskgs "¿No es broma?{w=0.5}{nw}"
                extend 3uchbs " ¡Yaaay!{w=0.2} ¡Felicidades,{w=0.1} [player]!"

                if Natsuki.isLove(higher=True):
                    n 4kwmsm "¡Sabía que podías hacerlo,{w=0.1} gran tonto!"
                    extend 4kchsm " Ehehe."

                n 3kwmsm "Solo asegúrate de mantener los buenos hábitos cuando continúes aprendiendo por tu cuenta,{w=0.1} ¿está bien?{w=0.2} Ahaha."
                $ persistent.jn_player_can_drive = True
            "¡Puedo manejar de nuevo!":

                n 3uchbgedz "¡Oye!{w=0.2} ¡Bien ahí,{w=0.1} [player]!"
                n 1fchbl "¡Maneja seguro!"
                $ persistent.jn_player_can_drive = True
            "Nop, nada nuevo":

                n 4unmaj "¿Oh?{w=0.5}{nw}"
                extend 1nlrss " ¡Bueno,{w=0.1} me parece justo!"
                n 2tnmsm "¿Tú y yo ambos entonces,{w=0.1} en ese caso?{w=0.5}{nw}"
                extend 1nchsm " Ahaha."

        return
    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_sustainable_fashion",
            unlocked=True,
            prompt="Moda sostenible",
            category=["Medio ambiente", "Moda"],
            nat_says=True,
            affinity_range=(jn_affinity.UPSET, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_sustainable_fashion:
    n 1nnmaj "Oye,{w=0.1} [player]..."
    n 3nllaj "Esto es medio aleatorio,{w=0.1} pero..."
    extend 4unmpu " ¿te gusta la moda?"
    if Natsuki.isHappy(higher=True):
        n 1fcsbg "¡Yo sé que a mí sí!{w=0.2} ¿Se nota?"
        extend 1nchsm " Ehehe."
    else:

        n 1nnmpu "Sé que a mí sí."

    n 3fllpu "Pero lo que me toma por sorpresa es justo cuánto desperdicio hay."

    if Natsuki.isNormal(higher=True):
        n 1uwdgs "En serio,{w=0.1} [player] {w=0.1}-{w=0.1} ¡es de locos!"
        n 1ullaj "La gente tira un {i}montón{/i} de ropa...{w=0.5}{nw}"
        extend 3flrem " se estima que desechamos alrededor de 90{w=0.3} {i}millones{/i}{w=0.3} de toneladas cada año."
        n 1fnman "¡Eso es un camión lleno cada segundo!{w=0.2} ¡Qué desperdicio!"
    else:

        n 1nllbo "Es bastante loco, honestamente."
        n 2fnmsl "Recuerdo leer en alguna parte que desechamos algo así como 90{w=0.3} {i}millones{/i}{w=0.3} de toneladas cada año."
        n 1fcsan "Eso es literalmente un camión lleno {i}cada{w=0.3} segundo{/i}."

    n 2fsrem "Y ni siquiera hemos empezado a hablar sobre la cantidad de agua usada para lavar y plástico usado para empaquetado también."
    n 1ksrsr "...O las condiciones que algunos de los trabajadores haciendo nuestra ropa tienen que soportar."

    if Natsuki.isNormal(higher=True):
        n 1fcssm "¡Es de hecho una de las razones por las que empecé a aprender a coser!"
        n 2klrsr "Yo...{w=0.3} nunca he tenido toneladas de dinero para comprar más ropa de todos modos,{w=0.1} así que trato de reusar y arreglar lo que puedo."
        n 1fchbg "¡Pero te sorprendería lo que puedes lograr con un poco de creatividad!"
        extend 1fcssm " Y solo una pizca de saber-cómo también,{w=0.1} obviamente."
        n 4fchgn "Apuesto a que no sabías que mi falda rosa favorita fue hecha a mano,{w=0.1} ¿o sí?"

    n 1unmaj "Creo que te he sermoneado suficiente por ahora,{w=0.1} [player],{w=0.1} así que no seguiré dándote la lata con eso."
    n 3nllpu "Pero...{w=0.3} la próxima vez que estés comprando ropa,{w=0.1} ¿o mirando a través de catálogos en línea?"
    n 3unmpu "Solo piensa un poco en el medio ambiente,{w=0.1} ¿harías eso?"

    if Natsuki.isAffectionate(higher=True):
        n 1kllssl "¿Por mí?"
        n 1nchbg "Ahaha.{w=0.5}{nw}"
        extend 4uchsm " ¡Gracias,{w=0.1} [player]!"

    elif Natsuki.isNormal(higher=True):
        n 1nchbg "Ahaha.{w=0.5}{nw}"
        extend 4uchsm " ¡Gracias,{w=0.1} [player]!"
    else:

        n 1nllsl "Gracias."

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_give_nickname",
            unlocked=True,
            prompt="Can I give you a nickname?",
            conditional="persistent._jn_nicknames_natsuki_allowed",
            category=["Natsuki"],
            player_says=True,
            affinity_range=(jn_affinity.ENAMORED, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_give_nickname:

    if persistent._jn_nicknames_natsuki_allowed and persistent._jn_nicknames_natsuki_current_nickname == "Natsuki":
        n 1unmaj "¿Eh?{w=0.2} ¿Quieres darme un apodo?"
        n 2fsqsl "¿Por qué?{w=0.2} ¿Natsuki no es suficientemente bueno para ti?{w=0.2} ¿Es eso?"
        extend 4fsqpu " ¿Huh?{w=0.2} ¡Vamos, [player]!{w=0.2} ¡Suéltalo!"
        n 1fsqsm "..."
        n 1fchbg "¡Relájate,{w=0.1} [player]!{w=0.2} ¡Cielos!{w=0.2} ¡Solo estoy bromeando!"
        extend 1fchsm " Ehehe."
        n 3ullbg "Bueno...{w=0.3} ¡no veo por qué no!"
    else:




        if persistent._jn_nicknames_natsuki_bad_given_total == 0:
            n 4unmaj "¿Oh?{w=0.2} ¿Quieres darme otro apodo?"
            n 1uchbg "Seguro,{w=0.1} ¡por qué no!"

        elif persistent._jn_nicknames_natsuki_bad_given_total == 1:
            n 4unmaj "¿Quieres darme un nuevo apodo?"
            n 1unmbo "Está bien,{w=0.1} [player]."

        elif persistent._jn_nicknames_natsuki_bad_given_total == 2:
            n 1nnmsl "¿Otro apodo,{w=0.1} [player]?{w=0.5}{nw}"
            extend 1nllsl " Bien."
            n 2ncsaj "Solo...{w=0.3} piensa un poco en lo que elijes,{w=0.1} ¿okay?"

        elif persistent._jn_nicknames_natsuki_bad_given_total == 3:
            n 1nnmsl "Está bien,{w=0.1} [player]."
            n 2fsqpu "Solo recuerda.{w=0.3} Has tenido tu advertencia final sobre esto."
            n 1nsqsl "No me decepciones de nuevo."


    $ nickname = renpy.input(prompt="¿Qué tenías en mente,{w=0.2} [player]?", allow=jn_globals.DEFAULT_ALPHABETICAL_ALLOW_VALUES, length=10).strip()

    if nickname.lower() == "nevermind" or nickname.lower() == "olvídalo" or nickname.lower() == "olvidalo":
        n 4tnmpu "¿Huh?{w=0.2} ¿Cambiaste de opinión?"
        n 4tllpu "Bueno...{w=0.3} está bien entonces."
        n 1nnmaj "Solo déjame saber si de hecho quieres llamarme algo más entonces,{w=0.1} ¿okay?"
        return
    else:

        $ nickname_type = jn_nicknames.getNatsukiNicknameType(nickname)

    if nickname_type == jn_nicknames.NicknameTypes.invalid:
        n 2tlraj "Uhmm...{w=0.3} [player]?"
        n 1tnmaj "No creo que eso sea un apodo para nada."
        n 1tllss "Me...{w=0.3} quedaré con lo que tengo ahora,{w=0.1} gracias."
        return

    elif nickname_type == jn_nicknames.NicknameTypes.loved:
        $ persistent._jn_nicknames_natsuki_current_nickname = nickname
        $ n_name = persistent._jn_nicknames_natsuki_current_nickname
        n 1uskgsl "¡O-{w=0.1}oh!{w=0.2} ¡[player]!"
        n 1ulrunl "..."
        n 1fcsbgl "B-{w=0.1}bueno,{w=0.1} tienes buen gusto,{w=0.1} al menos."
        n 1fcssml "¡[nickname] será!{w=0.5}{nw}"
        extend 1uchsml " Ehehe."
        return

    elif nickname_type == jn_nicknames.NicknameTypes.disliked:
        n 2fsqbo "Vamos,{w=0.1} [player]...{w=0.3} ¿en serio?"
        n 2fllsl "Sabías que no voy a estar cómoda siendo llamada así."
        n 1fcssl "..."
        n 1nlraj "Voy a...{w=0.3} pretender que no dijiste eso,{w=0.1} ¿está bien?"
        return

    elif nickname_type == jn_nicknames.NicknameTypes.hated:
        n 2fskem "¿Q-{w=0.1}qué?{w=0.5}{nw}"
        extend 1fscwr " ¡¿Cómo me acabas de llamar?!"
        n 2fcsan "¡[player]!{w=0.2} ¡No puedo creerte!"
        n 2fcsfu "¿Por qué me llamarías así?{w=0.5}{nw}"
        extend 1fsqfu " ¡Eso es {i}horrible{/i}!"
        n 1fcspu "..."
        $ persistent._jn_nicknames_natsuki_bad_given_total += 1

    elif nickname_type == jn_nicknames.NicknameTypes.profanity:
        n 4fskpu "¡¿D-{w=0.1}disculpa?!"
        n 2fskfu "¡¿Qué demonios me acabas de llamar,{w=0.1} [player]?!"
        n 1fcsan "..."
        n 1fslan "Seriamente no puedo creerte,{w=0.1} [player].{w=0.5}{nw}"
        extend 2fnman " ¿Por qué harías eso?{w=0.1} ¡¿Estás {i}tratando{/i} de colmar mi paciencia?!"
        n 1fcspu "..."
        $ persistent._jn_nicknames_natsuki_bad_given_total += 1

    elif nickname_type == jn_nicknames.NicknameTypes.funny:
        n 4nbkdvesm "¡Pffft!"
        n 1uchbselg "¡Ahaha!"
        n 1fbkbs "¡¿[nickname]?!{w=0.2} ¿Qué se supone que sea eso,{w=0.1} [player]?"
        n 4fchbg "Bueno...{w=0.3} tienes suerte de que tenga un sano sentido del humor."
        n 4fsgbg "¡[nickname] será entonces,{w=0.1} supongo!{w=0.5}{nw}"
        extend 1fchgn " Ehehe."

        $ persistent._jn_nicknames_natsuki_current_nickname = nickname
        $ n_name = persistent._jn_nicknames_natsuki_current_nickname
        return

    elif nickname_type == jn_nicknames.NicknameTypes.nou:
        n 2usqsg "¡Tú más~!"
        return
    else:

        $ neutral_nickname_permitted = False


        if nickname.lower() == "natsuki":
            n 1fllss "Uhmm...{w=0.5}{nw}"
            extend 4tnmdv " ¿[player]?"
            $ chosen_tease = jn_utils.getRandomTease()
            n 1fchbg "¡Ese es solo mi nombre normal,{w=0.1} [chosen_tease]!"
            n 3fcsca "Honestamente...{w=0.5}{nw}"
            extend 3ksgsg " a veces me pregunto por qué me molesto."
            n 1unmbg "Bueno,{w=0.1} ¡no me estoy quejando!{w=0.2} Si no está roto,{w=0.1} no lo arregles -{w=0.1} ¿verdad?"
            n 1nchbg "Ahaha."
            $ neutral_nickname_permitted = True

        elif nickname.lower() == "thiccsuki":
            n 3kllunl "..."
            n 3fnmssl "S-{w=0.1}soñando en grande,{w=0.1} ¿verdad,{w=0.1} [player]?"
            n 1klrsrl "Uhmm..."
            n 4klrpol "Realmente...{w=0.3} no soy...{w=0.3} fan,{w=0.1} pero si es lo que prefieres..."
            $ neutral_nickname_permitted = True

        elif nickname.lower() == persistent.playername.lower():
            n 4fsldv "Yo...{w=0.3} no creo que hayas pensado bien esto,{w=0.1} [player]."
            n 1tnmbg "¿Siquiera sabes cuán confuso sería eso?"
            n 1tlrss "Creo...{w=0.3} que me quedaré con lo que funciona,{w=0.1} ¿okay?{w=0.5}{nw}"
            extend 4fsqsm " Ehehe."
            n 1uchbg "¡Buen intento sin embargo!"
        else:


            n 1fllsr "Hmm...{w=0.5}{nw}"
            extend 1ullpu " [nickname],{w=0.1} ¿eh?"
            n 4fllss "[nickname]..."
            n 1fnmbg "¿Sabes qué?{w=0.2} ¡Sí!{w=0.2} ¡Me gusta!"
            n 3fchbg "¡Considéralo hecho,{w=0.1} [player]!{w=0.5}{nw}"
            extend 3uchsm " Ehehe."
            $ neutral_nickname_permitted = True


        if (neutral_nickname_permitted):
            $ persistent._jn_nicknames_natsuki_current_nickname = nickname
            $ n_name = persistent._jn_nicknames_natsuki_current_nickname

        return


    if persistent._jn_nicknames_natsuki_bad_given_total == 1:
        n 2kllsf "Cielos,{w=0.1} [player]...{w=0.3} ¡eso no es propio de ti para nada!{w=0.5}{nw}"
        extend 1knmaj " ¿Qué pasa contigo hoy?"
        n 1kcssl "..."
        n 1knmsl "Solo...{w=0.3} no hagas eso de nuevo,{w=0.1} ¿está bien?"
        n 2fsqsl "Eso realmente dolió,{w=0.1} [player].{w=0.2} No abuses de mi confianza."


        $ Natsuki.addApology(jn_apologies.ApologyTypes.bad_nickname)
        $ Natsuki.percentageAffinityLoss(1)

    elif persistent._jn_nicknames_natsuki_bad_given_total == 2:
        n 1fsqsl "No puedo creer que me hicieras eso de nuevo,{w=0.1} [player]."
        n 2fsqan "¡Te dije que duele,{w=0.1} y fuiste adelante de todos modos!"
        n 1fcsan "..."
        n 1fcsun "Tú...{w=0.3} realmente...{w=0.3} me gustas, [player].{w=0.5}{nw}"
        extend 4kllun " Duele extra mal cuando eres tú."
        n 2fsqsr "No pruebes mi paciencia como esto.{w=0.2} Eres mejor que eso."


        $ Natsuki.addApology(jn_apologies.ApologyTypes.bad_nickname)
        $ Natsuki.percentageAffinityLoss(2.5)

    elif persistent._jn_nicknames_natsuki_bad_given_total == 3:
        n 1fsqan "Eres honestamente increíble,{w=0.1} [player]."
        n 2fnmfu "¡Te lo he dicho tantas veces ya,{w=0.1} y todavía no paras!"
        n 1fcspu "..."
        n 2fsqpu "No más advertencias,{w=0.1} [player]."
        menu:
            n "¿Entiendes?"
            "Entiendo":

                n 1fsqsr "Entiendes,{w=0.1} ¿verdad?"
                n 2fsqan "...Entonces empieza a actuar como tal,{w=0.1} [player]."
                n 1fslsl "Gracias."

                $ Natsuki.percentageAffinityLoss(3)
            "...":

                n 1fcssl "Mira.{w=0.2} No estoy bromeando,{w=0.1} [player]."
                n 1fnmpu "Actuar así no es gracioso,{w=0.1} o lindo."
                n 2fsqem "Es tóxico."
                n 1fsqsr "No me importa si estás tratando de tomarme el pelo.{w=0.2} Déjalo."

                $ Natsuki.percentageAffinityLoss(5)


        $ Natsuki.addApology(jn_apologies.ApologyTypes.bad_nickname)

    elif persistent._jn_nicknames_natsuki_bad_given_total == 4:

        n 2fcsan "Sí,{w=0.1} no.{w=0.2} He escuchado suficiente.{w=0.2} No necesito escuchar más."
        n 1fnmem "¿Cuándo aprenderás que tus acciones tienen consecuencias?"
        n 1fcspu "..."
        n 1fnmpu "¿Sabes qué?{w=0.5}{nw}"
        extend 2fsqpu " Ni te molestes en responder."
        n 1fsqsr "Te lo advertí,{w=0.1} [player].{w=0.2} Recuerda eso."


        python:
            get_topic("talk_give_nickname").lock()
            Natsuki.percentageAffinityLoss(10)
            persistent._jn_nicknames_natsuki_allowed = False
            persistent._jn_nicknames_natsuki_current_nickname = None
            n_name = "Natsuki"
            Natsuki.addApology(jn_apologies.ApologyTypes.bad_nickname)


    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_sleeping_well",
            unlocked=True,
            prompt="Dormir bien",
            conditional="persistent.jn_total_visit_count >= 5",
            category=["Salud", "Tú"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_sleeping_well:
    n 1fllpu "Huh..."
    n 4uwdaj "Oye,{w=0.1} [player].{w=0.5}{nw}"
    extend 1nnmaj " Déjame hacerte una pregunta,{w=0.1} ¿okay?"
    n 2fsqsr "¿Cómo duermes de noche?"
    n 1fsqpu "Sé honesto.{w=0.2} ¿Cómo lo haces?"
    n 1ksqsm "..."
    n 3fchsm "Ehehe.{w=0.2} ¿Te atrapé?"
    n 1unmaj "Pero en serio,{w=0.2} [player].{w=0.5}{nw}"
    extend 4tnmaj " ¿Luchas con tu sueño?"


    if jn_utils.get_current_session_length().total_seconds() / 3600 >= 12:
        n 2fsqpo "Digo,{w=0.1} {i}has{/i} estado aquí por un rato ya..."
        n 1ullaj "Así que...{w=0.5}{nw}"
        extend 1nnmaj " me imaginé que podrías sentirte un poco somnoliento de todos modos."

    elif jn_admissions.last_admission_type == jn_admissions.TYPE_TIRED:
        n 2fllpo "Digo,{w=0.1} incluso {i}dijiste{/i} que estabas cansado antes."
        n 1ullaj "Así que...{w=0.5}{nw}"
        extend 1nnmaj " solo tiene sentido preguntar,{w=0.1} ¿verdad?{w=0.2} Como sea..."

    n 2fslpu "Lo admitiré,{w=0.1} tengo la rara noche de insomnio yo misma.{w=0.5}{nw}"
    extend 4fbkwr " ¡Es lo peor!"
    n 1fllem "No hay nada que odie más que dar vueltas y vueltas,{w=0.3}{nw}"
    extend 2fcsan " solo esperando a que mi cuerpo decida que es hora de que suceda el mañana."
    n 1ullaj "Pero...{w=0.5}{nw}"
    extend 4fnmss " ya sabes lo que dicen,{w=0.1} [player]."
    n 3fcsss "Con el sufrimiento...{w=0.5}{nw}"
    extend 3uchbg " ...¡viene la sabiduría!"
    n 1nsqbg "Y afortunadamente para ti,{w=0.1} no me importa compartir.{w=0.5}{nw}"
    extend 1nchsm " Ehehe."
    n 1fcsbg "Así que,{w=0.1} escucha bie -{w=0.1} ¡es hora de otra lección de tu servidora!"
    n 1fnmaj "Muy bien -{w=0.1} primero,{w=0.1} ¡déjate de tonterías!{w=0.2} Si estás tratando de dormir,{w=0.1} cualquier cosa alta en azúcar o cafeína es tu enemigo."
    n 3fllss "Así que antes que nada,{w=0.1} deja el refresco y el café.{w=0.2} Puedes agradecerme después."
    n 1fcsaj "Siguiente -{w=0.1} ¡sin pantallas!{w=0.5}{nw}"
    extend 4fsqpo " Incluyendo esta,{w=0.1} [player]."
    n 1unmsl "Sin pantalla significa sin luces brillantes o distracciones para mantenerte despierto,{w=0.1} obviamente."
    n 1fnmpu "Si estás cansado entonces lo último que necesitas es algo irradiándote lo que sea."

    if jn_activity.ACTIVITY_MANAGER.hasPlayerDoneActivity(jn_activity.JNActivities.anime_streaming):
        n 3tsqsr "Y no, [player] {w=0.1}-{w=0.3}{nw}"
        extend 3fnmpo " Nada de sesiones de maratón de anime tarde por la noche tampoco."
        n 1nchgn "¡Lo siento~!"

    n 1fcsbg "Continuando, ¡siguiente es la temperatura!{w=0.2} Si hace calor,{w=0.1} usa sábanas más delgadas y viceversa."
    n 1fcspu "Nada interrumpe tu sueño más que tener que arrancar cobijas,{w=0.1} o sacar algunas."
    n 3fsgsg "¿Me sigues hasta ahora,{w=0.1} [player]?{w=0.5}{nw}"
    extend 4fchgn " Casi termino,{w=0.1} no te preocupes."
    n 1unmaj "Por último...{w=0.5}{nw}"
    extend 1fchbg " ¡ponte cómodo!"
    n 1nnmsm "Asegúrate de tener suficientes almohadas para apoyar tu cabeza,{w=0.1} o tal vez incluso pon algo de música tranquila si encuentras que eso ayuda."
    n 1fcssm "...¡Y eso es todo!"
    n 1nllss "Deberías haber sabido al menos algunas de esas ya,{w=0.3}{nw}"
    extend 4unmss " pero de todas formas..."
    n 3fwlbg "¡Espero que puedas descansar tranquilo con tu nuevo conocimiento,{w=0.1} [player]!"
    n 1uchsm "Ehehe."

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_aging",
            unlocked=True,
            prompt="Envejecer",
            category=["Vida"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_aging:
    n 1unmaj "Sabes,{w=0.1} [player]..."
    n 1nllpu "Creo que la mayoría de la gente comparte un montón de miedos."
    n 1unmpu "Entiendes a lo que me refiero,{w=0.1} ¿verdad?{w=0.2} Como presentar cosas a una habitación llena de gente,{w=0.1} o reprobar un examen."
    n 3tlrss "Por supuesto,{w=0.1} es raro encontrar uno que {i}todos{/i} tengan..."
    n 1tnmaj "O al menos algo que haga a cualquiera sentirse inquieto."
    n 1unmbg "Pero...{w=0.3} ¡creo que encontré uno!"
    n 4usgsm "¿En qué estoy pensando,{w=0.1} preguntas?"
    n 1ullaj "Bueno...{w=0.3} es de hecho un poco aburrido,{w=0.1} realmente."
    n 1nnmbo "Estaba de hecho pensando sobre envejecer."
    n 3unmpu "¿Alguna vez has pensado mucho sobre ello,{w=0.1} [player]?"
    n 4fllbg "Probablemente es la última cosa en tu mente si eres bastante joven."
    n 1nwmpu "Pero creo que a medida que de hecho envejeces,{w=0.1} empieza a colarse."
    n 1kllpu "Podrías tener menos energía,{w=0.1} o amigos y familia comienzan a alejarse..."
    n 2knmem "Los cumpleaños pierden todo significado -{w=0.1} ¡podrías incluso temerles!"
    n 1ullaj "Las señales aparecen en un montón de formas,{w=0.3}{nw}"
    extend 1knmsl " pero eso es lo que lo hace desconcertante."
    n 1kllaj "Todos lo experimentan diferente,{w=0.3}{nw}"
    extend 2ksksl " ¡y ni siquiera sabemos qué pasa después del final!"
    n 1klrss "Espeluznante,{w=0.1} ¿eh?"
    n 1ulrpu "Aunque...{w=0.3} supongo que podrías decir que eso es más el miedo a lo desconocido que al envejecimiento en sí."
    n 2flraj "Lo que sí me molesta sin embargo es qué tan inmadura puede ser la gente sobre ello."
    n 1fnmaj "¡Especialmente cuando se trata de relaciones entre diferentes edades!"
    n 2fslsf "La gente simplemente se pone tan sermoneadora sobre eso..."
    n 1fllaj "Como...{w=0.3} mientras ambos sean felices,{w=0.2} es todo legal,{w=0.3}{nw}"
    extend 4fnmem " y nadie esté siendo lastimado o hecho sentir incómodo,{w=0.1} ¿a quién le importa {i}realmente{/i}?"
    n 2nlrpu "Es justo como la mayoría de cosas,{w=0.1} realmente."
    n 1unmaj "Además,{w=0.1} no es como que tener cierta edad signifique que {i}tienes{/i} que ser de cierta manera."
    n 1fchbg "Digo...{w=0.3} ¡mira a Yuri!"
    n 1uchgn "Siendo toda anticuada así -{w=0.1} ¡pensarías que está retirada!"
    n 4nllbg "Pero como sea...{w=0.3} creo que nos desviamos."
    n 1unmss "Realmente no me importa qué tan viejo seas,{w=0.1} [player]."

    if Natsuki.isLove(higher=True):
        $ chosen_tease = jn_utils.getRandomTease()
        n 3klrpol "M-{w=0.1}mejor que sepas que te amo igual,{w=0.1} [chosen_tease]."
        n 3knmpol "No olvides eso,{w=0.1} ¿okay?"
        n 4flrpol "Me enojaré si lo haces.{w=0.5}{nw}"
        extend 1klrbgl " Ahaha..."

    elif Natsuki.isEnamored(higher=True):
        n 2fllbgl "Has sido bastante asombroso conmigo igual."

    elif Natsuki.isHappy(higher=True):
        n 4fchbgl "¡Siempre es divertido pasar el rato contigo!"
    else:

        n 1fllbg "Pero...{w=0.3} ¿solo por si acaso?"
        n 2fsqsg "Solo tendremos una vela en tu pastel de cumpleaños.{w=0.2} Lo siento.{w=0.5}{nw}"
        extend 1uchbgelg " ¡Ahaha!"

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_work_life_balance",
            unlocked=True,
            prompt="Equilibrio vida-trabajo",
            category=["Vida", "Sociedad"],
            nat_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_work_life_balance:
    if Natsuki.isUpset(higher=True):
        n 4ullaj "Sabes,{w=0.1} [player]..."

    n 1nnmaj "Creo que hoy en día es bastante fácil dejar que la vida académica o laboral se cuele en tu tiempo personal."
    n 2nlrsl "Quiero decir...{w=0.3} piénsalo."
    n 1nnmsl "Con todos teniendo celulares,{w=0.1} más usualmente algún tipo de computadora en casa -{w=0.1} es difícil no estar conectado de alguna manera."
    n 2flrbo "Y como...{w=0.3} si ya hay esa conexión,{w=0.1} entonces ¿qué detiene al trabajo de molestarte durante tu tiempo libre?"
    n 2fsrun "¿O compañeros de clase pidiendo ayuda en el último minuto posible?"

    if Natsuki.isUpset(higher=True):
        n 1fcsem "Simplemente se vuelve molesto -{w=0.1} como si todos esperaran que siempre estés ahí para aportar un poco más,{w=0.1} ¡o terminar algo!"
        n 2fnmpo "Abrumador,{w=0.1} ¿verdad?"
        n 1fllaj "Huh.{w=0.2} De hecho...{w=0.3} ahora que lo pienso..."
        n 4fnmsf "No es como que ese tipo de intrusión esté solo limitada a cuando estás lejos tampoco."
        n 1fslpu "He escuchado {i}demasiadas{/i} historias de gente haciendo cantidades estúpidas de horas extra en el trabajo...{w=0.5}{nw}"
        extend 3fnman " ¡a veces ni siquiera pagadas!"
        n 1fsran "O incluso estudiantes estudiando hasta tarde en la noche hasta que colapsan...{w=0.3} ¡es una locura!"
    else:

        n 1fsqpu "Simplemente se vuelve molesto -{w=0.1} todos esperan que siempre estés ahí para hacer más."
        n 2fslsl "De hecho,{w=0.1} ahora que lo pienso..."
        n 1fcsaj "No es como que ese tipo de cosa esté solo limitada a cuando estás lejos tampoco."
        n 1fsrsr "He escuchado demasiadas historias de gente haciendo cantidades estúpidas de horas extra en el trabajo.{w=0.5}{nw}"
        extend 3fsqan " A menudo ni siquiera pagadas."
        n 1fslem "O incluso estudiantes estudiando hasta tarde en la noche hasta que colapsan..."

    if Natsuki.isNormal(higher=True):
        n 1kcsemesi "Ugh...{w=1} Solo desearía que la gente valorara su propio tiempo más."
        n 1klrsr "..."
        n 4unmaj "Oye,{w=0.1} [player]..."
        n 1nllaj "No sé si estás trabajando,{w=0.1} o estudiando,{w=0.1} o qué..."
        n 3fnmsf "Pero más te vale no estar dejando que lo que sea que sea tome control de tu vida.{w=0.2} ¿Entiendes?"

        if Natsuki.isEnamored(higher=True):
            n 1knmpu "Eres {i}más{/i} que tu carrera,{w=0.1} o tu educación.{w=0.2} Tienes tus propios deseos y necesidades que importan también."
            n 3kllun "No quiero que algún trabajo tonto o tarea estúpida tome control de tu vida."
            n 1fcsun "Tú eres...{w=0.3} mucho más importante que cualquiera de esas cosas,{w=0.1} [player].{w=0.2} Créeme."

            if Natsuki.isLove(higher=True):
                n 4fllun "Además..."
                n 1fllssl "Tú y tu tiempo son míos primero, [player]."
                n 3flldvl "Ya lo pedí primero,{w=0.1} d-{w=0.1}después de todo.{w=0.5}{nw}"
                extend 3fchsml " Ehehe..."
        else:

            $ chosen_tease = jn_utils.getRandomTease()
            n 3kllpo "La gente es más que lo que hace para ganarse la vida,{w=0.1} después de todo.{w=0.2} ¡Y eso te incluye a ti también, [chosen_tease]!"

    elif Natsuki.isDistressed(higher=True):
        n 3fllsr "Me hace desear que la gente valorara su propio tiempo más."
        n 1fnmsr "...Supongo que eso te incluye a ti también,{w=0.1} [player]."
        n 1fllpu "Tienes mejores cosas que hacer."
        n 2fsqsf "...Como ser un amigo decente para otros para variar.{w=0.2} ¿Tengo razón?"
    else:

        n 1fslbo "La gente necesita valorar su propio tiempo más,{w=0.1} supongo."
        n 1fcssl "...Heh."
        n 3fcsunl "Tal vez debería seguir mi propio consejo..."
        n 1fsqanltsb "Porque {i}claramente{/i} estar aquí es un desperdicio de mi tiempo también."

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_using_headphones_carefully",
            unlocked=True,
            prompt="Usar audífonos con cuidado",
            category=["Salud", "Música", "Tecnología"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_using_headphones_carefully:
    n 1unmaj "..."
    n 4tnmaj "...?"
    n 2fnmaw "...!"
    n 1fbkwr "¡...[player]!"
    n 3fnmpo "¡[player]!{w=0.2} ¡Finalmente!{w=0.2} ¿Puedes escucharme ahora?"
    n 3fllpo "Cielos...{w=0.3} ¡te tomaste tu tiempo!"
    n 1fslsm "..."
    n 1uchbg "Ehehe."
    n 4fnmbg "¡Admítelo,{w=0.1} [player]!{w=0.2} Te atraparé uno de estos días."
    n 1nnmaj "Pero en serio -{w=0.1} ¿usas audífonos o algo así a menudo?"
    n 3nlrpo "Lo admitiré,{w=0.1} probablemente uso los míos más de lo que debería."
    n 1fnmaj "Estaba medio bromeando sobre toda la cosa de escuchar,{w=0.1} pero esto es importante,{w=0.1} [player]."
    n 1nlrss "A mí me gusta subirle volumen también -{w=0.1} solo no hagas un mal hábito de ello."
    n 4unmsl "Hay incluso advertencias en algunos países si tienes el volumen demasiado alto..."
    n 1fllem "...¡Y por una buena razón!"
    n 2fnmpo "No solo para proteger tus oídos tampoco -{w=0.1} mejor ten cuidado usándolos fuera también."
    n 1fcsem "¡No quiero escuchar sobre ti siendo atropellado porque no escuchaste algo venir!"
    n 4unmbo "Oh -{w=0.1} y una última cosa,{w=0.1} de hecho."
    n 1unmpu "Podrías usarlos para enfocarte en el trabajo o relajarte en casa -{w=0.1} ¡y eso está bien!"
    n 2nnmsr "Pero por favor,{w=0.1} [player]."
    n 4flrsr "...Quítatelos de vez en cuando,{w=0.1} ¿lo harás?{w=0.2} Por otras personas,{w=0.1} digo."
    n 1ncsbo "Lo entiendo -{w=0.1} si solo quieres escuchar algo en paz,{w=0.1} o darte algo de espacio,{w=0.1} eso está bien."

    if jn_activity.ACTIVITY_MANAGER.hasPlayerDoneActivity(jn_activity.JNActivities.music_applications):
        n 1kslbg "Sé que te gusta tu streaming de música."

    n 1nsqbo "Pero no los uses para bloquearte de todos y todo."
    n 2ksrsl "Es...{w=0.3} no es saludable hacer eso tampoco,{w=0.1} [player]."
    n 1nchsm "...¡Y eso es casi todo lo que tenía que decir!"
    n 4fchbg "¡Gracias por {i}escucharme{/i},{w=0.1} [player]!{w=0.2} Ehehe."
    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_thoughts_on_horror",
            unlocked=True,
            prompt="Pensamientos sobre el horror",
            category=["Media", "Literatura"],
            nat_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_thoughts_on_horror:

    if Natsuki.isNormal(higher=True):
        n 4unmaj "Sabes,{w=0.1} [player]..."
        n 1tllaj "No creo que alguna vez explicara por qué me disgusta tanto el horror."
        n 1tlrss "Sé que lo mencioné antes,{w=0.1} pero fui medio tomada desprevenida en el momento."
        n 3unmaj "¿Honestamente?"
        n 1nnmsm "Cada quien tiene sus gustos,{w=0.1} ¿verdad? Y puedo entender por qué la gente lo disfruta."

    elif Natsuki.isDistressed(higher=True):
        n 1nllbo "No creo que explicara por qué me disgusta el horror."
        n 2nnmsl "Entiendo que todos tengan sus gustos,{w=0.1} pero no me importa."
    else:

        n 1kslsl "..."
        n 2fsqun "...Estaba a punto de compartir algunos de mis pensamientos sobre el horror contigo.{w=1}{nw}"
        extend 1fsrsl " O al menos,{w=0.1} estaba pensando en ello."
        n 2fsqem "...Pero entonces sabes de lo que me di cuenta,{w=0.1} [player]?"
        n 1fsqan "Odio el horror -{w=0.5}{nw}"
        extend 1fllem " no que te importara -{w=0.3}{nw}"
        extend 4fnmful " ¿y honestamente?"
        n 1fcsanltsa "Estar atrapada aquí {i}contigo{/i} es suficiente horror."
        return

    if Natsuki.isNormal(higher=True):
        n 1fchbg "¡Como Yuri!"
        n 1fcsss "¡Es lleno de suspenso,{w=0.1} y los miedos son un motivador súper poderoso para los personajes!"
        n 4ullpu "Así que no me malinterpretes{w=0.1} -{w=0.1} puedo totalmente apreciar el esfuerzo que conlleva."
        n 2fllpol "...Cuando no son solo sustos estúpidos,{w=0.1} c-{w=0.1}como sea."
    else:

        n 2uslbo "I get the effort that goes into it.{w=0.2} For the most part."

    n 1nllpu "Pero..."
    n 1nnmbo "Cuando leo algo -{w=0.1} o veo algo -{w=0.1} lo hago porque para mí,{w=0.1} es cómo me relajo."
    n 1fllbo "No quiero que me hagan sentir inquieta."
    n 2fllpu "No quiero que me hagan saltar."
    n 2fllsr "No quiero tener que ver cosas asquerosas."
    n 1fcssr "Yo...{w=0.3} solo quiero sentarme,{w=0.1} sentirme bien y simplemente escapar un rato."
    n 4fnmsl "Hay más que suficientes cosas desagradables pasando allá afuera,{w=0.1} ¿sabes?"
    n 1flrpu "Algunas cosas más cerca de casa que otras."
    n 1fcssl "..."
    n 1nnmaj "Así que...{w=0.3} sí.{w=0.1} Eso es casi todo lo que tenía que decir al respecto."

    if Natsuki.isAffectionate(higher=True):
        n 1unmss "Aunque...{w=0.3} ¿si quieres poner algo,{w=0.1} [player]?{w=0.2} Adelante."
        n 2fllssl "Si eres tú,{w=0.1} {i}creo{/i} que puedo lidiar con ello."
        n 2flrpol "Pero...{w=0.3} mantendremos el volumen bajo.{w=0.2} ¿Entendido?"

    elif Natsuki.isNormal(higher=True):
        n 1nnmaj "No te preocupes por mí,{w=0.1} [player].{w=0.2} Si quieres ver algo,{w=0.1} hazlo."
        n 2flrcal "Pero lo verás solo."

    elif Natsuki.isDistressed(higher=True):
        n 1flrsl "..."
        n 1fnmpu "{i}Pediría{/i} que si fueras a ver algo como eso,{w=0.1} entonces me avises primero."
        n 2fsqsrtsb "Pero no me escucharías de todos modos,{w=0.1} ¿verdad?"

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_gaming",
            unlocked=True,
            prompt="¿Te gustan los videojuegos?",
            category=["Juegos", "Media"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_gaming:
    if Natsuki.isNormal(higher=True):
        n 4unmaj "¿Videojuegos?"
        n 1fcsbg "Bueno...{w=0.3} ¡duh!"
        n 1fnmbg "¡Apuéstalo que me gustan los videojuegos,{w=0.1} [player]!"
        n 3ullss "No diría que soy la jugadora más activa...{w=0.2} pero definitivamente hago mi parte de machacar botones."
        n 1nslsg "Hmm..."
        n 4tnmss "No creo que siquiera necesite preguntar,{w=0.1} pero..."
        menu:
            n "¿Qué hay de ti,{w=0.1} [player]?{w=0.2} ¿Juegas a menudo?"
            "¡Absolutamente!":

                $ persistent.jn_player_gaming_frequency = "High"
                n 3fcsbg "¡Sip!{w=0.2} Justo como sospechaba..."
                n 1uchgn "[player] es un mega-nerd."
                n 4uchbselg "¡Ahaha!"
                n 1uchsm "¡Relájate,{w=0.1} [player]!"
                n 3fllssl "No soy mucho mejor,{w=0.1} después de todo."
            "Juego ocasionalmente":

                $ persistent.jn_player_gaming_frequency = "Medium"
                n 1fsqsm "Sí,{w=0.1} sí.{w=0.2} Cree lo que quieras creer,{w=0.1} [player]."
                n 3usqbg "No estoy segura de tragármelo,{w=0.1} sin embargo."
            "No juego para nada":

                $ persistent.jn_player_gaming_frequency = "Low"
                n 4tnmaj "¿Huh?{w=0.2} ¿En serio?"
                n 1tllaj "¿Ni siquiera el raro juego casual?"

                if jn_activity.ACTIVITY_MANAGER.hasPlayerDoneActivity(jn_activity.JNActivities.gaming):
                    n 4fsqts "Mentiroso.{nw}"

                n 1ncsaj "... Bueno entonces."
                n 3fnmbg "¡Parece que tengo mucho que enseñarte,{w=0.1} [player]!"

    elif Natsuki.isDistressed(higher=True):
        n 1nnmsl "¿Huh?{w=0.2} ¿Videojuegos?"
        n 2nslsl "Sí,{w=0.1} supongo.{w=0.2} Por lo que valga para ti."
    else:

        n 1nsqsl "¿Videojuegos...?"
        n 2fsqsltsb "...Heh.{w=0.2} ¿Por qué,{w=0.3} [player]?{w=1}{nw}"
        extend 1fcsantsa " ¿Pisotear todos mis sentimientos no fue suficiente?"
        n 4fsqfultsb "¿O buscabas ver si puedes pisotearme en juegos también?"
        n 1fcsfrltsa "..."
        n 1fcsupl "...No quiero hablar sobre esto más.{w=0.2} {i}Terminamos{/i} aquí."
        return

    if Natsuki.isNormal(higher=True):
        n 1ullaj "Como sea,{w=0.1} poniendo eso de lado..."
        n 4nsgbg "¿Cuando se trata de mis preferencias?{w=0.2} ¡Quiero desafío en mis juegos!"
        n 3fcsbg "Juego para ganar{w=0.1} -{w=0.1} ¡soy yo contra los desarrolladores,{w=0.1} y ellos no están para detenerme!"
        n 3fchbg "Ahaha."
        n 1ullss "De hecho me gustan más mis roguelikes,{w=0.1} para ser honesta."
        n 4fnmsm "Heh.{w=0.2} ¿Estás sorprendido,{w=0.1} [player]?"
        n 3fcsbg "Duros de roer,{w=0.1} y tengo que pensar rápido{w=0.1} -{w=0.1} además es asombrosamente satisfactorio aprender todo también."
        n 1fchsm "¡Y con qué tan aleatorio es todo,{w=0.1} siempre se sienten refrescantes y divertidos de jugar!"
        n 1fnmbg "Cada vez que cargo uno,{w=0.1} no tengo idea de a qué me enfrento...{w=0.3} ¡y eso es lo que los hace adictivos!"
        n 1fcssm "Ehehe.{w=0.2} No te preocupes sin embargo, [player]."
        n 4fcsbg "No sé si te gustan ese tipo de cosas también,{w=0.1} pero..."

        if persistent.jn_player_gaming_frequency == "High":
            n 1fchgn "¡Todavía hay mucho que puedo enseñarte!"

            if Natsuki.isEnamored(higher=True):
                n 3ksqsml "Y apuesto a que te gustaría eso también,{w=0.1} ¿eh?"
                n 1nchbg "Ahaha."

            elif Natsuki.isAffectionate(higher=True):
                n 1fchbg "¡Y no voy a tomar un 'No' por respuesta!"

        elif persistent.jn_player_gaming_frequency == "Medium":
            n 1fsqsm "No me importa mostrarte cómo se hace."
            n 3fchbg "I {i}am{/i} a professional,{w=0.1} after all!"
        else:

            if jn_activity.ACTIVITY_MANAGER.hasPlayerDoneActivity(jn_activity.JNActivities.gaming):
                n 3fsqts "Liar.{nw}"

            n 1ullaj "Bueno entonces...{w=0.5}{nw}"
            extend 4usqsm " Estoy segura de que puedo hacer que {i}tú{/i} de todas las personas entres en ello."
    else:

        n 1nnmsl "I suppose I look for challenge in my games more than anything."
        n 2nllsl "It's fun pitting myself against the developers and beating them at their own game."
        n 1nsqaj "I guess I could say I like being tested -{w=0.1} so long as I'm in control of it,{w=0.1} that is."
        n 2fsqbo "What does that mean?{w=0.2} I guess I'll spell it out for you,{w=0.1} [player]."
        n 4fsqan "I really {i}don't{/i} like the kind of testing you're doing."

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_natsukis_fang",
            unlocked=True,
            prompt="[n_name]'s fang",
            category=["Natsuki"],
            nat_says=True,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_natsukis_fang:
    n 1nllbo "..."
    n 4unmaj "Eh?{w=0.2} ¿Qué pasa,{w=0.1} [player]?"
    n 1unmsl "..."
    n 1tnmaj "¿Qué?{w=0.2} ¿Hay algo en mi cara?"
    n 1tnmca "..."
    n 4uwdaj "Oh.{w=0.2} Sí.{w=0.2} Lo entiendo."
    n 3nsqss "Simplemente no puedes evitar notar el colmillo,{w=0.1} ¿verdad?{w=0.2} Ehehe."
    n 1nllss "Sabes..."
    n 1nnmaj "No siempre estuve feliz con mis dientes,{w=0.1} [player]."
    n 3flran "Solía ser bastante insegura sobre ellos.{w=0.2} La gente simplemente seguía señalándolos todo el tiempo."
    n 1fcsaj "No era...{w=0.3} {i}malo{/i} ni nada...{w=0.3} un poco molesto al principio,{w=0.1} pero nada exagerado."
    n 4kslsf "...Mayormente."
    n 1ulrsl "Pero...{w=0.3} ¿supongo que simplemente llegué a aceptarlos?"
    n 3fchbg "¡Son como una marca registrada o algo así ahora!{w=0.2} Que es por lo que cuido bien de ellos."
    n 1fnmsf "¡Más te vale no estar descuidando los tuyos,{w=0.1} [player]!"
    n 3fnmaj "Y no solo me refiero a saltarte una cepillada ocasional,{w=0.1} tampoco..."
    n 3fsgss "Sí.{w=0.2} Ambos sabemos lo que viene,{w=0.2} ¿no?"
    n 4fsqbg "¿Cuándo fue la última vez que {i}tú{/i} usaste hilo dental,{w=0.1} [player]!"
    n 1tsqsm "..."
    n 1fchbgelg "¡Ahaha!{w=0.2} ¿Te exhibí?"
    n 1nlrss "Bueno,{w=0.1} como sea.{w=0.2} Solo asumiré que irás a hacer eso más tarde."
    n 4fcsaw "Pero en serio.{w=0.2} ¡Más te vale asegurarte de cuidar tus dientes!"
    n 1fnmaj "El cepillado regular y el hilo dental son importantes,{w=0.1} pero vigila tu dieta también."
    n 3fllsl "¡No usar hilo dental no es genial,{w=0.1} pero las bebidas azucaradas constantes son aún peores!"
    n 1fsgsm "Recuerda,{w=0.1} [player] -{w=0.1} si los ignoras,{w=0.1} se irán~."
    n 1nllss "Pero no, en serio."

    if Natsuki.isLove(higher=True):
        $ chosen_endearment = jn_utils.getRandomEndearment()
        n 1kllss "Hacerte sonreír te queda bien,{w=0.1} [chosen_endearment]."
        n 4fnmsm "Mantengámoslos viéndose así."
        n 4uchsml "Ehehe.{w=0.2} ¡Te amo,{w=0.1} [player]~!"

    elif Natsuki.isEnamored(higher=True):
        n 1fnmsml "Creo que las sonrisas te quedan bien,{w=0.1} [player]."
        n 4fchbgl "¡Mantengámoslos viéndose así!"

    elif Natsuki.isAffectionate(higher=True):
        n 1usqbg "La sonrisa correcta puede hacer toda la diferencia,{w=0.1} sabes.{w=0.2} ¡Solo mira la mía!"
        n 3uchgn "Ehehe."
    else:

        n 1unmaj "¿Si no los cuidas?"
        n 3fllajl "¡No voy a sostener tu mano en el dentista!"

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_i_love_you",
            unlocked=True,
            prompt="¡Te amo, {0}!".format(n_name),
            category=["Natsuki", "Romance"],
            player_says=True,
            location="classroom",
            affinity_range=(jn_affinity.ENAMORED, None)
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_i_love_you:

    $ player_initial = jn_utils.getPlayerInitial()
    $ chosen_tease = jn_utils.getRandomTease()
    $ chosen_endearment = jn_utils.getRandomEndearment()
    $ chosen_descriptor = jn_utils.getRandomDescriptor()


    if (
        persistent.affinity >= (jn_affinity.AFF_THRESHOLD_LOVE -1)
        and not persistent._jn_player_confession_accepted
    ):
        n 1uscemf "O-{w=0.1}o-{w=0.1}oh dios mío..."
        n 4uskemf "[player_initial]-{w=0.2}[player]...{w=0.3} ¡t-{w=0.1}tú...!"
        n 2fcsanf "¡Nnnnnnn-!"
        n 1fbkwrf "¡B-{w=0.1}bueno te tomaste tu tiempo!{w=0.2} ¡¿Qué creías que estabas haciendo?!"
        n 4flrwrf "¡Apuesto a que solo estabas esperando a que yo lo dijera primero!"
        n 4fllemf "Cielos,{w=0.1} [player]...{w=0.3} [chosen_tease]..."
        n 1kllemf "Pero..."
        n 2fcswrf "¡P-{w=0.1}pero...!"
        n 1flranf "¡Uuuuuuu-!"
        n 1fchwrf "¡Oh,{w=0.1} lo que sea!{w=0.2} ¡No me importa!{w=0.2} ¡Tengo que decirlo!{w=0.2} ¡Tengo que decirlo!"
        n 4kwdemf "¡[player]!{w=0.2} ¡Yo también te amo!"
        n 4kchbsf "Y-{w=0.1}yo te amo...{w=0.3} también..."
        n 4kplbgf "Yo...{w=0.3} Yo..."
        n 1fcsunfsbl "..."

        show natsuki 1kcspuf zorder JN_NATSUKI_ZORDER at jn_center
        show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
        play audio clothing_ruffle
        $ jnPause(3.5)
        play audio kiss
        show natsuki 1ksrsmfsbr zorder JN_NATSUKI_ZORDER at jn_center
        $ jnPause(1.5)
        hide black with Dissolve(1.25)

        n 1kchsmf "..."
        n 3kwmsmf "Te amo,{w=0.3} [player]..."
        n 3kllsml "..."
        n 1kskemf "¡L-{w=0.1}lamento eso...!"
        n 4klrunf "Creo...{w=0.3} que me dejé llevar un poco..."
        n 1kcssmf "..."
        n 1knmajf "..."
        n 2kbkemf "¡C-{w=0.1}cielos!{w=0.2} ¡Deja de mirarme así de una vez!"
        n 4fllemf "A-{w=0.1}ambos estamos en la misma sintonía ahora,{w=0.1} así que..."
        n 4kllbof "...{w=0.3}E-eso es todo lo que tenía."
        n 1kllsmf "..."
        n 1kllssf "A-{w=0.1}así que..."
        n 3kplssf "¿En qué estábamos?{w=0.2} Ehehe..."

        python:
            import datetime

            persistent._jn_player_confession_accepted = True
            persistent._jn_player_confession_day_month = (
                datetime.date.today().day,
                datetime.date.today().month
            )
            persistent.jn_player_love_you_count += 1
            Natsuki.percentageAffinityGain(10)
        return


    elif persistent.jn_player_love_you_count == 0 and not persistent._jn_player_confession_accepted:
        if Natsuki.isEnamored():
            n 1uscgsf "[player_initial]-{w=0.2}[player]!"
            n 2fskgsf "¡T-{w=0.1}tú...!"
            n 1fcsanf "¡Nnnnn-!"
            n 1fbkwrf "¡S-{w=0.1}sé que nos hemos estado viendo un tiempo,{w=0.1} pero esto es demasiado repentino!"
            n 3fllwrf "¡Ahora has ido y lo has hecho súper incómodo,{w=0.1} [player]!{w=0.2} ¡¿Por qué tuviste que ir a hacer eso?!"
            n 1fcsemf "¡Caray!"
            n 2fslpof "...Espero que estés feliz."
            n 1fsqunf "..."
            n 4fnmpof "P-{w=0.1}pero no creas que esto significa que te {i}odie{/i} o algo así..."
            n 2flreml "Es solo que...{w=0.3} Es solo..."
            n 1fcsanl "Uuuuuu..."
            n 1flrbol "O-{w=0.1}olvídalo..."
            n 4fcseml "Olvida que dije algo."
            n 1kllbof "..."
            $ Natsuki.calculatedAffinityGain(base=2, bypass=True)

        elif Natsuki.isAffectionate(higher=True):
            n 1uskwrf "¿Q-{w=0.1}q-{w=0.1}qué?"
            n 4fwdwrf "¿A-{w=0.1}acabas de...?"
            n 1fcsanf "¡Nnnnnnnnn-!"
            n 1fbkwrf "[player_initial]-{w=0.2}[player]!"
            n 3fcsemf "¡¿Estás tratando de darme un ataque al corazón?!{w=0.2} ¡Cielos!"
            n 3fllemf "Simplemente no puedes decir cosas así tan de repente..."
            n 1kllunf "..."
            n 4fllajf "D-{w=0.1}digo..."
            n 1flranf "No es que {i}no{/i} me gustes,{w=0.1} o-{w=0.1}o nada,{w=0.1} pero..."
            n 3fslanf "¡Pero...!"
            n 1fcsanf "Uuuuu..."
            n 1fcsajf "¡O-{w=0.1}olvídalo!{w=0.2} N-{w=0.1}no es nada..."
            n 1kslslf "..."
            $ Natsuki.calculatedAffinityGain(bypass=True)

        elif Natsuki.isHappy(higher=True):
            n 4fsqdvlesm "¡Pffffft!"
            n 1uchbslelg "¡Ahaha!"
            n 1tllbgl "¡No puedes hablar en serio,{w=0.1} [player]!{w=0.2} ¡Solo me estás tomando el pelo!{w=0.2} ¿Verdad?"
            n 3knmbgl "¿Verdad,{w=0.1} [player]?"
            n 4knmajf "¿V-{w=0.1}verdad...?"
            n 1fllunf "..."
            n 1fcsgsf "¡C-{w=0.1}cielos!{w=0.2} ¡Suficiente de esto!"
            n 3fsqajf "¡Realmente no deberías jugar con chicas así,{w=0.1} [player]!"
            n 3fslpul "T-{w=0.1}tienes suerte de que tenga un gran sentido del humor."
            n 4fnmpol "A-{w=0.1}así que está bien...{w=0.3} esta vez..."
            n 1fcsajl "¡Solo...{w=0.3} piensa un poco antes de soltar cosas así sin más!{w=0.2} Caray."
            $ capitalized_tease = chosen_tease.capitalize()
            n 1fllslf "[capitalized_tease]..."

        elif Natsuki.isNormal(higher=True):
            n 1fscgsf "¡Urk-!"
            n 4fskanf "Q-{w=0.1}qué acabas de..."
            n 1fwdanf "¿Acaso tú...?"
            n 1fllajl "..."
            n 3fcsbgf "¡A-{w=0.1}aha!{w=0.2} Digo...{w=0.3} ¡s-{w=0.1}sí!{w=0.2} ¿Quién no me amaría,{w=0.1} verdad?"
            n 3fllbgf "Mi ingenio,{w=0.1} mi estilo,{w=0.1} mi sentido del humor matador...{w=0.3} lo tengo todo.{w=0.1} Sí..."
            n 1fbkwrf "¡N-{w=0.1}no te hagas ideas equivocadas o a-{w=0.1}algo así, sin embargo!"
            n 1fllssf "D-{w=0.1}digo,{w=0.1} solo me alegra que tengas buen gusto."
            n 2fllunf "Sí..."

        elif Natsuki.isUpset(higher=True):
            n 1fcsan "..."
            n 4fnmfu "¿En serio,{w=0.1} [player]?{w=0.2} ¿Realmente vas a decirme eso {i}ahora{/i}?"
            n 1fsqfutsb "¿La primera vez que eliges decirlo...{w=0.3} y lo dices {i}ahora{/i}?"
            n 1fcspu "..."
            n 1fwman "¿Y realmente crees que voy a tragarme eso {i}ahora{/i},{w=0.1} [player]?"
            n 4fcsfu "..."
            n 1fcssr "..."
            n 2fsqsr "Terminamos con esto."
            n 1fsqpu "¿Y si {i}realmente{/i} te sientes así?"
            n 2fsqsftsb "...Entonces ¿por qué no estás {i}tú{/i} tratando de hacer que esto funcione,{w=0.1} [player]?"
            $ Natsuki.percentageAffinityLoss(10)
        else:


            n 1fsqputsb "..."
            n 2fcsuntsa "T-{w=0.1}tú..."
            n 1fcsantsa "Tú...{w=0.3} ¡c-{w=0.1}cómo...!"
            n 4fscwr "¡C-{w=0.1}cómo te {i}atreves{/i} a decirme eso ahora!"
            n 1fscfu "{i}Cómo {w=0.3} te {w=0.3} atreves.{/i}"
            n 1fcsfu "..."
            n 1fcssr "..."
            n 1fsqsr "Sabías como me sentía,{w=0.1} [player]..."
            n 2fcsan "Lo sabías por tanto tiempo..."
            n 1fsqfutsb "¿Y ahora?{w=0.2} ¿{i}Ahora{/i} es cuando me lo dices?"
            n 4fsquptse "¿Por la {i}primera vez{/i}?"
            n 1fcsuptsa "..."
            n 1kplan "Yo...{w=0.3} Yo n-{w=0.1}no puedo hacer esto ahora mismo."
            n 2kcsantsd "Es...{w=0.5} duele..."
            n 1kcsfutsd "..."
            n 4fcsputsd "Fuera de mi vista,{w=0.1} [player]."
            n 1fcsantsd "..."
            n 1fsqfutse "¡Vete!"
            n 4fscsctdc "{i}¡SOLO DÉJAME EN PAZ!{/i}{nw}"

            $ Natsuki.percentageAffinityLoss(25)
            $ Natsuki.setForceQuitAttempt(False)
            $ persistent.jn_player_love_you_count += 1

            return { "quit": None }

        $ persistent.jn_player_love_you_count += 1
    else:


        $ persistent.jn_player_love_you_count += 1
        if Natsuki.isLove(higher=True):


            $ random_response_index = random.randint(0, 11)

            if random_response_index == 0:
                n 4unmbgf "Ehehe.{w=0.2} ¡Yo también te amo,{w=0.1} [chosen_endearment]!"
                n 3uchsmf "Siempre eres [chosen_descriptor] para mí."
                $ Natsuki.calculatedAffinityGain()
                return

            elif random_response_index == 1:
                n 1tsqssl "Aww,{w=0.1} ¿no me digas?"
                n 3uchbslelg "¡Ahaha!"
                $ chosen_endearment = chosen_endearment.capitalize()
                n 1kwmbgf "[chosen_endearment],{w=0.1} ¡yo también te amo!"
                n 4fcsbgf "Siempre estaré aquí para apoyarte."
                $ Natsuki.calculatedAffinityGain()
                return

            elif random_response_index == 2:
                n 1uchsmf "¡Aww,{w=0.1} [chosen_endearment]!{w=0.2} ¡Yo también te amo!"
                n 4klrbgf "Eres la mejor cosa que me ha pasado."
                $ Natsuki.calculatedAffinityGain()
                return

            elif random_response_index == 3:
                n 1ksqbgf "¿Oh?{w=0.2} Alguien está todo necesitado hoy,{w=0.1} ¿eh?"
                n 4fsqsmf "Bueno,{w=0.1} ¡estaría feliz de complacerte!"
                n 1uchsmf "¡Yo también te amo,{w=0.1} [chosen_endearment]!"
                n 3fchbgf "Sigue sonriendo para mí,{w=0.1} ¿okay?"
                $ Natsuki.calculatedAffinityGain()
                return

            elif random_response_index == 4:
                n 3flrpof "¿Adulándome como siempre,{w=0.1} [player]?"
                n 1usqssf "Ehehe.{w=0.2} No te preocupes,{w=0.1} ¡no me estoy quejando!"
                n 4uchbgf "¡Yo también te amo,{w=0.1} [chosen_endearment]!"
                n 3fcssmf "¡Solo somos nosotros dos contra el mundo!"
                $ Natsuki.calculatedAffinityGain()
                return

            elif random_response_index == 5:
                n 1fllbgf "Bueno,{w=0.1} p-{w=0.1}por supuesto que sí.{w=0.2} ¡Ahaha!"
                n 4fchbgf "Pero...{w=0.3} ambos sabemos que yo te amo más,{w=0.1} [player]."
                menu:
                    "No, yo te amo más":
                        n 1fnmbgf "No,{w=0.1} Yo-"
                        n 1tllajl "..."
                        n 4fnmawl "¡O-{w=0.1}oye...{w=0.3} espera un minuto...!"
                        n 1fchgnl "¡Sé a dónde vamos con esto!{w=0.2} ¡Buen intento,{w=0.1} [player]!"
                        n 1fsqsml "Solo vas a tener que aceptar que yo te amo más,{w=0.1} y así es como es."
                        menu:
                            "Tú me amas más, y así es como es.":
                                n 1uchgnf "Ehehe.{w=0.2} ¿Ves?"
                                n 3fwmsmf "Eso no fue tan difícil,{w=0.1} ¿o sí?"
                                n 1nchbgf "¡Te aaaamo,{w=0.1} [player]~!"
                    "Está bien":

                        n 1uchgnlesm "¡Pffffft!{w=0.2} ¡Ahaha!"
                        n 3fwltsf "¡Vamos,{w=0.1} [player]!{w=0.2} ¿Dónde está tu espíritu de lucha?"
                        n 1fchsmf "Bueno,{w=0.1} como sea.{w=0.2} Solo me alegra que aceptes la verdad."
                        n 4uchsmf "Ehehe."

                $ Natsuki.calculatedAffinityGain()
                return

            elif random_response_index == 6:
                n 1uchsmf "Ehehe...{w=0.3} Siempre adoro escuchar eso de ti,{w=0.1} [player]."
                n 1usqsmf "...Y creo que puedo adivinar que te gusta escucharlo igual."
                n 3uchbgf "¡Yo también te amo,{w=0.1} [chosen_endearment]!"
                n 4nchsmf "No necesito a nadie más~."
                $ Natsuki.calculatedAffinityGain()
                return

            elif random_response_index == 7:
                n 1nsqajl "Wow,{w=0.1} [player]..."
                n 3tslajl "Realmente eres un gran desastre cursi hoy,{w=0.1} ¿no es así?"
                n 3tsldvl "Que asco..."
                n 1fchbgf "...Pero justo el tipo de asco con el que estoy bien.{w=0.2} Ehehe."
                n 4uchbgf "¡Yo también te amo,{w=0.1} [chosen_endearment]!"
                n 1unmsmf "Siempre cubriré tu espalda."
                $ Natsuki.calculatedAffinityGain()
                return

            elif random_response_index == 8:
                n 1uchsmf "Ehehe."
                n 1nchssf "Yo..."
                n 3uchbsf "¡Te aaaaaaaamo también,{w=0.1} [player]!"
                n 4kwmsmf "Siempre serás mi roca."
                $ Natsuki.calculatedAffinityGain()
                return

            elif random_response_index == 9:
                n 1fllsmf "Digo...{w=0.3} eso es muy dulce de tu parte y todo,{w=0.1} [player]..."
                n 4fsqsmf "Pero ambos sabemos que yo te amo más~."
                $ player_is_wrong = True
                $ wrong_response_count = 0


                while player_is_wrong:
                    menu:
                        "¡No, yo te amo {i}más{/i}!":

                            if wrong_response_count == 1:
                                n 1fsqbgl "¿Hmm?{w=0.2} ¿Me escuchaste mal,{w=0.1} [player]?"
                                n 4fchbgf "¡Dije que yo te amo {i}más{/i},{w=0.2} [chosen_tease]!"

                            elif wrong_response_count == 5:
                                n 1fsqbgl "¿Oh?{w=0.2} Competitivos,{w=0.1} ¿lo somos?"
                                n 3fslbgl "Ehehe.{w=0.2} Tontito [player].{w=0.1} ¿Nadie te dijo nunca?"
                                n 3fchgnl "¡No empieces una pelea que no puedes terminar!"
                                n 1fchbgf "Especialmente esta -{w=0.1} ¡Yo te amo {i}más{/i}~!"

                            elif wrong_response_count == 10:
                                n 3tsqcsl "¿Oho?{w=0.2} ¡Nada mal,{w=0.1} [player]!"
                                n 1fsqbgl "Casi admiro tu terquedad..."
                                n 4uchsmf "¡Pero no tanto como te admiro a ti!{w=0.2} ¡Yo te amo {i}más{/i}!"

                            elif wrong_response_count == 20:
                                n 3fsqbgl "Ehehe.{w=0.2} ¡Eres persistente!{w=0.2} Te daré eso."
                                n 1fsqsml "Pero si crees que te voy a dar una victoria..."
                                n 1fchgnl "¡Entonces tienes otra cosa viniendo!"
                                n 4uchbgl "¡Yo te amo {i}más{/i},{w=0.1} tontito!"

                            elif wrong_response_count == 50:
                                n 1tnmajl "¡Wow!{w=0.2} Esta es como...{w=0.3} ¡la 50va vez que te equivocas!{w=0.2} ¡Seguidas!"
                                n 3tsqsgl "Me suena a que estás en una seria negación ahí,{w=0.1} [player]~."
                                n 1nllssl "No creo que pueda molestarme en contar mucho más desde aquí..."
                                n 3fsqtsl "Así que ¿por qué no me haces un favor y solo aceptas que yo te amo {i}más{/i} ya?"
                                n 1uchsml "Ehehe."
                                n 4fchbgl "¡Gracias,{w=0.1} [chosen_endearment]~!"

                            elif wrong_response_count == 100:
                                n 4uwdgsl "...¡Oh!{w=0.2} ¡Y parece que tenemos nuestra 100va respuesta equivocada!"
                                n 3fllawl "¡Bajen las luces!{w=0.2} ¡Corran la música!"
                                n 1flrbgl "Ahora,{w=0.1} miembros de la audiencia -{w=0.1} ¿qué obtiene nuestro participante obstinado?"
                                n 1fsqbgl "Ellos obtienen..."
                                n 3uchgnl "¡Una corrección!{w=0.2} ¡Wow!"
                                n 4fsqbgl "Y esa corrección es..."
                                n 1fchbsf "¡[n_name] los ama {i}a ellos{/i} mucho más!{w=0.2} ¡Felicidades,{w=0.1} tontito!"
                                n 3fsqdvl "Y ahora,{w=0.1} para irse con el gran premio -{w=0.1} todo lo que nuestro invitado aquí necesita hacer..."
                                n 1fchbsl "...¡Es rendirse y admitir qué tan equivocados están~!{w=0.2} Ehehe."
                            else:

                                $ player_is_wrong_responses = [
                                    "¡Nop!{w=0.2} ¡Yo te amo {i}más{/i}!",
                                    "¡Lo siento,{w=0.1} bub!{w=0.2} ¡Definitivamente te amo {i}más{/i}!",
                                    "Ehehe.{w=0.2} ¡Nop~!{w=0.2} Ambos sabemos que te amo {i}más{/i}.",
                                    "Hmm...{w=0.3} ña.{w=0.2} ¡Bastante segura de que te amo {i}más{/i}!",
                                    "¡Nooooop~!{w=0.2} ¡Yo te amo {i}más{/i}!",
                                    "Tontito [player]~.{w=0.2} Te amo {i}más{/i},{w=0.1} ¿recuerdas?",
                                    "Mmmmmmmm...{w=0.3} ¡nop!{w=0.2} ¡Te amo {i}mucho{/i} más,{w=0.1} [player]~!",
                                    "Vamos vamos ahora,{w=0.1} [player].{w=0.2}  ¡No seas tonto!{w=0.2} Definitivamente te amo {i}más{/i}.",
                                    "Espera...{w=0.3} ¿puedes oír eso?{w=0.2} ¡Oh!{w=0.2} Es qué tan equivocado estás -{w=0.1} ¡te amo más,{w=0.1} tontito!",
                                    "Solo estás perdiendo tu tiempo,{w=0.1} [player]~.{w=0.2} ¡Te amo {i}muuucho{/i} más!",
                                    "Vaya,{w=0.1} oh vaya,{w=0.1} [player].{w=0.2} ¿No sabes que te amo {i}más{/i} para ahora?{w=0.2} Ehehe.",
                                    "Ajá...{w=0.3} Nat te oye,{w=0.1} Nat sabe que estás equivocado.{w=0.1} Te amo {i}más{/i},{w=0.1} ¡bobo!",
                                    "Eres adorable cuando estás en negación,{w=0.1} [player].{w=0.2} Ehehe.{w=0.2} ¡Te amo {i}más{/i}~!",
                                    "Aww,{w=0.1} vamos ya,{w=0.1} [player].{w=0.2} Si {i}realmente{/i} me amaras,{w=0.2} ¡admitirías que yo te amo {i}más{/i}!"
                                ]
                                $ chosen_random_response = renpy.substitute(random.choice(player_is_wrong_responses))
                                n 1fchbgf "[chosen_random_response]"

                            $ wrong_response_count += 1
                        "Está bien, bien. Tú me amas más":

                            $ player_is_wrong = False
                            n 3tsqbgl "¿Ves?{w=0.2} ¿Fue eso realmente tan difícil?"
                            n 1uchtsl "A veces solo tienes que admitir que estás equivocado,{w=0.1} [player]~."
                            n 4nchsml "Ehehe."

                            if wrong_response_count >= 10:
                                n 3nsqsml "¡Buen intento,{w=0.1} sin embargo~!"

                            $ Natsuki.calculatedAffinityGain()
                            return

            elif random_response_index == 10:
                n 1ksqsml "Ehehe.{w=0.2} Nunca me cansaré de escuchar eso de ti,{w=0.1} [player]."
                n 1uchsmf "¡Yo también te amo!"
                n 3uchbgf "Eres mi número uno~."
                $ Natsuki.calculatedAffinityGain()
                return
            else:

                n 4usqbgf "¿Oh?{w=0.2} ¿Romántico como de costumbre?"
                n 1uslsmf "Eres tan sentimental,{w=0.1} [player].{w=0.2} Ehehe."
                n 3uchbgf "Pero...{w=0.3} ¡no me voy a quejar!{w=0.2} ¡Yo también te amo,{w=0.1} [chosen_endearment]!"
                n 1uchsmf "Siempre me haces sentir alta."
                $ Natsuki.calculatedAffinityGain()
                return

            return

        elif Natsuki.isEnamored(higher=True):
            n 1fbkwrf "¡G-{w=0.1}gah!{w=0.2} ¡[player]!"
            n 3fllwrf "¿Qué dije sobre hacer las cosas incómodas?{w=0.2} ¡Ahora es el doble de incómodo!"
            n 1fcsemf "Caray..."
            n 1flremf "Solo hablemos de algo,{w=0.1} ¿de acuerdo?"
            n 4flrpof "¡P-{w=0.1}puedes adularme en tu {i}propio{/i} tiempo!"
            n 4klrpof "Tonto..."
            $ Natsuki.calculatedAffinityGain()
            return

        elif Natsuki.isHappy(higher=True):
            n 1fskemf "¡H-{w=0.1}hey! ¡Pensé que te dije que no salieras con cosas como esas!"
            n 2fllemf "Caray..."
            n 1fcsemf "N-{w=0.1}no sé si estás tratando de ganarme,{w=0.1} o qué..."
            n 2fcspof "¡Pero vas a tener que esforzarte mucho más que eso!"
            return

        elif Natsuki.isNormal(higher=True):
            n 1fskemf "¡G-{w=0.1}gah!"
            n 4fbkwrf "[player_initial]-{w=0.1}[player]!"
            n 1fnmanl "¡Deja de ser asqueroso!"
            n 2fcsanl "Caray..."
            n 1fllajl "No sé si crees que esto es una broma,{w=0.1} o qué..."
            n 2fsqaj "Pero realmente no es gracioso para mí,{w=0.1} [player]."
            return

        elif Natsuki.isUpset(higher=True):
            n 1fcssr "..."
            n 1fsqsr "Hablar es barato,{w=0.1} [player]."
            n 1fsqaj "Si {i}realmente{/i} te importo..."
            n 2fsqpu "Entonces {i}pruébalo{/i}."
            $ Natsuki.percentageAffinityLoss(2.5)
            return
        else:

            n 1fsqpu "..."
            n 1fsqan "Eres realmente increíble,{w=0.1} [player]."
            n 2fsqfu "¿Siquiera {i}entiendes{/i} lo que estás diciendo?"
            n 1fcsfu "..."
            n 1fcspu "¿Sabes qué?{w=0.2} Lo que sea.{w=0.2} Ya no me importa."
            n 4fsqfu "Di lo que quieras,{w=0.1} [player].{w=0.2} Es todo basura,{w=0.1} justo como todo lo demás de ti."
            $ Natsuki.percentageAffinityLoss(2)
            return

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_natsukis_hairstyle",
            unlocked=True,
            prompt="¿Por qué te peinas así?",
            category=["Moda"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_natsukis_hairstyle:
    if Natsuki.isEnamored(higher=True):
        n 4tnmaj "¿Hmm?{w=0.2} ¿Mi peinado?"
        n 3fsqss "¿Por qué preguntas,{w=0.1} [player]?{w=0.5}{nw}"
        extend 3fsgsg " ¿Buscas un estilista?"
        n 1fchsm "Ehehe."

    elif Natsuki.isNormal(higher=True):
        n 4tnmpu "¿Huh?{w=0.2} ¿Mi peinado?"
        n 1fsqaj "Espera...{w=0.75}{nw}"
        extend 4fnmeml " ¿m-{w=0.1}me estás tomando el pelo?{w=0.2} ¿A qué te refieres?"
        n 3fslpo "Más te vale no estar burlándote de mí,{w=0.1} [player]..."

    elif Natsuki.isDistressed(higher=True):
        n 1nnmsl "...¿Huh?{w=0.2} Oh.{w=0.2} Mi cabello."
        n 2flrsl "Estoy...{w=0.3} sorprendida de que te importe lo suficiente para preguntar sobre eso."
    else:

        n 1fsqfu "Porque me {i}gusta{/i} así.{w=0.75}{nw}"
        extend 2fnman " ¿Es eso suficientemente bueno para ti,{w=0.3} {i}[player]{/i}?"
        n 1fsqantsb "¿Y por qué siquiera te {i}importaría{/i} de todos modos?{w=1}{nw}"
        extend 4fsqupltsb " No te has preocupado por mí hasta ahora."
        n 2fcsanltsa "Idiota."
        return

    n 1nnmpu "Bueno,{w=0.1} como sea."
    n 4ullpu "Nunca pensé realmente mucho en ello,{w=0.1} honestamente."

    if Natsuki.isNormal(higher=True):
        if Natsuki.isWearingHairstyle("jn_hair_twintails") or Natsuki.isWearingHairstyle("jn_hair_twintails_long") or Natsuki.isWearingHairstyle("jn_hair_twintails_white_ribbons"):
            n 2ulrpo "Solo pensé que las coletas se verían algo lindas en mí."
        else:

            n 2ulrpo "Creo que este peinado se ve algo lindo en mí."

        n 4fsqpo "...Sí,{w=0.1} sí.{w=0.2} Sé lo que estás pensando,{w=0.1} [player]."

        if Natsuki.isEnamored(higher=True):
            n 1ksqsm "¿Me equivoqué...?"
            n 1fchbg "Ehehe.{w=0.2} Creí que no."

        if Natsuki.isWearingHairstyle("jn_hair_twintails") or Natsuki.isWearingHairstyle("jn_hair_twintails_long") or Natsuki.isWearingHairstyle("jn_hair_twintails_white_ribbons"):
            n 1ullaj "Además,{w=0.1} tenía un montón de cintas tiradas por ahí de mis cosas de manualidades {w=0.1}-{w=0.5}{nw}"
            extend 3fcsbg " así que no es como si tuviera que ir a {i}comprar{/i} nada nuevo para probar las coletas."
    else:

        if Natsuki.isWearingHairstyle("jn_hair_twintails") or Natsuki.isWearingHairstyle("jn_hair_twintails_long") or Natsuki.isWearingHairstyle("jn_hair_twintails_white_ribbons"):
            n 1nnmsl "Supongo que simplemente me gustó la idea de las coletas."
            n 1nlrpu "Además,{w=0.1} tenía algunas cintas de repuesto tiradas por ahí de todos modos.{w=0.5}{nw}"
            extend 4nsrsr " No es como si tuviera que {i}comprar{/i} nada para probar hacer coletas."
        else:

            n 1nnmsl "Supongo que simplemente me gusta este peinado."

    n 1ulraj "En cuanto al flequillo,{w=0.1} yo...{w=0.3} siempre encontré difícil cortarme el cabello."

    if Natsuki.isNormal(higher=True):
        n 4flraj "Simplemente cuesta demasiado,{w=0.1} ¿sabes?{w=0.2} ¡Es súper tonto!"
        n 1fnman "Como...{w=0.3} ¡no lo entiendo para nada!"
        n 3fllan "Y lo molesto es que si fuera un chico,{w=0.1} ¡sería {i}mucho{/i} más barato!{w=0.5}{nw}"
        extend 1fbkwrean " ¡¿Qué pasa con eso?!"
        n 1fcspuesi "Ugh...{w=1}{nw}"
        extend 2nsrpo " pero sí."
    else:

        n 1nlrsl "Siempre me quedaba algo corta cuando se trataba de cortarlo."
        n 1fsqsl "...Y no,{w=0.1} {i}no{/i} en el sentido físico."

    if Natsuki.isWearingAccessory(jn_outfits.getWearable("jn_accessory_hairband_red")):
        n 4ullaj "¿En cuanto a mi banda?{w=0.2} Es solo para mantener mi cabello fuera de mis ojos."
    else:

        n 4ullaj "No la estoy usando ahora,{w=0.1} pero mi vieja banda era solo para mantener mi cabello fuera de mis ojos."

    if Natsuki.isNormal(higher=True):
        n 3fllss "Verse bien es un bono,{w=0.1} pero mayormente me cansé de cepillar mi cabello fuera de mi cara."
        n 1nsrca "¡Especialmente con ese flequillo!"
        n 1unmaj "Como sea..."

    n 4tllaj "¿He pensado en otros peinados?{w=0.2} Bueno..."

    if not Natsuki.isWearingHairstyle("jn_hair_twintails") or Natsuki.isWearingHairstyle("jn_hair_twintails_white_ribbons"):
        if Natsuki.isEnamored(higher=True):
            n 1tsqsml "¿No es eso lo que estoy haciendo justo ahora?"
            extend 1fchsml " Ehehe."

        elif Natsuki.isNormal(higher=True):
            n 1ullbo "Creo que eso habla por sí mismo,{w=0.1} realmente.{w=0.2} {i}Estoy{/i} probando uno diferente..."
        else:

            n 2nsqsl "...Imagínate,{w=0.1} [player]."
    else:

        if Natsuki.isEnamored(higher=True):
            $ chosen_tease = jn_utils.getRandomTease()
            n 1fcssml "Estoy bastante segura de que ya me solté el cabello contigo,{w=0.1} [chosen_tease].{w=0.2} Eso califica, ¿verdad?"
            n 3uchgnlelg "¡Ahaha!"

        elif Natsuki.isNormal(higher=True):
            n 1unmaj "Ya sabes lo que dicen,{w=0.1} [player]."
            n 3fnmbg "¡Si no está roto,{w=0.1} no lo arregles!"
            n 1uchgn "Ehehe."
        else:

            n 2fslaj "...¿A este punto,{w=0.1} [player]?{w=0.2} Preferiría que no te metieras en mis enredos."
            n 1fsqbo "Gracias."

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_integrity",
            unlocked=True,
            prompt="Tener integridad",
            category=["Sociedad", "Tú"],
            nat_says=True,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_integrity:
    n 4ullaj "Sabes,{w=0.1} [player]..."
    n 1nnmaj "Siento que hoy en día,{w=0.1} todos están tratando de probar un punto,{w=0.1} o predicar algo."
    n 2flrem "Especialmente con redes sociales y todo eso en todas partes -{w=0.1} ¡es una locura!"
    n 2fllem "Como...{w=0.3} hay publicaciones diciéndote que esto es malo,{w=0.1} otras preguntando por qué no apoyas algo más..."
    n 1fcsan "Y por supuesto,{w=0.1} {i}todos{/i} están sintonizados en eso -{w=0.1} ¡así que se filtra a la vida real también!"
    n 1flrsl "Ugh...{w=0.3} no puedo ser solo yo la que encuentra todo eso agotador,{w=0.1} ¿verdad?"
    n 1unmaj "Creo que lo hace algo fácil perder el rastro de lo que realmente te gusta,{w=0.1} o lo que defiendes."
    n 4ullaj "Lo cual...{w=0.3} es de hecho algo de lo que realmente quería hablar contigo,{w=0.1} [player]."
    n 1fllpu "No estoy diciendo que debas solo ignorar a todos los demás,{w=0.1} o nunca considerar otros puntos de vista."
    n 3fnmpo "Eso es solo ser ignorante."
    n 1knmaj "Pero...{w=0.3} no dejes que las opiniones o concepciones de otras personas sobrescriban completamente las tuyas,{w=0.1} ¿okay?"
    n 4fnmbo "Al menos no sin una pelea."
    n 1fnmpu "{i}Tú{/i} eres tu propio maestro,{w=0.1} [player] -{w=0.1} tienes tus propias opiniones,{w=0.1} tus propios valores:{w=0.1} ¡y eso es súper importante!"
    n 1fcsbg "Digo,{w=0.1} ¡mírame a mí!"
    n 1fllaj "¿Y qué si alguien dice que lo que me gusta apesta?{w=0.2} ¿O si debería estar siguiendo algo más popular?"
    n 1fnmsf "No le está haciendo daño a nadie,{w=0.1} así que ¿quiénes son ellos para juzgar y decirme que debería estar disfrutando?"
    n 3fcsbg "Es mi vida,{w=0.1} ¡así que pueden largarse!"
    n 1nnmsr "Como sea...{w=0.3} supongo que lo que estoy diciendo es que no tengas miedo de defender lo que te importa,{w=0.1} [player]."
    n 1fcsaj "Va a haber veces que estarás equivocado,{w=0.1} ¡pero no dejes que te afecte!"
    n 1flrsl "Simplemente no me gusta la idea de que la gente sea empujada a lo que no es correcto para ellos."
    n 4nnmpu "Dicho eso,{w=0.1} [player]..."

    if Natsuki.isEnamored(higher=True):
        n 1ksqsm "Estoy bastante segura de que ambos sabemos qué es lo correcto para el otro ahora,{w=0.1} ¿huh?"
        n 3fcsbglesssbl "Ahaha."

        if Natsuki.isLove(higher=True):
            n 4uchsml "¡Te amo,{w=0.1} [player]~!"

    elif Natsuki.isAffectionate(higher=True):
        n 1ksqsm "Estoy bastante segura de que sé lo que es correcto para ti..."
        n 3fcsbgledz "¡Pasar más tiempo conmigo!"
        extend 4nchgnedz " Ehehe."
    else:

        n 1unmss "Estoy segura de que puedo ayudarte a encontrar lo que es correcto para ti."
        n 1fllss "Para eso son los amigos,{w=0.1} ¿verdad?"
        n 3fcsbg "¡{i}Especialmente{/i} unas como yo!{w=0.5}{nw}"
        extend 4nchgnedz " Ehehe."

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_favourite_animal",
            unlocked=True,
            prompt="¿Cuál es tu animal favorito?",
            category=["Animales", "Naturaleza"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_favourite_animal:
    if Natsuki.isNormal(higher=True):
        n 1fsqsr "Hamstercitos."
        n 3fcssm "Esa es apenas una pregunta para mí,{w=0.1} [player]."
        n 1uwdaj "Como...{w=0.3} si los has visto,{w=0.1} ¿puedes culparme?"
        n 1fcspu "Son...{w=0.5}{nw}"
        n 4fspgsedz "¡¡{i}Adorables{/i}!!"
        n 1fbkbsl "Simplemente amo todo sobre ellos...{w=0.3} las patitas,{w=0.1} los ojos brillantes, esas mejillas hinchadas..."
        n 4fspbgl "Y esa pequeña colita...{w=0.3} ¡oh Dios mío!{w=0.2} ¡Es simplemente precioso!"
        n 2fllan "Realmente me revienta cuando la gente los llama aburridos,{w=0.1} o poco cariñosos sin embargo.{w=0.2} Como...{w=0.3} ¿Alguna vez has observado uno?"
        n 1fnmaj "Todos tienen sus propias pequeñas personalidades,{w=0.1} justo como cualquier otro animal -{w=0.1} ¡solo que más pequeños!"
        n 1uwdaj "Y si creas un vínculo con ellos,{w=0.1} no tienen miedo de mostrarlo -{w=0.1} He visto videos de ellos siguiendo a sus dueños,{w=0.1} ¡e incluso saltando a sus manos!"
        n 4fchbg "Además son fáciles de cuidar,{w=0.1} ¡también!"
        n 1fchsm "Solo rellena su comida y cambia su agua diariamente,{w=0.1} y limpia su jaula una vez a la semana -{w=0.1} sin sudar."
        n 4nllpu "Hmm..."
        n 1unmpu "Sabes,{w=0.1} [player]...{w=0.3} se pone un poco tranquilo cuando no estás cerca,{w=0.1} si sabes a lo que quiero llegar..."
        n 3fnmsm "Quizás un día podamos tener nuestro propio amigo peludo aquí también?{w=0.1} Ehehe."
        n 1fllss "No te preocupes sin embargo,{w=0.1} [player]..."
        n 1ucssm "No me importa cuidarlo."
        n 3fchgn "...¡Pero tú estás a cargo de los suministros!"

        if Natsuki.isEnamored(higher=True):
            n 1fchbg "Oh,{w=0.1} y relájate -{w=0.1} ¡Me aseguraré de que esté bien domado!"
            n 1uslbg "O..."
            n 3usqts "Al menos casi tan dócil como tú,{w=0.1} ¿eh [player]?{w=0.2} ¡Ahaha!"

            if Natsuki.isLove(higher=True):
                n 4uchbg "¡Te amo~!"

    elif Natsuki.isDistressed(higher=True):
        n 1fsqpu "Hámsters,{w=0.1} si importa."
        n 2fllpu "¿Por qué?{w=0.2} No sé.{w=0.2} Solo creo que son lindos."
        n 1nllbo "Creo que la gente realmente subestima cuán expresivos pueden ser,{w=0.1} también."
        n 1nnmbo "Son como la mayoría de los animales realmente -{w=0.1} todos tienen sus propias personalidades."
        n 1nnmaj "Supongo que son bastante fáciles de cuidar también,{w=0.1} así que esta eso."
        n 1nlrsl "..."
        n 2flrsl "...Estaría mintiendo si dijera que no he estado pensando en tener uno yo misma..."
        n 1fsqpu "Pero honestamente,{w=0.1} [player]?{w=0.2} ¿Si has demostrado que no puedes cuidar de {i}mí{/i}?"
        n 2fcsan "...Entonces no creo que sería justo traer uno aquí,{w=0.1} tampoco.{w=0.2} Heh."
    else:

        n 1fsqpu "Heh.{w=0.2} ¿En serio?{w=0.2} ¿Mi animal favorito...?"
        n 2fcsantsa "No tú,{w=0.1} [player].{w=0.2} Eso es seguro."

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_favourite_drink",
            unlocked=True,
            prompt="¿Cuál es tu bebida favorita?",
            category=["Comida"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_favourite_drink:
    if Natsuki.isAffectionate(higher=True):
        n 1unmbg "¡Ooooh!{w=0.2} ¿Mi bebida favorita?"

    elif Natsuki.isNormal(higher=True):
        n 1unmaj "¿Mmm?{w=0.2} ¿Mi bebida favorita?"

    elif Natsuki.isDistressed(higher=True):
        n 1nllbo "¿Huh?{w=0.2} Oh.{w=0.1} Mi bebida favorita."
    else:

        n 2fslsf "...No puedo entender por qué te importaría,{w=0.1} [player]."
        n 1fsqsf "Así que...{w=0.3} ¿por qué debería?"
        n 2fsqan "Agua.{w=0.2} Ahí hay una respuesta para ti.{w=0.2} ¿Feliz?"
        n 2fcsanltsa "Ahora solo vete..."
        return

    if Natsuki.isNormal(higher=True):
        n 1ullaj "Tengo que decir...{w=0.3} depende del clima más que nada."
        n 3tnmaj "Digo...{w=0.3} ¡¿qué clase de tonto ordenaría una bebida helada en medio del invierno?!"
        n 1fllss "Pero como sea..."
        n 1fcsbg "Si hace frío,{w=0.1} entonces chocolate caliente.{w=0.2} Sin preguntas,{w=0.1} sin dudas."
        n 4uchgn "En las profundidades del invierno,{w=0.1} ¡definitivamente no obtendrás una mejor opción que esa!"

        if Natsuki.isAffectionate(higher=True):
            n 1fcsbg "Y sí,{w=0.1} [player] -{w=0.1} crema batida,{w=0.1} malvaviscos -{w=0.1} todo.{w=0.2} El paquete completo."
            n 1uchgn "...¡Y no aceptaría nada menos!"
            n 3fllbg "Digo,{w=0.1} piénsalo -{w=0.1} si estás tomando chocolate caliente,{w=0.1} ya has perdido un poco en el frente de la salud."
            n 3uchgn "Así que bien podrías ir con todo,{w=0.1} ¿verdad?{w=0.2} Ahaha."

            if Natsuki.isLove(higher=True):
                n 4fcsdvl "Además,{w=0.2} no estoy muy preocupada -{w=0.1} simplemente compartiremos las calorías,{w=0.1} [player]~."

        n 1unmaj "En cuanto a clima más cálido...{w=0.3} eso es un poco más complicado,{w=0.1} en realidad."
        n 3fslsr "Déjame pensar..."
        n 3fsrsr "..."
        n 1fchbs "¡Ajá!{w=0.2} ¡Lo tengo!"
        n 1unmbg "¡Tienen que ser esas malteadas,{w=0.1} pero de uno de esos lugares donde puedes elegir qué lleva!"
        n 1fsqsm "No solo me refiero a elegir un sabor,{w=0.1} [player]..."
        n 4fchgn "¡Me refiero a donde puedes escoger cualquier combinación de ingredientes que quieras!"
        n 1fllss "Bueno...{w=0.3} siempre y cuando se mezcle bien,{w=0.1} al menos."
        n 1ncssm "Todo tipo de dulces,{w=0.1} cualquier tipo de leche..."

        if Natsuki.isAffectionate(higher=True):
            n 1ucssm "¿Aunque si tuviera que elegir un favorito?"
            n 3fcsbg "Tienen que ser fresas con crema,{w=0.1} obviamente."
            n 3fllbgl "Y...{w=0.3} ¿quizás con solo un toque de chocolate también?{w=0.2} Ehehe."
        else:

            n 1fchbg "Sí.{w=0.2} ¡Ese es el verdadero trato!"

        n 3fllpo "Cielos...{w=0.3} toda esta charla sobre bebidas me está dando un poco de sed,{w=0.1} en realidad.{w=0.2} Así que en esa nota..."
        n 1fnmbg "Necesitas mantenerte hidratado también,{w=0.1} [player] -{w=0.1} ¡cualquiera que sea el clima!"
    else:

        n 1flrsl "Supongo que depende de cómo esté el clima."
        n 2fnmbo "Chocolate caliente si hace frío,{w=0.1} aunque no soy muy exigente supongo."
        n 1fllaj "En cuanto a clima más cálido..."
        n 1fllsl "Realmente no lo sé.{w=0.2} Lo que sea está bien."
        n 2fsqsl "Heh.{w=0.2} Aunque a este paso,{w=0.1} no debería esperar mucho más que agua del grifo de ti de todos modos.{w=0.2} ¿Verdad,{w=0.1} [player]?"

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_school_uniform",
            unlocked=True,
            prompt="¿Qué piensas de tu uniforme escolar?",
            category=["Moda"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_school_uniform:
    if Natsuki.isLove(higher=True):
        n 4fsqcsl "¿Oho?{w=0.2} ¿A [player] le gustan las chicas en uniforme?"
        n 1ksqaj "Wow...{w=0.3} eres incluso {i}más{/i} asqueroso de lo que pensé."
        n 1fsqsm "..."
        $ chosen_tease = jn_utils.getRandomTease()
        n 3uchgn "¡Oh vamos,{w=0.1} [chosen_tease]!{w=0.2} ¡Siempre te pones todo berrinchudo cuando te llamo así!{w=0.2} Simplemente no puedo resistirme."
        n 1fchsm "Ehehe.{w=0.2} Así que como sea..."

    elif Natsuki.isAffectionate(higher=True):
        n 4unmaj "¿Huh?{w=0.2} ¿Mi uniforme escolar?"
        n 1fsqsm "...Ehehe."
        n 3fcsbgl "¿Por qué preguntas,{w=0.1} [player]?{w=0.2} ¿{i}Tú{/i} querías usarlo o algo así?"
        n 1fchgn "¡Oh!{w=0.2} ¡Podemos jugar a los disfraces!{w=0.2} ¿No te gustaría eso,{w=0.1} [player]?{w=0.2} ¡Será muy divertido!"
        n 4uchbselg "Apuesto a que podría hacerte ver tan lindo~.{w=0.1} ¡Ahaha!"
        n 1nllss "Bueno como sea,{w=0.1} poniendo las bromas a un lado..."

    elif Natsuki.isNormal(higher=True):
        n 4tnmaj "¿Mi uniforme escolar?{w=0.2} Eso es...{w=0.3} una cosa un poco rara para preguntarme,{w=0.1} ¿eh?"
        n 1nslaj "Bueno,{w=0.1} como sea.{w=0.2} Lo dejaré pasar...{w=0.3} esta vez."

    elif Natsuki.isDistressed(higher=True):
        n 2nsraj "...¿Huh?{w=0.2} Oh,{w=0.1} el uniforme escolar."
        n 1nsqsl "Yo...{w=0.3} no sé qué esperas escuchar de mí,{w=0.1} [player]."
        n 1fsqsl "Tenía que usarlo para la escuela.{w=0.2} Ese es el punto de un uniforme,{w=0.1} si no te habías dado cuenta."
        n 2fsrsf "No importa si me gusta o no."
        n 4fsqbo "...Y importa aún menos si a ti te gusta."
        return
    else:

        n 2fsran "Heh.{w=0.2} Me gusta más que {i}tú{/i}.{w=0.2} Idiota."
        return

    n 1unmaj "Está bien,{w=0.1} supongo.{w=0.2} ¡De hecho realmente me gustan los colores cálidos!"
    n 1nnmss "Son mucho más fáciles para la vista que muchos de los otros uniformes que he visto por ahí."
    n 2nsqsr "Pero Oh.{w=0.2} Dios.{w=0.2} Mío.{w=0.2} [player]."
    n 1fcsan "Las capas.{w=0.2} Tantas capas."
    n 4fllem "¡¿Quién pensó siquiera que alguien necesita tanta ropa?!{w=0.2} ¡¿Para la escuela,{w=0.1} de todos los lugares?!"
    n 1fbkwr "Digo...{w=0.3} ¡¿siquiera {i}sabes{/i} cómo es usar toda esa ropa en verano?!{w=0.2} ¡Es {i}horrible{/i}!"
    n 2flrpo "Y el blazer...{w=0.3} ¡ugh!{w=0.2} Es de hecho la peor cosa de la historia."
    n 2fsqpo "Como sí,{w=0.1} podría quitarme algo entre clases,{w=0.1} pero tenía que ponérmelo todo de nuevo cuando entraba."
    n 2fllpo "...O ser regañada.{w=0.2} {i}Otra vez{/i}.{w=0.2} Honestamente no tengo idea de cómo Sayori se salía con la suya con el suyo siendo tan desarreglado."
    n 1fcsan "¡Y todas las cosas del uniforme son súper caras también!{w=0.2} ¡Hablando de una patada en los dientes!"
    n 4fslan "Idiotas."
    n 1fslsr "Ugh...{w=0.3} En serio desearía que los uniformes fueran prohibidos o algo."
    n 3flrpo "Supongo que podría ser peor.{w=0.5}{nw}"
    extend 1ksrsl " Al menos me mantuvo caliente cuando importaba."

    if not Natsuki.isWearingClothes("jn_clothes_school_uniform"):
        n 1nchgn "...¡Y no lo estoy usando ahora,{w=0.1} al menos!{w=1}{nw}"
        extend 3fcsbg " Siempre un plus."
        n 1ullaj "Dicho eso...{w=0.75}{nw}"
    else:

        n 1ulraj "Pero...{w=0.75}{nw}"

    extend 4unmbo " ¿qué hay de ti,{w=0.1} [player]?"
    show natsuki 1tnmpu at jn_center

    menu:
        n "¿Tuviste que usar algún uniforme en la escuela?"
        "Sí, tuve que usar uniforme":

            n 3fcsbg "¡Ajá!{w=0.2} Así que conoces la lucha también,{w=0.1} ¿eh?"
        "No, no tuve que usar uniforme":

            n 1fslsr "..."
            n 3fsqsr "...Suertudo."
        "Tengo que usar uniforme ahora":

            n 1fchgn "¡Entonces tienes mis condolencias,{w=0.1} [player]!{w=0.2} Ahaha."
            n 4fcsbg "Bueno saber que estamos en la misma página,{w=0.1} sin embargo."
        "No tengo que usar uniforme ahora":

            n 1fslsr "..."
            n 3fsqsr "...Suertudo."

    n 1ullss "Bueno,{w=0.1} como sea..."

    if Natsuki.isLove(higher=True):
        n 1fllss "Todavía no me {i}gusta{/i} particularmente usarlo..."
        n 3uslbgl "Pero...{w=0.3} creo que puedo soportarlo.{w=0.2} Solo por ti,{w=0.1} [player]~."
        n 1usrdvl "Ehehe."

    elif Natsuki.isAffectionate(higher=True):
        n 4usrdvl "S-{w=0.1}si no te importa,{w=0.1} [player]?"
        n 1fllbgl "Supongo que tiene eso a su favor también,{w=0.1} al m-{w=0.1}menos..."

    elif Natsuki.isNormal(higher=True):
        n 1fcsbg "¡Supongo que al menos nunca tuve que aprender a hacer una corbata!"
        extend 1nchgn " Ehehe."

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_flying",
            unlocked=True,
            prompt="¿Alguna vez has volado a algún lugar?",
            category=["Transporte"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_flying:
    if Natsuki.isEnamored(higher=True):
        n 4uwdaj "¡Ooh!{w=0.2} ¿Volar?{w=0.2} ¿Como en un avión?"
        n 3fllun "Nnn...{w=0.3} Desearía poder decir que sí,{w=0.1} [player]..."
        n 1fchbg "¡No me malinterpretes sin embargo!{w=0.2} ¡{i}Totalmente{/i} volaría a algún lugar nuevo si pudiera!"
        n 4fslsl "Es solo...{w=0.3} el precio de todo,{w=0.1} ¿sabes?"
        n 4kllsl "Nunca he tenido un pasaporte,{w=0.1} pero es principalmente los boletos y todo más allá de eso..."

    elif Natsuki.isHappy(higher=True):
        n 4unmaj "¿Huh?{w=0.2} ¿Volar?{w=0.2} ¿Como en un avión o algo así?"
        n 1kllaj "Yo...{w=0.3} desearía poder decir que sí,{w=0.1} [player]."
        n 1fnmbg "¡No me malinterpretes sin embargo!{w=0.2} Me encantaría salir volando a algún lugar.{w=0.2} ¡Como para unas vacaciones o algo!"
        n 2flrpo "Es solo el costo lo que me detiene, ¿sabes?"
        n 2fcspo "Incluso si tuviera un pasaporte, hay tantas cosas que pagar..."

    elif Natsuki.isNormal(higher=True):
        n 1unmaj "¿Oh?{w=0.2} ¿Como volar en un avión o lo que sea?"
        n 1kllbo "Uhmm..."
        n 2klraj "Yo...{w=0.3} nunca tuve realmente la oportunidad de volar a ningún lado,{w=0.1} [player]."
        n 1unmaj "Ni siquiera tengo un pasaporte o algo así,{w=0.1} ¿e incluso si lo tuviera?"
        n 2nsraj "No es como si los boletos fueran...{w=0.3} asequibles,{w=0.1} ¿si sabes a lo que me refiero?"
        n 2nslpo "Especialmente para alguien en mi...{w=0.3} posición."

    elif Natsuki.isDistressed(higher=True):
        n 1nnmbo "¿Volar?{w=0.2} Como...{w=0.3} ¿en un avión?"
        n 2fnmsf "No,{w=0.1} [player].{w=0.2} No lo he hecho."
        n 1fllsf "Nunca he tenido un pasaporte,{w=0.1} y es demasiado caro de todos modos."
        n 1fnmaj "Realmente tampoco me gusta la idea del impacto ambiental."
        n 2fsqaj "...Pero algo me dice que realmente no te importa ese último punto,{w=0.2} ¿o sí?"
        n 1flrca "Sabes...{w=0.3} solo yendo por mi experiencia hasta ahora."
        n 2fsqca "...¿Estoy {i}equivocada{/i}?"
        return
    else:

        n 2fsqanean "No,{w=0.1} [player].{w=0.2} No lo he hecho.{w=0.2} Y probablemente nunca lo haré."
        n 1fcsanltsa "Regodéate todo lo que quieras.{w=0.2} No me importa un comino si tú lo has hecho."
        return

    n 1ullaj "Además,{w=0.1} trato de no sentirme muy mal por ello.{w=0.2} ¡Es mucho mejor para el medio ambiente si no lo hago,{w=0.1} de todos modos!"
    n 1nnmbo "Volar a lugares es bastante contaminante.{w=0.2} Creo que solo me sentiría egoísta si estuviera constantemente zumbando por ahí,{w=0.1} sabiendo lo malo que es eso para todos."
    n 1nllss "Pero...{w=0.3} esa soy solo yo,{w=0.1} supongo."
    n 4unmaj "¿Qué hay de ti,{w=0.1} [player]?"
    menu:
        n "¿Eres un viajero frecuente?"
        "Sí, vuelo regularmente":

            n 1fcsbg "¿Oh?{w=0.2} ¡Bueno mírate,{w=0.1} [player]!"
            n 3fslpo "Supongo que está {i}claro{/i} como el cielo lo bien que te está yendo para ti mismo."
            n 1fchbg "Ehehe."
            n 1fnmaj "Solo trata de evitar acumular demasiadas millas,{w=0.1} [player]."
            n 4fllss "Tienes que pensar en el planeta también,{w=0.1} sabes..."

            if Natsuki.isEnamored(higher=True):
                n 4fslnvf "E-{w=0.1}especialmente si la gente que realmente nos importa está en él.{w=0.2} Ahaha..."

            elif Natsuki.isHappy(higher=True):
                n 1fchgn "¡Sin excusas,{w=0.1} [player]! Ehehe."

            $ persistent._jn_player_has_flown = True
        "Vuelo a veces":

            n 1unmss "¡Ooh,{w=0.1} okay!{w=0.2} ¿Así que la vacación ocasional o vuelo familiar entonces?"
            n 2fslsm "Ya veo,{w=0.1} ya veo..."
            n 1fcsbg "Bueno,{w=0.1} ¡bien por ti,{w=0.1} [player]!{w=0.2} Todos deberían tener la oportunidad de explorar el mundo."
            n 4kslss "Con suerte tendré la oportunidad algún día también."

            if Natsuki.isEnamored(higher=True):
                n 1fsqsg "Espero estar disponible cuando eso pase,{w=0.1} [player]."
                n 3fchgnl "¡Vas a ser mi guía turístico,{w=0.1} te guste o no!"

            elif Natsuki.isHappy(higher=True):
                n 1fsqsm "Más te vale ser útil cuando eso pase,{w=0.1} [player]..."
                n 4fchgn "¡Veremos qué tan buen guía eres!"

            $ persistent._jn_player_has_flown = True
            $ persistent._jn_player_has_flown = True
        "He volado antes":

            n 4fsqct "¿Oh?{w=0.2} Así que ya te ganaste tus alas,{w=0.1} ¿eh?"
            n 1tllaj "Hmm...{w=0.3} ¿Me pregunto a dónde fuiste?"
            n 1fnmaj "Tienes que prometer contarme si vuelas de nuevo,{w=0.1} ¿okay?"
            n 3fchgn "¡Quiero escuchar todo sobre ello!"

            $ persistent._jn_player_has_flown = True
        "Nunca he volado":

            n 1fcsbg "¡Entonces eso es solo otra cosa que tenemos en común,{w=0.1} [player]!"
            n 1fsqss "Supongo que podrías decir..."
            n 4fsqdv "Que ambos somos gente {i}con los pies en la tierra{/i},{w=0.1} ¿eh?"
            n 3fchgnelg "¡Ahaha!"

            $ persistent._jn_player_has_flown = False

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_are_you_into_cars",
            unlocked=True,
            prompt="¿Te gustan los autos?",
            category=["Transporte"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_are_you_into_cars:
    $ already_discussed_driving = False


    if get_topic("talk_driving"):
        $ already_discussed_driving = get_topic("talk_driving").shown_count > 0

    elif get_topic("talk_are_you_into_cars"):
        $ already_discussed_driving = get_topic("talk_are_you_into_cars").shown_count > 0

    if already_discussed_driving:

        if Natsuki.isNormal(higher=True):
            n 4unmaj "¿Eh?{w=0.2} ¿Autos?"
            n 1fchgn "¡Caray,{w=0.1} sabes que no puedo conducir,{w=0.1} tonto!{w=0.2} ¡No tengo una razón para que me gusten los autos!"
            n 3nlrbg "Bueno,{w=0.1} como sea..."

        elif Natsuki.isDistressed(higher=True):
            n 1fcssl "[player].{w=0.2} Sabes que no puedo conducir.{w=0.2} ¿Por qué pensarías que me gustarían los autos,{w=0.1} de todas las cosas?"
            n 2fllsl "...Bien.{w=0.2} Lo que sea."
        else:

            n 1fsqpu "...¿En serio?"
            n 2fsqan "Sabes que no puedo conducir.{w=0.2} Así que ni siquiera voy a {i}fingir{/i} que me importa si a ti te va eso,{w=0.1} [player]."
            n 1fnmfultsc "Además...{w=0.3} apuesto a que tú {i}nunca{/i} tratarías a tu {i}precioso{/i} auto como me tratas a mí,{w=0.1} ¿hum?"
            return
    else:


        if Natsuki.isNormal(higher=True):
            n 4unmaj "¿Huh?{w=0.1} ¿Que si me gustan los autos?"
            n 2fllnv "Bueno...{w=0.3} ¿para decirte la verdad,{w=0.1} [player]?"
            n 1unmaj "...Nunca he tenido una licencia en realidad."
            n 3flrpo "¡Ni siquiera creo que pudiera permitirme aprender!"
            n 1nnmaj "Así que nunca me he sentido realmente atraída por ellos honestamente."

        elif Natsuki.isDistressed(higher=True):
            n 1fnmsr "No puedo conducir,{w=0.1} [player].{w=0.2} No tengo una licencia tampoco;{w=0.1} aprender fue siempre demasiado caro."
            n 2fnmpu "Así que...{w=0.3} ¿por qué me gustaría eso?{w=0.1} Literalmente no puedo {i}permitirme{/i} que me gusten."
        else:

            n 1fcsan "Última noticia,{w=0.1} idiota.{w=0.2} {i}No puedo{/i} conducir,{w=0.1} y ni siquiera puedo permitirme {i}aprender{/i}."
            n 2fsqan "Así que dime {i}tú{/i} -{w=0.1} ¿por qué me gustarían los autos?{w=0.2} Y si fuera así,{w=0.1} ¿por qué demonios querría hablar contigo sobre ellos?"
            n 1fcspu "...Heh.{w=0.2} Sí,{w=0.1} eso pensé.{w=0.2} Terminamos aquí,{w=0.1} [player]."
            return

    if Natsuki.isNormal(higher=True):
        n 1unmsm "Puedo apreciar el talento que conlleva hacerlos -{w=0.1} ¡creo que es realmente genial lo expresivos que pueden ser!"
        n 1nllss "Como...{w=0.3} los lenguajes de diseño de todas las diferentes marcas,{w=0.1} la ingeniería que llevan y todo eso."
        n 1fchbg "Es bastante loco cuánto trabajo conlleva;{w=0.1} ¡y eso es definitivamente algo por lo que tengo respeto!"
        n 2fsqsm "¿Qué hay de ti sin embargo, [player]?{w=0.2} Tú {i}sí{/i} sacaste el tema,{w=0.1} pero pensé en preguntar de todos modos..."
        menu:
            n "¿Te gustan los autos?"
            "¡Sí! Me gustan mis autos":



                if persistent.jn_player_can_drive is None:
                    n 1tllbo "Huh.{w=0.2} De hecho no estaba segura de si podías conducir siquiera,{w=0.1} pero supongo que eso no importa realmente."
                    n 3fsqsm "Supongo que ser un fan del motor no es un club exclusivo,{w=0.1} ¿eh?"
                    n 1uchbg "Ahaha."


                elif persistent.jn_player_can_drive:
                    n 4fsgbg "Bueno,{w=0.1} vaya sorpresa."
                    n 1fchgn "Ehehe."
                    n 1fcsbg "No te preocupes,{w=0.1} te tenía calado por el estilo,{w=0.2} [player]."
                    n 3fchbg "Pero oye -{w=0.1} ¡lo que te haga feliz!"
                else:


                    n 1unmaj "Eso es...{w=0.3} de hecho bastante sorprendente de escuchar de ti,{w=0.1} [player]."
                    n 1nllaj "Sabes,{w=0.1} ya que dijiste que no puedes conducir y todo eso..."
                    n 3fchbg "Pero supongo que es como cualquier cosa -{w=0.1} no tienes que estar haciéndolo para ser un fan,{w=0.1} ¡y eso está bien conmigo!"
            "No me importan mucho":

                n 1ullss "Supongo que eso es justo -{w=0.1} y no te preocupes,{w=0.1} lo entiendo completamente."
                n 4nnmsm "Pero si a alguien le gusta ese tipo de cosas,{w=0.1} ¿quiénes somos para juzgar,{w=0.1} después de todo?"
            "No, no me gustan":

                n 1ulraj "...Huh.{w=0.2} Eso es un poco raro -{w=0.1} entonces ¿por qué sacaste el tema,{w=0.1} [player]?"

                if persistent.jn_player_can_drive:
                    n 4tlraj "¡Especialmente si puedes conducir!"
                    n 1tllpu "Huh..."

                n 3fchbg "Bueno,{w=0.1} como sea.{w=0.2} ¡Justo supongo!"
    else:

        n 2flrsr "Supongo que puedo respetar el trabajo y talento que conlleva diseñar y hacer uno..."
        n 1fnmbo "Pero es lo mismo que cualquier otra cosa."
        n 1fsqbo "...Supongo que te gustan tus autos entonces,{w=0.1} ¿no?"
        n 1fcspu "Heh."
        n 2fsqpu "Sería lindo si extendieras ese respeto a las {i}personas{/i} también,{w=0.1} [player]."
        n 4fsqsr "{i}Solo digo.{/i}"

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_how_do_you_feel_about_me",
            unlocked=True,
            prompt="¿Cómo te sientes sobre mí?",
            category=["Natsuki", "Romance", "Tú"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_how_do_you_feel_about_me:
    if Natsuki.isLove(higher=True):

        if persistent.jn_player_love_you_count > 0:
            n 3kwmpof "[player]...{w=0.3} ¿no es obvio? Sabes que ya te amo,{w=0.1} ¿verdad?"
            n 3fllpol "Caray...{w=0.3} realmente eres un tonto a veces,{w=0.1} sabes."
            n 1kllssl "Pero...{w=0.3} me gusta un poco esa parte tonta de ti,{w=0.1} [player]."
            n 1nwmbgl "Nunca cambies,{w=0.1} ¿okay? Ehehe."
            n 4nchbgl "¡Te amo,{w=0.1} [player]~!"
        else:

            n 1fcsanf "¡Nnnnnnn-!"
            n 4fnmanf "¡V-{w=0.1}vamos! ¿No es obvio para ahora? Caray...{w=0.5}{nw}"
            n 2fllpof "¿Realmente tengo que deletreártelo,{w=0.1} [player]?"
            n 1fcspolesi "Ugh...{w=0.5}{nw}"
            n 1fsqssl "Heh.{w=0.2} De hecho,{w=0.1} ¿sabes qué?"
            n 4fsqbgl "Dejaré que lo averigües."
            n 1fslajl "Y no,{w=0.1} antes de que preguntes -{w=0.1} ya has tenido suficientes pistas."
            n 2fllpol "Tonto..."

        return

    elif Natsuki.isEnamored(higher=True):
        n 1fcsanf "¡Uuuuuu-!"
        n 4fskwrf "¿E-{w=0.1}estás tratando de acorralarme o algo así,{w=0.1} [player]?"
        n 2fllemf "Caray...{w=0.5}{nw}"
        n 1fcseml "Deberías {i}saber{/i} lo que pienso de ti para ahora...{w=0.5}{nw}"
        n 2fllpol "...{w=0.5}{nw}"
        n 2kcspol "...{w=0.3}Bien."
        n 4fcspol "Tú...{w=0.3} me...{w=0.3} gustas,{w=0.1} [player].{w=0.2} Un montón."
        n 1fbkwrf "¡A-{w=0.1}ahí!{w=0.2} ¿¡Feliz ahora!?"
        n 4kllsrl "Cielos..."
        return

    elif Natsuki.isAffectionate(higher=True):
        n 1fskemf "¿H-{w=0.1}huh? ¿Cómo me siento sobre ti?"
        n 4fbkwrf "¡¿P-{w=0.1}or qué me estás preguntando sobre eso?!"
        n 2fllpol "Cielos,{w=0.1} [player]...{w=0.3} harás las cosas todas incómodas a este paso..."
        n 1fcseml "Estás bien,{w=0.1} ¡así que no necesitas seguir molestándome sobre eso!"
        n 4flrunl "Caray..."
        return

    elif Natsuki.isHappy(higher=True):
        n 1uskemf "¡¿H-huh?!"
        n 2fllbgl "¡O-oh! Ahaha..."
        n 1nllaj "Bueno,{w=0.1} digo...{w=0.5}{nw}"
        n 1ullaj "Es bastante divertido estar contigo,{w=0.1} considerando todo."
        n 4fllnvl "Así que...{w=0.3} sí...."
        return

    elif Natsuki.isNormal(higher=True):
        n 1uskeml "¡¿H-{w=0.1}huh?!"
        n 1fllbg "¡O-oh!"
        n 4unmaj "Digo...{w=0.3} estás bien...{w=0.3} ¿supongo?"

        if not persistent.jn_player_first_farewell_response:
            n 1flleml "¿Q-{w=0.1}qué esperabas?{w=0.5}{nw}"
            extend 2fnmpol " ¡Nos acabamos {i}literalmente{/i} de conocer!"

        n 1nnmpu "Eso es todo lo que puedo decir hasta ahora,{w=0.1} así que...{w=0.3} sí."
        n 1nllca "...{w=0.5}{nw}"
        n 4nlraj "Así que...{w=0.3} ¿dónde estábamos?"
        return

    elif Natsuki.isUpset(higher=True):
        n 2fsqaj "...{w=0.3}¿Oh? Eso te importa ahora,{w=0.1} ¿no es así?"
        n 1fsqbo "Entonces dime,{w=0.1} [player]."
        n 1fnmun "¿Por qué sigues hiriendo mis sentimientos así?"
        n 1fcsun "...{w=0.5}{nw}"
        n 2fllan "No tengo mucha paciencia para los idiotas,{w=0.1} [player]."
        n 1fnmaj "No sé si estás tratando de ser gracioso o qué,{w=0.1} pero basta ya.{w=0.2} ¿Entendido?"
        n 1fsqsr "Gracias."
        return

    elif Natsuki.isDistressed(higher=True):
        n 1fsqsr "...{w=0.3}Dejémonos de tonterías."
        n 4fcsan "Me has lastimado,{w=0.1} [player].{w=0.2} Me has lastimado otra vez,{w=0.1} y otra vez."
        n 2fnmfu "Lo has hecho tantas veces ahora."
        n 2fnman "Así que dime tú."
        n 1fsqpu "¿Qué demonios pensarías {i}tú{/i} de alguien que te hiciera eso a ti?"
        n 1fcspu "...{w=0.5}{nw}"
        n 2fsqan "Estás pisando hielo delgado,{w=0.1} [player].{w=0.2} ¿Entendido?"
        return

    elif Natsuki.isBroken():
        $ already_discussed_relationship = get_topic("talk_how_do_you_feel_about_me").shown_count > 0
        if already_discussed_relationship:
            n 2fsqpultse "...Wow.{w=0.2} ¿En serio?"
        else:

            n 1fsqputsb "...{w=0.3}No tengo palabras para cómo me siento sobre {i}ti{/i}."
            n 2fsqfultseean "No me pongas a prueba,{w=0.1} {i}[player]{/i}."

        return
    else:

        n 1fsqunltse "...{w=1}...{w=1}{nw}"
        n 1fcsanltda "...{w=1}..."
        return

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_are_you_into_cosplay",
            unlocked=True,
            prompt="¿Te gusta el cosplay?",
            category=["Moda", "Media", "Sociedad"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_are_you_into_cosplay:
    $ already_unlocked_cosplay_outfits = jn_outfits.getOutfit("jn_trainer_cosplay").unlocked and jn_outfits.getOutfit("jn_sango_cosplay").unlocked

    if Natsuki.isEnamored(higher=True):
        if already_unlocked_cosplay_outfits:
            n 1tnmpu "¿Eh?{w=0.5}{nw}"
            extend 2tsqsf " ¿Cosplay {i}otra vez{/i}, [player]?"
            n 2fllpo "Yeesh..."

            if Natsuki.isWearingClothes("jn_clothes_trainer_cosplay") or Natsuki.isWearingClothes("jn_clothes_sango_cosplay"):
                n 4fsqpol "Como si tenerme {i}usando{/i} cosplay no fuera ya suficiente para ti..."
                n 1fnmeml "¡Es todo de lo que quieres {i}hablar{/i} también!"
                n 1fcseml "No soy tu propia muñeca de vestir personal,{w=0.75}{nw}"
                extend 2fsrpol " sabes..."
            else:

                n 1nslaj "Sabes,{w=0.75}{nw}"
                extend 1fsqajl " si me querías usándolo {i}tanto{/i}..."
                n 4fsqsslsbl "Te das cuenta de que podrías solo haber {i}preguntado{/i},{w=0.2} ¿verdad?"

            n 1fchsml "Ahaha."
            n 1ullss "Bueno,{w=0.2} como sea.{w=0.5}{nw}"
            extend 4unmbo " ¿Hablando en serio?"
            n 1ulrsl "No puedo decir que mucho haya cambiado,{w=0.2} honestamente."
            n 1unmpu "¡No me malinterpretes!"
            n 1fchbg "¡Totalmente quiero entrar más en el cosplay!{w=0.75}{nw}"
            extend 3fcssmeme " Cualquier excusa para presumir mi talento {i}y{/i} costura."
            n 1ullaj "Además digo,{w=0.75}{nw}"
            extend 4unmgs " ¿has {i}visto{/i} qué tipos de atuendos la gente puede lograr,{w=0.5}{nw}"
            extend 4fnmgs " todo en el nombre de las cosas que aman?"
            n 3fcsem "Todo ese talento,{w=0.3} toda esa pasión...{w=1}{nw}"
            n 1fcspu "¡Es{w=0.75}{nw}"
            extend 4fspgsedz " {i}increíble{/i}!{w=1}{nw}"
            extend 1fchgnedz " ¡No hay manera de que {i}no{/i} quiera ser parte de eso!"
            n 1kllpu "Pero..."
            n 2nslsl "Bueno."
            n 2ksrca "Ignorando cómo las convenciones están prácticamente fuera de mi alcance..."
            n 1ksqtr "No supongo que {i}tú{/i} hayas visto alguna tienda de manualidades por aquí,{w=0.2} ¿verdad?{w=0.75}{nw}"
            extend 1ksqca " ¿O alguna de mis cosas de costura?"
            n 1ksqsl "..."
            n 4ncsss "Heh.{w=1}{nw}"
            extend 4nsrsl " Sí,{w=0.2} pensé que no."
            n 1nsrajsbl "Realmente tengo que averiguar algo para eso,{w=0.75}{nw}"
            extend 1tsqsssbl " ¿eh?"
            n 1tslslsbl "..."
            n 3fcsbgsbl "B-{w=0.2}bueno,{w=0.2} si hay una cosa de la que no ando corta aquí,{w=0.75}{nw}"
            extend 1fchbgedz " ¡son ideas!{w=0.5}{nw}"
            extend 1fsqsm " Así que no te preocupes por nada,{w=0.2} [player]..."
            n 1fwrbg "¡Porque no hay escasez de ese {i}material{/i}!{w=0.75}{nw}"
            extend 4nchgnl " Ehehe."

            return
        else:

            n 4usqct "¿Oho?{w=0.5}{nw}"
            extend 3fcsbg " Cosplay,{w=0.2} ¿dices?"
            n 1fllbo "..."
            n 1ullpu "¿Honestamente?{w=0.75}{nw}"
            extend 2nslsssbl " Nunca he hecho realmente ningún cosplay {i}serio{/i} ni nada..."
            n 1unmaj "¡Pero de hecho he pensado en ello mucho más desde que me metí en el manga y todas esas cosas un montón!"
            n 1fcsbg "Además digo,{w=0.1} ¿por qué no debería?{w=0.75}{nw}"
            extend 4fspgsedz " ¡{w=0.2}{i}Amo{/i}{w=0.2} pensar en nuevas ideas para atuendos!"
            n 1fcsbg "Además,{w=0.2} ¡conozco mi camino alrededor de una aguja e hilo!{w=0.75}{nw}"
            extend 3nsrsssbr " He tenido que usarlos lo suficientemente a menudo antes."
            n 1fcsajlsbr "P-{w=0.2}pero creo que parece una manera bastante increíble de mostrar mi aprecio por los personajes que me gustan..."
            n 1fsqbg "...Y mostrar mi talento {i}ilimitado{/i} mientras estoy en ello."
            n 1usqsm "Como sea,{w=0.2} ¿quién sabe?"
            n 4fsqsm "Quizás llegues a ver algo de mi trabajo algún día,{w=0.2} [player]."
            n 1fsqbg "Apuesto a que te gustaría eso,{w=0.2} ¿eh?{w=0.5}{nw}"
            extend 1fchsml " Ehehe."



    elif Natsuki.isAffectionate(higher=True):
        if already_unlocked_cosplay_outfits:
            n 1tsqpu "¿Huh?{w=0.5}{nw}"
            extend 1tsqsf " ¿Cosplay {i}otra vez{/i}, [player]?"

            if Natsuki.isWearingClothes("jn_clothes_trainer_cosplay") or Natsuki.isWearingClothes("jn_clothes_sango_cosplay"):
                n 2fsqsflsbl "...¿Estaba {i}usándolo{/i} en serio no era suficiente ya?"
                n 4fsqsslsbl "¿O de alguna manera desperté algún tipo de nerditud oculta en ti?"
                n 4fslsslsbr "Ehehe..."
                n 1fcsemlsbr "¡C-{w=0.3}como sea!{w=0.5}{nw}"
            else:

                n 1tlraj "Tengo que decir,{w=0.2} estoy de hecho un poco impresionada."
                n 1fslsslsbr "Adulando mi interés en el manga,{w=0.75}{nw}"
                extend 4fsqsslsbr " molestándome sobre cosplay..."
                n 1tsqsm "Estás absorbiendo mi sentido del gusto bastante rápido,{w=0.2} ¿eh?{w=0.75}{nw}"
                extend 3uchgn " ¡Como una pequeña esponja tonta!"
                n 1fchsm "Ehehe."
                n 1fchss "¡Como sea!{w=0.75}{nw}"

            extend 4nllss " Poniendo todo eso a un lado..."
            n 1unmaj "De hecho no estaría {i}en contra{/i} de hacer un poco más de cosplay para nada."
            n 1ulrpu "Digo,{w=0.75}{nw}"
            extend 3flrss " Ya tengo la mayoría de lo que necesito."
            n 1fsqss "¿Ideas {i}asombrosas{/i}?{w=0.75}{nw}"
            extend 3fcsbg " ¡Listo!{w=0.75}{nw}"
            extend 4tsqsm " ¿Toneladas de experiencia?{w=0.75}{nw}"
            extend 3fchbg " ¡Listo!"
            n 4usqgn "¿Habilidad con aguja e hilo {i}inigualable{/i}?{w=1}{nw}"
            extend 3fcsbg " Oh,{w=0.2} puedes apostarlo."
            n 1fllpu "Es solo que..."
            n 2kslsl "..."
            n 1tsrsf "No tengo exactamente mucho {i}material{/i} con qué trabajar aquí,{w=0.75}{nw}"
            extend 4tnmsf " ¿sabes?"
            n 2kslbo "...O siquiera mis cosas de costura,{w=0.2} para el caso."
            n 1kslsl "..."
            n 1fcswrlsbl "B-{w=0.2}bueno,{w=0.2} ¡se me ocurrirá algo!{w=0.75}{nw}"
            extend 2fcspolsbl " Siempre lo hago,{w=0.2} c-{w=0.2}como sea."
            n 1fsqcal "Así que más te vale esperarlo con ansias,{w=0.2} [player]..."
            n 1fcsbglsbr "¡Porque no has visto nada aún!{w=0.75}{nw}"
            extend 3fcssmlsbr " Ehehe."

            return
        else:

            n 1tsrpu "Por qué...{w=1}{nw}"
            extend 1nsqbo " ¿tuve la sensación de que sacarías esto tarde o temprano,{w=0.2} [player]?"
            n 1fsqsl "..."
            n 3fnmpo "¿Qué?{w=0.75}{nw}"
            extend 3fsqgs " ¿Pensaste que {i}automáticamente{/i} me gustaría porque leo manga de vez en cuando?"
            n 4fsqpo "¿Huh?{w=0.75}{nw}"
            extend 4fnmgs " ¿Es eso?"
            n 1fsqaj "¿Y bien?"
            n 1fsqdv "..."
            n 4fchdvesm "¡Pfffft!"
            n 3fchsm "Ehehe.{w=0.5}{nw}"
            extend 1ullss " Nah,{w=0.2} está bien."
            n 1ulraj "He pensado en ello un montón,{w=0.2} honestamente -{w=0.3}{nw}"
            extend 4unmbo " como desde que me metí en el manga y todo eso hace un tiempo."
            n 2nslsssbr "No he ido {i}realmente{/i} disfrazada a una convención ni nada todavía..."
            n 2fcswrlsbl "¡P-{w=0.2}pero eso no significa que no haya intentado hacer cosplay para nada!"
            n 4fcsbgsbl "{i}Soy{/i} algo así como una pro con aguja e hilo,{w=0.75}{nw}"
            extend 1fcssmeme " ¡así que es justo lo mío!"
            n 1tslsl "..."
            n 2tslss "De hecho...{w=1}{nw}"
            extend 1fsqbg " ¿sabes qué,{w=0.2} [player]?"
            n 1fsrsm "Tal vez {i}podría{/i} simplemente darle otro intento...{w=0.5}{nw}"
            extend 3fchbg " ¡sí!"
            n 1fcsss "Hombre,{w=0.5}{nw}"
            extend 4fchgnedz " ¡tengo tantas ideas asombrosas zumbando alrededor en mi cabeza ahora!"
            n 1fsqss "Más te vale estar preparado,{w=0.2} [player]..."
            n 1fchbg "¡Porque voy a necesitar algunas segundas opiniones cuando lo haga!"
            n 3fwlbll "Para eso son los amigos,{w=0.2} ¿verdad?"



    elif Natsuki.isNormal(higher=True):
        n 1unmbo "Cosplay,{w=0.2} ¿eh?"
        n 1ulraj "Bueno...{w=0.5}{nw}"
        extend 3tnmbo " Digo,{w=0.2} he jugado con ello,{w=0.2} si eso es lo que estás preguntando."
        n 1tllpu "Nunca pensé realmente mucho en ello hasta que me metí más en el manga y cosas como esas."
        n 3flrbg "¡Se siente como que una vez que empiezas a meterte en esas cosas,{w=0.2} descubres toneladas más a la vez!"
        n 4nslsssbr "Nunca he salido realmente y hecho cosplay yo misma sin embargo..."
        n 3fcsgslsbr "¡P-{w=0.2}ero eso no significa que no podría intentarlo más!"
        n 3fcspolesi "Soy básicamente una pro con aguja e hilo,{w=0.5}{nw}"
        extend 1fchsml " ¡así que ya tengo la parte más difícil hecha!"
        n 1fcsaj "El resto es solo encontrar materiales,{w=0.2} los cuales son usualmente bastante fáciles de conseguir de todos modos."
        n 2fslcasbl "Accesorios y pelucas y todo eso son un poco más molestos,{w=0.2} pero no exactamente {i}imposibles{/i}.{w=1}{nw}"
        extend 1fcssmeme " Especialmente con un poco de ingenio."
        n 1tcssl "..."
        n 3tupbo "Mmmm..."
        n 1tllpu "Sabes,{w=0.75}{nw}"
        extend 1fllss " mientras más pienso en ello...{w=1}{nw}"
        extend 3nchgnedz " ¡más me gusta la idea de darle otra oportunidad!"
        n 1fnmbg "¿Qué hay de ti,{w=0.2} [player]?{w=0.75}{nw}"
        extend 1usqbg " Apuesto a que te encantaría ver mis habilidades en acción,{w=0.2} ¿verdad?"
        n 3fsrbgl "Bueno...{w=1}{nw}"
        extend 1fsqsm " ya veremos."
        n 2fcsgssbl "¡P-{w=0.2}ero sin promesas!"

        return

    elif Natsuki.isDistressed(higher=True):
        n 1nnmpu "¿Huh?{w=0.2} ¿Cosplay?"
        n 1fsqsr "...¿Por qué,{w=0.2} [player]?"
        n 2fsqpu "¿Para que puedas burlarte de mi ropa también?"
        n 1fslsr "..."
        n 2fsqpu "No,{w=0.2} [player].{w=0.75}{nw}"
        extend 1fcssr " Eso es para que yo lo sepa,{w=0.75}{nw}"
        extend 4fsqan " y para que tú {i}no{/i} lo averigües."
        n 2fsqgs "¿Eso responde a tu pregunta?"

        return
    else:

        n 1fsqsr "Heh.{w=0.5} ¿Por qué?"
        n 2fcsantsa "¿Para que tengas algo más sobre lo que hacerme sentir horrible?"
        n 1fcssrltsa "...Sí.{w=0.75} No gracias."
        n 2fcsanltsd "Terminé de hablar contigo sobre esto."

        return


    if (
        Natsuki.isAffectionate(higher=True)
        and persistent.jn_custom_outfits_unlocked
        and not already_unlocked_cosplay_outfits
    ):
        n 1tllbo "..."
        n 1tslpu "...De hecho,{w=0.5}{nw}"
        extend 2tslaj " ahora que lo pienso..."
        n 1tlrsl "Me pregunto..."
        n 1fcssl "..."
        n 3nnmaj "¿Sabes qué?{w=0.75}{nw}"
        extend 1nllaj " Solo...{w=0.75}{nw}"
        extend 4nslunl " dame un segundo aquí...{w=1}{nw}"

        show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
        $ jnPause(1)
        play audio chair_out

        $ jnPause(3)
        play audio drawer
        $ jnPause(2)
        play audio gift_open
        $ jnPause(3)
        n "¡...!"
        play audio clothing_ruffle
        $ jnPause(1)
        play audio zipper
        $ jnPause(5)

        $ outfit_to_restore = Natsuki.getOutfit()
        $ jn_outfits.getOutfit("jn_trainer_cosplay").unlock()
        $ jn_outfits.getOutfit("jn_sango_cosplay").unlock()
        $ Natsuki.setOutfit(jn_outfits.getOutfit(random.choice(["jn_trainer_cosplay", "jn_sango_cosplay"])))

        play audio chair_in
        $ jnPause(3)
        show natsuki 1fsldvlesssbr at jn_center
        hide black with Dissolve(1.25)


        n 2fchsslesssbr "¡T-{w=0.5}tada!{w=0.5}{nw}"
        extend 1fchsml " Ehehe..."
        n 1fsqsll "..."
        n 2fslunl "..."
        n 4fcsemlsbl "B-{w=0.2}bueno?"
        n 2fcsbglsbl "¿Qué piensas,{w=0.2} [player]?{w=0.75}{nw}"
        extend 1fchsmlsbr " ¡Lo hice todo yo misma,{w=0.2} también!"
        n 2fsqsrlsbr "..."
        n 4fnmemlsbr "¿Qué?"
        n 3fcsgslsbl "¡{i}Dije{/i} que era buena con una aguja e hilo!"
        n 3fllsslsbl "A-{w=0.3}así que por supuesto que {i}tuve{/i} que probarlo!"
        extend 1fcsajlsbl " Y..."
        n 1nslsslsbl "...Y..."
        n 4nslsllsbl "..."
        n 1kslsll "..."
        n 1kcspul "Esto...{w=1}{nw}"
        extend 2ksrsfl " no estaba hecho realmente {i}para{/i} mí,{w=0.2} sabes."
        n 1kcspulesi "..."
        n 4ksqbol "...Lo hice para Sayori."
        n 1fcseml "E-{w=0.2}estaba destinado a ser para algún tipo de fiesta después del festival que ella insistió,{w=0.2} pero...{w=1}{nw}"
        extend 2kcssll " sí."
        n 1kslslltsb "..."
        n 2fcsunltsb "Voy a...{w=1.25}{nw}"
        extend 4ksrsrl " ir a guardar esto ahora."

        show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
        $ jnPause(2)
        play audio chair_out

        $ jnPause(3)
        play audio drawer
        $ jnPause(3)
        play audio clothing_ruffle
        $ jnPause(4)
        play audio gift_close
        $ jnPause(3)

        play audio chair_in
        $ jnPause(3)
        $ Natsuki.setOutfit(outfit_to_restore)
        show natsuki 1ncspul at jn_center
        hide black with Dissolve(1.25)

        n 1kslsll "..."
        n 2kslpul "...Sé que no puedo simplemente tirar ese atuendo.{w=1.25}{nw}"
        extend 1kcsajl " Es solo que...{w=0.5} no estaría bien."
        n 1kslbol "..."
        n 4kcspul "Lo...{w=0.5} mantendré por aquí."
        n 2knmsll "Lo mejor que podría hacer es hacer algunos recuerdos {i}felices{/i} con él yo misma en su lugar."
        n 2ksrajl "...Es lo que ella hubiera hecho, d-{w=0.2}después de todo."
        n 1ksrsll "..."
        n 4ksqbol "...¿Verdad?"

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_why_do_you_like_me",
            unlocked=True,
            prompt="¿Por qué te gusto?",
            category=["Natsuki", "Romance", "Tú"],
            player_says=True,
            affinity_range=(jn_affinity.AFFECTIONATE, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_why_do_you_like_me:
    if Natsuki.isLove(higher=True):
        if jn_admissions.last_admission_type == jn_admissions.TYPE_INSECURE:
            n 4kwmsl "[player]..."
            n 1kwmsf "No me estás preguntando esto por lo que te dije antes...{w=0.3} ¿verdad?"
            n 1kllbo "..."
            n 1ncspu "Mira,{w=0.1} [player].{w=0.2} Voy a ser completamente honesta contigo,{w=0.1} ¿okay?"
            n 1ncssl "Lo que puedes -{w=0.1} o {i}no puedes{/i} hacer -{w=0.1} no es importante para mí."
            n 1nnmpu "Lo que la gente {i}dice{/i} que eres -{w=0.1} o {i}no{/i} eres capaz de -{w=0.1} no es importante para mí tampoco."
            n 4fnmpu "Tampoco es lo que la gente dice de ti."
            n 2knmsr "[player]."
            $ chosen_endearment = jn_utils.getRandomEndearment()
            n 1klrpu "Yo...{w=0.3} siento por ti de la manera que lo hago debido a cómo me has tratado,{w=0.1} [chosen_endearment].{w=0.2} ¿No puedes ver eso?"
            n 2klrss "Has pasado tanto tiempo conmigo,{w=0.1} día tras día..."
            n 4kwmss "Has escuchado mis problemas,{w=0.1} y me has contado los tuyos..."
            n 2kllpo "Has sido tan paciente con mis cambios de humor,{w=0.1} y mis momentos gruñones..."

            if persistent.jn_player_love_you_count >= 10:
                n 1kcsunl "Y...{w=0.3} me has hecho sentir..."
                n 4kcsunf "Tan amada..."
                n 1kllunl "..."

            elif persistent.jn_player_love_you_count >= 1:
                n 1kllssl "Eres...{w=0.3} eres mi primer amor,{w=0.1} [player]..."
                n 4kcussl "¿Siquiera te das cuenta de cuánto {i}significa{/i} eso para mí?"

            elif persistent.jn_player_love_you_count == 0:
                n 2kwmssl "Tú honestamente,{w=0.1} verdaderamente significas el mundo para mí,{w=0.1} [player]..."

            n 1kllssl "Así que...{w=0.3} sí."
            n 4klrnvl "¿Eso responde a tu pregunta?"
            n 1knmsr "Sé que no puedo resolver tus problemas con un chasquido de mis dedos,{w=0.1} [player].{w=0.2} No hago milagros."
            n 2kslsl "Créeme -{w=0.1} {i}ya{/i} lo habría hecho si pudiera."
            n 1knmsl "Pero..."
            n 1kllss "Espero que puedas creerme cuando digo que las cosas saldrán bien,{w=0.1} ¿okay?"
            n 4fwmsm "Solo...{w=0.3} sigue luchando..."
            n 1fcssml "...Porque yo estoy luchando por ti también."
            n 3kplnvf "Te amo,{w=0.1} [player].{w=0.2} Más te vale no olvidar eso."
            return
        else:

            n 3fcspo "[player]..."
            n 3flrpo "¿Realmente tengo que explicarte todo esto?"
            n 1flrsll "Es solo...{w=0.3} vergonzoso...{w=0.3} para mí..."
            n 1kcssll "..."
            n 4ncspu "...Okay,{w=0.1} mira."
            n 1fllssl "Has...{w=0.3} honestamente hecho más de lo que podrías saber,{w=0.1} [player]."
            n 2fllsll "Por mí,{w=0.1} digo."
            n 1knmsll "Casi he perdido la cuenta de cuántas horas has pasado hablando conmigo..."
            n 3klrssl "Has escuchado tantos de mis problemas tontos,{w=0.1} una y otra vez..."
            n 4fllunl "...Y has sido tan paciente a través de todos mis estados de ánimo estúpidos."

            if persistent.jn_player_love_you_count >= 10:
                n 1fcsunl "T-tú me has hecho sentir..."
                n 4kcsunl "Realmente apreciada.{w=0.2} Tantas veces,{w=0.1} he perdido la cuenta..."

            elif persistent.jn_player_love_you_count >= 1:
                n 1kskajf "Eres...{w=0.3} ¡eres mi primer amor,{w=0.1} incluso!"
                n 3kwmpuf "¿Siquiera sabes lo que eso {i}significa{/i} para mí?"

            elif persistent.jn_player_love_you_count == 0:
                n 3kwmpuf "Tú seriamente significas el mundo para mí,{w=0.1} [player]..."

            n 1kllssl "Así que...{w=0.3} sí."
            n 4klrnvl "¿Eso responde a todas tus preguntas?{w=0.2} ¿Soy libre de irme ahora?"
            n 1klrss "Ahaha..."
            n 2kwmpu "Pero en serio,{w=0.1} [player]."
            n 1kplbo "No dudes nunca de cuán importante eres para mí,{w=0.1} ¿entendido?"
            n 2fnmpol "Me enfadaré si lo haces."
            n 2flrpol "Y créeme..."
            n 4klrssl "Dudo que quieras eso."
            return

    elif Natsuki.isEnamored(higher=True):
        if jn_admissions.last_admission_type == jn_admissions.TYPE_INSECURE:
            n 1knmaj "...Oye,{w=0.1} [player]..."
            n 2klrpu "Esto no es por casualidad debido a lo que dijiste antes...{w=0.3} ¿verdad?"
        else:

            n 1uskpul "¿P-{w=0.1}por qué yo-{w=0.1}...?"
            n 2fcsanl "Uuuuuuu..."

        n 1fcsajl "...Okay,{w=0.1} mira.{w=0.2} Trataré de ayudarte a entender lo mejor que pueda."
        n 3fllaj "No estoy segura si alguien te está dando un mal rato o qué, pero lo diré de todos modos."
        n 1fllsr "Realmente no me importa lo que otros esperen de ti."
        n 4fnmsr "Realmente no me importa lo que otros digan o piensen de ti."
        n 4knmpu "Realmente no me importa si puedes -{w=0.1} o no puedes -{w=0.1} hacer algo."
        n 1fcseml "¡Tú...{w=0.3} me {i}gustas{/i},{w=0.1} debido a cómo me has tratado,{w=0.1} tonto!"
        n 3flleml "O sea,{w=0.1} ¡vamos!"
        n 4flrssl "Me has escuchado parlotear,{w=0.1} una y otra vez..."
        n 1knmssl "Me has escuchado en tantos problemas tontos que he tenido..."
        n 3fcsbgl "¡Incluso has lidiado con mi mal genio como un campeón!"
        n 1klrsl "..."
        n 1kcssl "...Nunca he sido tratada por nadie tan bien como he sido tratada por ti,{w=0.1} [player]."
        n 3fllslf "Así que, ¿es alguna maravilla por qué yo...{w=0.3} disfruto pasar el rato contigo tanto?"
        n 1fcsslf "..."
        n 1flrajl "Bien,{w=0.1} okay.{w=0.2} Realmente no quiero tener que explicar todo eso de nuevo,{w=0.1} así que espero que hayas asimilado todo eso."
        n 4fnmssl "Solo...{w=0.3} continúa siendo tú,{w=0.1} ¿entendido?"
        n 3kllpul "Yo...{w=0.3} como que me gusta cómo haces eso ya."
        return
    else:

        if jn_admissions.last_admission_type == jn_admissions.TYPE_INSECURE:
            n 1unmpul "...¿Huh?"
            n 4uskemf "¿P-{w=0.1}por qué yo...?"
            n 2fcsanf "..."
            n 1tlremf "..."
            n 1flrsll "..."
            n 4fnmpul "Uhmm...{w=0.3} [player]?"
            n 2fllpo "Esto no está todo relacionado con lo que me dijiste antes,{w=0.1} ¿verdad?"
            n 4knmpo "¿Sobre sentirte inseguro y todo eso?"
            n 1klrsl "..."
            n 4nnmsl "[player]."
            n 3fnmpuf "Escucha,{w=0.1} ¿okay?{w=0.2} Yo...{w=0.3} realmente no quiero tener que repetir esto."
        else:

            n 4uscemf "¡Urk-!"
            n 1uskemf "E-{w=0.1}espera,{w=0.1} ¿q-{w=0.1}qué?"
            n 3fwdemf "¡¿P-{w=0.1}or qué tú...{w=0.3} me {i}gustas{/i}?!"
            n 1fcsanf "¡Nnnnnnnnn-!"
            n 1fllwrf "¡Digo...!{w=0.2} ¡No es que tú me {i}gustes{/i} gustes,{w=0.1} o algo ridículo como eso!"
            n 3fcsemf "Ugh...{w=0.3} lo juro,{w=0.1} [player] -{w=0.1} honestamente tratas de ponerme en las situaciones más incómodas a veces..."
            n 1fllslf "..."
            n 4fllsll "Supongo...{w=0.3} que te {i}debo{/i} una respuesta sin embargo,{w=0.1} al menos."

        n 1fcssll "Mira."
        n 1nlrpu "Has sido increíble conmigo hasta ahora,{w=0.1} [player]."
        n 4klrpu "...¿Siquiera sabes cuán pocas otras personas me hacen sentir de esa manera?"
        n 1klrsl "No es...{w=0.3} realmente mucho,{w=0.1} si no lo habías deducido."
        n 2fllpol "Siempre me escuchas,{w=0.1} no me dices que soy molesta,{w=0.1} o que me calle..."
        n 1kwmsrl "Y has sido súper comprensivo también."
        n 1kllpul "Yo...{w=0.3} honestamente no podría pedir un mejor amigo,{w=0.1} [player]."
        n 3fnmbol "Siempre recuerda eso,{w=0.1} ¿entendido?{w=0.2} Me enfadaré si no lo haces."
        n 1kllbol "..."

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_fried_squid",
            unlocked=True,
            prompt="Calamar frito",
            category=["DDLC", "Comida"],
            nat_says=True,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_fried_squid:
    n 1fllss "Oye,{w=0.1} [player]..."
    n 4usqsm "¿Sabes por qué podría ir ahora mismo?"
    n 1uchbs "¡Un tazón grande,{w=0.1} y humeante de Mon-{w=0.1}ika!"
    n 1uchbg "..."
    n 2flrpu "...Huh."
    n 1tnmpu "Sabes,{w=0.1} en retrospectiva?{w=0.2} Esa broma realmente no fue graciosa la primera vez."
    n 3tllpo "No tengo...{w=0.3} idea de por qué sería graciosa esta vez,{w=0.1} para ser honesta."
    n 4uspgsesu "¡Oh!"
    n 1fchbg "¡Pero el calamar frito no es ninguna broma,{w=0.1} [player]!{w=0.2} ¿Alguna vez lo has probado?"
    n 1uchbs "¡Es {i}delicioso{/i}!{w=0.2} ¡Me encanta!"
    n 3fsqsm "No solo el viejo y aburrido marisco frito sin embargo -{w=0.1} ¡tiene que estar bien rebozado primero!"
    n 4uspbg "Esa capa dorada y crujiente es seriamente lo mejor.{w=0.2} ¡La comida frita es asombrosa!"
    n 1fllbg "No es {i}bueno{/i} para ti exactamente,{w=0.1} pero como un capricho?{w=0.2} Podrías hacerlo mucho peor..."
    n 4fcsts "¡Especialmente con salsa para condimentar las cosas un poco!"
    n 1fnmss "Por cierto -{w=0.1} ¿quieres saber cómo puedes saber que estás cenando con alguna bondad de calamar de primera?"
    n 3uchbs "¡La textura,{w=0.1} por supuesto!"
    n 3fllaj "¡El calamar recocido se vuelve todo gomoso y asqueroso,{w=0.1} y aún peor -{w=0.1} pierde todo su sabor también!"
    n 1fsqsr "Imagina morder a través del rebozado,{w=0.1} solo para encontrar que estás básicamente masticando un montón de gomas elásticas."
    n 2fsqem "¡Ugh!{w=0.2} ¡Asqueroso!{w=0.2} Hablando de una decepción."
    n 1unmaj "Pero no dejes que eso te desanime,{w=0.1} [player] -{w=0.1} la próxima vez que veas algunos,{w=0.1} ¿por qué no darle una oportunidad?"

    if jn_admissions.last_admission_type == jn_admissions.TYPE_HUNGRY:
        n 1kllss "...Probablemente cuanto antes mejor,{w=0.1} si tienes hambre como dijiste."
        n 4ullaj "Pero como sea..."

    n 1unmbg "¡Podrías incluso ser todo elegante si quisieras y ordenarlo por el nombre culinario!"
    n 3fnmbg "Diez puntos si puedes adivinar cuál es ese.{w=0.2} Ehehe."

    if Natsuki.isLove(higher=True):
        n 3flrsg "Hmm..."
        n 1fnmbg "De hecho...{w=0.3} ¿sabes qué?"
        n 1fchbg "Deberíamos simplemente conseguir un tazón de calamares para compartir.{w=0.2} Eso es justo,{w=0.1} ¿verdad?"
        n 4fsqsm "Debería advertirte sin embargo,{w=0.1} [player]..."
        n 3fchgn "¡No entregaré la última pieza sin pelear!"
        n 1nchsml "Ehehe."

    elif Natsuki.isEnamored(higher=True):
        n 1uchbg "Pero sí -{w=0.1} ¡deberías realmente darle una oportunidad si no lo has hecho ya,{w=0.1} [player]!"
        n 4fchbg "¡No querría que nadie se perdiera eso!"
        n 2klrssl "E-{w=0.1}especialmente no tú.{w=0.2} Ehehe..."
    else:

        n 1uchbg "Pero sí {w=0.1}-{w=0.1} ¡deberías realmente probarlo si no lo has hecho ya,{w=0.1} [player]!"
        n 4fchbg "¡No querría que nadie se perdiera eso!{w=0.2} Ahaha."

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_collectibles",
            unlocked=True,
            prompt="¿Tienes algún objeto de colección?",
            category=["Media"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_collectibles:
    if Natsuki.isAffectionate(higher=True):
        n 4unmpueqm "¿Coleccionables?{w=0.2} ¿Te refieres a cosas como figuras, peluches y demás?"
        n 4flrpu "Mmm...{w=0.3} realmente no.{w=0.2} ¡Coleccionar es un pasatiempo costoso,{w=0.1} [player]!"
        n 3klrpo "Digo,{w=0.1} todo depende de qué colecciones exactamente,{w=0.1} pero se siente como que los lugares que los venden se aprovechan de eso."
        n 1flraj "Como...{w=0.3} el impulso de completar una colección -{w=0.1} ¡así que suben los precios!"
        n 1fcsboesi "Ugh..."
        n 3kllbosbl "Y para gente en mi...{w=0.3} uhmm...{w=0.3} {i}posición{/i},{w=0.1} es una gran barrera de entrada."
        n 1unmaj "Pero como sea..."

    elif Natsuki.isNormal(higher=True):
        n 4tnmpueqm "¿Huh?{w=0.2} ¿Te refieres a como figuras y todas esas cosas?"
        n 1tlrpu "Bueno...{w=0.3} no,{w=0.1} [player].{w=0.2} Realmente no."
        n 2knmsf "¡No podría justificar gastar tanto solo en pasatiempos como ese!"
        n 2flrbo "...Especialmente no cuando tenía {i}otras{/i} cosas de las que preocuparme en gastar mi dinero primero."
        n 1unmaj "P-{w=0.2}pero como sea,{w=0.1} poniendo todo eso a un lado..."

    elif Natsuki.isDistressed(higher=True):
        n 1fsqsfsbl "No,{w=0.1} [player]."
        n 2fsqaj "Los coleccionables eran demasiado caros para mí.{w=0.2} No podía justificar desperdiciar el dinero que {i}sí{/i} tengo."
        n 1fnmsl "{i}Especialmente{/i} en cosas que solo se quedarán en un estante que olvidaré."
        n 4fsqsr "Sí,{w=0.1} [player] -{w=0.1} créelo o no,{w=0.1} algunos de nosotros {i}sí{/i} tenemos que pensar en cómo gastamos nuestro dinero."
        n 2fsqun "Sorprendente,{w=0.1} ¿verdad?"
        n 1fcsun "..."
        n 1fnmaj "¿Y bien?{w=0.2} ¿Satisfecho con tu respuesta?"
        n 2fsqsl "Terminamos aquí."
        return
    else:

        n 1fsqsr "...¿Por qué?{w=0.2} ...Y no solo me refiero a por qué te importa."
        n 2fsqan "Pero ¿por qué debería decirte a {i}ti{/i} si lo hago o no?"
        n 1fcsan "Probablemente solo los destrozarías."
        n 2fcsun "Heh.{w=0.2} Después de todo."
        n 4fsqupltsa "Has demostrado ser genial destrozando cosas hasta ahora,{w=0.1} {i}¿no es así?{/i}{w=0.2} Idiota."
        return

    n 1ullbo "..."
    n 2tllbo "...Huh.{w=0.2} Ahí hay un punto,{w=0.1} de hecho.{w=0.2} ¿El manga cuenta como coleccionable?"
    n 1tllaj "No...{w=0.3} estoy realmente segura..."
    n 1tnmpu "¿Qué piensas tú,{w=0.1} [player]?"
    menu:
        n "¿Lo llamarías un coleccionable?"
        "¡Yo diría que sí!":

            n 4fsqct "¡Oho!"
            n 3fchbg "¡Así que supongo que soy algo así como una coleccionista,{w=0.1} después de todo!"

            if Natsuki.isLove(higher=True):
                n 1uchsm "Supongo que todo eso tiene sentido.{w=0.2} Después de todo..."
                n 3fllsmf "Me gustaría pensar que estás en mi colección también,{w=0.1} [player]~."
                n 1uchsmf "Ehehe."
            else:

                n 1flrsm "Bueno,{w=0.1} en ese caso..."
                n 4nchbg "¡Solo hazme saber si alguna vez te apetece un tour!"
                n 3nchgn "¡No encontrarás una mejor colección!{w=0.2} Ehehe."

                if jn_activity.ACTIVITY_MANAGER.hasPlayerDoneActivity(jn_activity.JNActivities.manga):
                    n 1fllss "O,{w=0.1} al menos...{w=0.5}{nw}"
                    extend 3fsqss " una mejor...{w=0.3} {i}física{/i}."
                    n 1fsqsm "¿Verdad,{w=0.5}{nw}"
                    extend 4fsqbg " [player]?"
        "No,{w=0.1} yo no lo haría":

            n 3flrpo "Huh...{w=0.3} tienes un punto."
            n 3tnmpo "Supongo que lo llamarías una biblioteca,{w=0.1} ¿o algo así?"
            n 1nnmsm "Bueno,{w=0.1} como sea."
            n 4nsqsm "Supongo que será mejor que {i}lea{/i} sobre mis definiciones,{w=0.1} ¿verdad?"
            n 1nchsm "Ehehe."
        "Bueno,{w=0.1} definitivamente no es literatura":

            n 1nsqsr "Ja.{w=0.2} Ja.{w=0.2} Ja.{w=0.2} Ja.{w=0.2} ...Ja."
            n 2flrpo "{i}Hilarante{/i},{w=0.1} [player]."
            n 1flraj "Sigue así,{w=0.1} y te voy a dar una."
            n 4fsqsg "...Y no,{w=0.1} no me refiero a leerte una historia."

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_play_snap",
            unlocked=True,
            prompt="¿Quieres jugar Snap?",
            conditional="persistent.jn_snap_unlocked",
            category=["Juegos"],
            player_says=True,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_play_snap:
    if persistent.jn_snap_player_is_cheater:

        if not int(jn_apologies.ApologyTypes.cheated_game) in persistent._jn_player_pending_apologies:
            $ persistent.jn_snap_player_is_cheater = False
        else:

            n 1ccsem "[player]..."
            n 2cllfl "Si ni siquiera lamentas haber hecho trampa,{w=0.5}{nw}"
            extend 2csqfl " ¿por qué {i}debería{/i} jugar contigo de nuevo?"
            n 4fcssl "Vamos...{w=1}{nw}"
            extend 2csrca " no es difícil disculparse,{w=0.75}{nw}"
            extend 2csqca " ¿o sí?"

            return

    if Natsuki.isLove(higher=True):
        $ chosen_tease = jn_utils.getRandomTease()
        n 3fchbg "¡Por supuesto que sí,{w=0.2} [chosen_tease]!{w=0.5}{nw}"
        extend 3fchsmeme " Ehehe."

    elif Natsuki.isEnamored(higher=True):
        n 4unmss "¿Snap?{w=0.75}{nw}"
        extend 4fchbg " ¡Claro que sí,{w=0.2} [player]!"

    elif Natsuki.isAffectionate(higher=True):
        n 1fcsbg "Bueno,{w=0.2} ¡duh!{w=0.75}"
        extend 2fchbg " ¡No digas más,{w=0.2} [player]!"
    else:

        n 1unmaj "¿Quieres jugar Snap?{w=0.75}{nw}"
        extend 4fchsm " ¡Seguro!"

    if Natsuki.getDeskItemReferenceName(jn_desk_items.JNDeskSlots.right) == "jn_card_pack":
        n 7csqbg "Cosa buena que nunca guardé las cartas,{w=0.2} ¿eh?"
    else:

        n 4fcsss "Déjame sacar las cartas muy rápido..."

        show natsuki 4fcssm
        show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
        $ jnPause(1.5)
        play audio drawer
        $ jnPause(1)
        $ Natsuki.setDeskItem(jn_desk_items.getDeskItem("jn_card_pack"))
        show natsuki 4fchsm
        hide black with Dissolve(1)

    $ get_topic("talk_play_snap").shown_count += 1
    jump snap_intro


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_remind_snap_rules",
            unlocked=True,
            prompt="¿Puedes repasar las reglas de Snap otra vez?",
            conditional="persistent.jn_snap_unlocked and persistent.jn_snap_explanation_given",
            category=["Juegos"],
            player_says=True,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_remind_snap_rules:
    if persistent.jn_snap_player_is_cheater:
        n 2fcsan "Vamos,{w=0.1} [player]."
        n 2flrpo "Si te importaran las reglas,{w=0.1} ¿entonces por qué hiciste trampa cuando jugamos antes?"
        n 4fnmpo "Ni siquiera te has disculpado por ello todavía..."

        $ get_topic("talk_remind_snap_rules").shown_count += 1
        return
    else:

        if Natsuki.isLove(higher=True):
            n 1nchbg "Ahaha.{w=0.2} Eres tan olvidadizo a veces,{w=0.1} [player]."
            n 3nsqbg "Seguro,{w=0.1} ¡las repasaré de nuevo!{w=0.2} Soooolo para ti~."

        elif Natsuki.isEnamored(higher=True):
            n 4nchbg "¡Por supuesto que puedo!"

        elif Natsuki.isAffectionate(higher=True):
            n 1fchsm "¡Puedes apostar a que puedo!"
        else:

            n 1nnmss "¡Claro que sí!"

        $ get_topic("talk_remind_snap_rules").shown_count += 1
        jump snap_explanation


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_windup_chewing_gum",
            unlocked=True,
            prompt="Chicle",
            category=["Cierres"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_windup_chewing_gum:
    n 2fcsan "Ugh...{w=0.3} ¿sabes qué realmente me pone de los nervios?"
    n 1fsqsl "Cuando la gente es asquerosa y no se deshace del chicle apropiadamente."
    n 1fbkwr "En serio -{w=0.1} ¡me molesta muchísimo!"
    n 3fllem "Como,{w=0.1} ¿alguna vez has caminado por el centro de una ciudad y mirado al suelo?{w=0.2} ¿A todo el pavimento?"
    n 1fcsan "Todas esas manchas secas de chicle -{w=0.1} es jodidamente asqueroso,{w=0.1} ¡y se ve horrible también!"
    n 4fsqan "Y eso es en un lugar donde usualmente hay papeleras en todos lados también,{w=0.1} así que no es solo asqueroso..."
    n 3fnmwr "¡Es súper perezoso también!{w=0.2} No puedo decidir qué me revienta más."
    n 3fcsup "Aún peor que eso -{w=0.1} hay incluso gente que va y lo pega debajo de las mesas,{w=0.1} o en las paredes -{w=0.1} ¡¿quién {i}hace{/i} eso?!"
    n 1flrpu "Cielos...{w=0.3} me dan ganas de rastrearlos y pegar esa mierda de vuelta en sus estúpidas bocas."
    n 1nnmsl "Realmente no me importa si tú masticas chicle,{w=0.1} [player]."

    if Natsuki.isLove(higher=True):
        n 2kllca "Solo asegúrate de desecharlo apropiadamente,{w=0.1} ¿okay?"
        n 1kllss "Estoy segura de que lo haces de todos modos,{w=0.1} pero...{w=0.3} solo por si acaso."
        n 4kchsml "¡Te amo,{w=0.1} [player]~!"

    elif Natsuki.isAffectionate(higher=True):
        n 1nllca "Pero por favor,{w=0.1} solo deshazte de él apropiadamente cuando termines."
        n 4nchsm "¡Gracias,{w=0.1} [player]~!"
    else:

        n 3fnmaj "Pero en serio -{w=0.1} tíralo a la basura cuando termines,{w=0.1} ¿entendido?{w=0.2} O solo envuélvelo en un pañuelo y deshazte de él luego."
        n 3fsqaj "...¡O no será solo el chicle lo que será masticado!"

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_windup_smoking_vaping_indoors",
            unlocked=True,
            prompt="Fumar en interiores",
            category=["Cierres"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_windup_smoking_vaping_indoors:
    n 1fllaj "¿Sabes qué apesta,{w=0.1} [player]?"
    n 3fsqaj "Digo {i}realmente{/i} apesta -{w=0.1} no solo figuradamente,{w=0.1} ¿sino literalmente también?"
    n 1fcssf "Cuando la gente fuma o vapea en interiores,{w=0.1} o cerca de las entradas -{w=0.1} {i}especialmente{/i} cuando otra gente está cerca.{w=0.2} ¡No puedo soportarlo!"
    n 4fcsan "Como...{w=0.3} ¿qué tan desconsiderado puedes ser?{w=0.2} ¿En serio?"
    n 3fsqwr "Para empezar,{w=0.1} y como estaba diciendo -{w=0.1} ¡absolutamente {i}apesta{/i}!"
    n 3fllem "El tabaco es una cosa de olor horrible,{w=0.1} y todos esos tipos de fluidos de vapeo empalagosos no son mucho mejores tampoco."
    n 4ksqup "Se pega a las paredes también -{w=0.1} ¡así que el olor se queda por años!"
    n 1kllan "Hablando de pegarse a las paredes,{w=0.1} el humo literalmente hace eso también -{w=0.1} ¿has {i}visto{/i} la casa de un fumador,{w=0.1} o su auto?"
    n 3ksqup "Todas esas manchas amarillas...{w=0.3} pensarías que fue pintado o algo así.{w=0.2} ¡Ew!"
    n 1fsqan "Y sabes qué,{w=0.1} [player]?{w=0.2} Ni siquiera he llegado a lo peor de todo aún..."
    n 3fcsan "No he dicho nada sobre lo caro que es todo,{w=0.1} o los problemas de salud no solo para el fumador..."
    n 4fsqaj "...¡Sino para todos los demás!"
    n 1fcsbo "Ugh..."
    n 3flrbo "No me malinterpretes -{w=0.1} si alguien quiere fumar o vapear,{w=0.1} esa es su elección y su dinero.{w=0.2} No me importa."
    n 1fnmbo "Pero lo menos que pueden hacer es respetar la decisión de todos los que {i}no{/i} lo hacen,{w=0.1} ¿sabes?"
    n 1fcssl "..."

    if Natsuki.isLove(higher=True):
        n 1nnmsl "Te conozco,{w=0.1} [player].{w=0.2} Dudo mucho que seas el tipo de persona que sea un imbécil así."
        n 4klrss "Solo...{w=0.3} no me pruebes lo contrario,{w=0.1} ¿entendido?"
        n 2uchgn "¡Lo aprecio!{w=0.2} Ahaha."

    elif Natsuki.isAffectionate(higher=True):
        n 3kllpo "Dudo que seas un imbécil así incluso si fumas,{w=0.1} [player]."
        n 3fsqpo "Pero...{w=0.3} trata de no probarme lo contrario,{w=0.1} ¿okay?{w=0.2} Me gustas más no siendo un imbécil."
        n 1uchsm "¡Gracias!"
    else:

        n 1ullaj "No creo que seas un imbécil así,{w=0.1} [player]."
        n 4nnmaj "Pero...{w=0.3} solo por si acaso -{w=0.1} tenlo en mente,{w=0.1} ¿quieres?"
        n 1nchsm "¡Gracias!"

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_windup_unwashed_hands",
            unlocked=True,
            prompt="Lavado de manos",
            category=["Cierres"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_windup_unwashed_hands:
    n 4unmaj "Oye,{w=0.1} [player]."
    n 3nsqsl "¿Alguna vez has trabajado en un restaurante,{w=0.1} o un hospital o algo así?"
    n 1fnmaj "Porque apuesto a que si hay una cosa inculcada en ti...{w=0.3} ¡es qué tan importante es lavarse las manos!"
    n 3flrun "Realmente me pone de los nervios cuando la gente no se lava las manos después de hacer algo asqueroso."
    n 3fsqsl "Como...{w=0.3} {i}sabemos{/i} qué tan importante es para detener a los gérmenes de andar por ahí -{w=0.1} ¡¿y {i}qué{/i} es exactamente difícil sobre poner tus manos bajo el grifo por un minuto?!"
    n 1fslem "¡Me molesta aún más cuando la gente es realmente tonta sobre ello también!{w=0.2} Como,{w=0.1} piensan que no necesitan hacer eso si no fueron."
    n 1fcsan "Última noticia -{w=0.1} si entraste,{w=0.1} debiste haber tocado cosas -{w=0.1} ¡así que ahora hay toda esa mierda en tus manos que has sacado contigo!"
    n 4fsqsf "No solo es {i}súper{/i} repugnante y malo para {i}tu{/i} salud..."
    n 2ksqan "¡Es terrible para otros también!{w=0.2} ¿Qué tal si estás a punto de manejar la comida de alguien,{w=0.1} o visitar a alguien en el hospital?"
    n 1fllem "Podrías enfermar seriamente a alguien..."
    n 3fnmfu "...¡Y luego se ponen todos molestos cuando les señalas su asquerosidad!{w=0.2} O sea,{w=0.1} ¡vamos {i}ya{/i}!"
    n 1fcssl "Solo...{w=0.3} ugh."
    n 1ncssl "...[player]."
    n 4nnmpu "Realmente espero que mantengas tus manos impecables.{w=0.2} Y no solo cuando visitas el baño."
    n 3fsgaj "Antes de que prepares comida,{w=0.1} después de que hayas manejado basura...{w=0.3} solo piensa en dónde has estado,{w=0.1} ¿entendido?"

    if Natsuki.isLove(higher=True):
        n 1kchbg "¡No me malinterpretes sin embargo!{w=0.2} ¡Estoy bastante segura de que al menos intentas hacer lo correcto!"
        n 3nnmss "Solo...{w=0.3} mantén el buen trabajo,{w=0.1} ¿entendido?{w=0.2} Por todos."
        n 4nchsm "¡Gracias,{w=0.1} [player]!"
    else:

        n 3tsqpo "Realmente no es mucho pedir...{w=0.3} ¿o sí?"

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_windup_litter",
            unlocked=True,
            prompt="Tirar basura",
            category=["Cierres"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_windup_litter:
    n 1ullpu "Sabes,{w=0.1} [player]..."
    n 1unmaj "¿En la escuela?{w=0.2} ¿En mi escuela,{w=0.1} al menos?"
    n 1unmss "Nosotros -{w=0.1} los estudiantes -{w=0.1} éramos de hecho responsables de mantener todo limpio."
    n 3fcsbg "Ehehe.{w=0.2} ¿Estás sorprendido?"
    n 3fchgn "¡Sip!{w=0.2} Desde las papeleras,{w=0.1} hasta los escritorios,{w=0.1} hasta los pisos.{w=0.2} ¡Era todo nuestro esfuerzo lo que lo mantenía reluciente de limpio!"
    n 3flrpol "N-{w=0.1}no es que lo {i}disfrutara{/i},{w=0.1} ¡por supuesto!{w=0.2} Limpiar {i}es{/i} bastante aburrido,{w=0.1} pero es solo algo que tienes que hacer."
    n 4fnmpo "Pero te diré una cosa,{w=0.1} [player]."
    n 2fsqtr "{i}Nada{/i} me cabreaba más que los imbéciles que solo iban y tiraban o dejaban su basura en todas partes."
    n 1fnman "...¡Y no solo en la escuela!"
    n 1fcsan "Digo...{w=0.3} ¡¿por dónde empiezo?!"
    n 3fnmaj "Primero que nada -{w=0.1} ¿qué tan jodidamente cochino tienes que ser?{w=0.2} ¡¿Esta gente solo tira mierda por todos lados en sus casas también?!"
    n 1flran "¡Me molesta aún más cuando hay papeleras y cosas literalmente justo ahí!"
    n 4fcsfu "Como,{w=0.1} wow...{w=0.3} ¿perezoso además de desconsiderado?{w=0.2} ¡Qué combinación {i}encantadora{/i}!"
    n 1fllpu "Incluso si no hay un bote de basura o lo que sea cerca..."
    n 3fllan "No es como si no tuvieran bolsillos,{w=0.1} ¡o no pudieran solo cargarlo por unos minutos!"
    n 1fcswr "Ugh..."
    n 3flrup "¡Y ni siquiera he mencionado a la gente tirando su basura fuera de los autos,{w=0.1} o en lagos y estanques!"
    n 1fcssl "Me cabrea solo de pensarlo..."
    n 1fllbo "..."
    n 4fnmbo "[player]."

    if Natsuki.isEnamored(higher=True):
        n 2ksqbo "Te conozco.{w=0.2} De hecho,{w=0.1} me atrevo a decir que te conozco {i}muy{/i} bien a estas alturas."
        n 1knmbo "No creo que seas del tipo que haga eso en absoluto..."
        n 2ksraj "No me equivoco...{w=0.3} ¿o sí?"
        n 1klrss "No quiero tener que estarlo.{w=0.2} Ahaha..."

    elif Natsuki.isAffectionate(higher=True):
        n 1unmaj "No creo que seas así,{w=0.1} [player]."
        n 2ullsl "O...{w=0.3} al menos no {i}tratas{/i} de serlo de todos modos."
    else:

        n 2fnmsl "Realmente,{w=0.1} realmente espero que no seas una de esas personas."

    n 1nllpu "Así que..."
    n 1nnmsl "...Si ya eres un cochino,{w=0.1} te perdonaré esta única vez."
    n 3klrpo "Solo...{w=0.3} asegúrate de mejorar tu acto,{w=0.1} ¿okay?"

    if Natsuki.isLove(higher=True):
        n 4uchsml "Ehehe.{w=0.2} Te amo,{w=0.1} [player]~."

    elif Natsuki.isAffectionate(higher=True):
        n 3nlrpol "Significaría...{w=0.3} mucho."
    else:

        n 1fchbg "Gracias,{w=0.1} [player]."

    return



init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_custom_music_introduction",
            unlocked=True,
            prompt="Music player",
            conditional="not persistent.jn_custom_music_unlocked",
            nat_says=True,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_custom_music_introduction:
    n 1tllboeqm "..."
    n 1fllpu "...Huh."
    n 1flrbo "Me pregunto si todavía está aquí..."
    n 2fsrpoesp "..."
    n 1flraj "¿Sabes qué?{w=0.75}{nw}"
    extend 4fnmsseid " Solo dame un segundo aquí,{w=0.2} [player]."
    n 1fcsbg "¡Vas a {i}amar{/i} esto!"
    show natsuki 1fcssm

    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(0.5)
    play audio chair_out
    $ jnPause(3)
    play audio drawer
    $ jnPause(2)

    n "¡Vamos!{w=0.75} ¡Tiene que estar todavía aquí en alguna parte!{w=0.75} ¡Lo sé!"

    play audio drawer
    $ jnPause(2.5)
    play audio gift_slide
    $ jnPause(0.5)

    n "¡...!"
    n "¡Ajá!{w=0.5} ¡Sí!{w=0.75} ¡Te encontré~!"
    play audio gift_close
    $ jnPause(3)
    n "...Ah.{w=0.75} Solo tengo que...{w=0.75}{nw}"
    play audio blow
    $ jnPause(0.3)
    n "¡A-{w=0.2}ack!{w=0.75} No pensé que estuviera {i}tan{/i} polvoriento..."
    n "...Ew."

    play audio headpat
    $ jnPause(3)
    play audio gift_close
    show music_player off zorder JN_PROP_ZORDER
    show natsuki 1fchsm
    $ jnPause(1.5)
    play audio chair_in
    $ jnPause(2)
    hide black with Dissolve(2)

    n 1nchsm "..."
    n 1unmajesu "¡Oh!{w=0.5}{nw}"
    extend 2fchbgsbl " ¡[player]!"
    n 1fcsbg "¡Adivina qué encooontré!{w=0.75}{nw}"
    extend 1fsqsm " Ehehe."
    n 1fcsbg "Es...{w=1.25}{nw}"
    play audio button_tap_c
    show music_player stopped
    $ jnPause(1)
    n 2uchgn "¡...Nuestro viejo reproductor de música!{w=1}{nw}"
    extend 1fwlbg " Genial,{w=0.2} ¿verdad?"
    n 4fchbgsbl "Ehehe..."
    n 1tlrss "Bueno...{w=1}{nw}"
    extend 1nsrsssbl " más o menos."
    n 2nllsssbl "No es exactamente...{w=0.5}{nw}"
    extend 2nslsssbl " bueno...{w=1}{nw}"
    extend 2fslposbl " {i}moderno{/i},{w=0.75}{nw}"
    extend 1fcsbgsbr " ¡pero hará el trabajo!"
    n 1tslbo "..."
    n 1tslaj "De hecho...{w=0.75}{nw}"
    extend 1tllsl " ahora que lo pienso..."
    n 4tnmpo "Realmente ni siquiera sé de quién es."
    n 1tllca "Simplemente lo encontramos en el club un día.{w=0.75}{nw}"
    extend 1tnmpu " Nadie sabía si pertenecía a alguien -{w=0.5}{nw}"
    extend 1unmaj " y créeme,{w=0.2} ¡{i}intentamos{/i} averiguarlo!"
    n 2tlrsl "Preguntamos en las clases,{w=0.5}{nw}"
    extend 2tllaj " Monika envió notas...{w=1}{nw}"
    extend 1unmaw " ¡nada!"
    n 4ulraj "Así que...{w=0.75}{nw}"
    extend 1tnmsl " como que solo lo mantuvimos aquí,{w=0.2} cerca del escritorio del maestro,{w=0.2} en caso de que quien fuera regresara por él."
    n 2nslss "Y,{w=0.2} bueno..."
    n 2tsqposbr "Supongo que nunca lo harán ahora,{w=0.2} ¿eh?"
    n 1kslbo "..."
    n 1fcssslsbl "B-{w=0.2}bueno,{w=0.2} como sea.{w=0.75}{nw}"
    extend 4fchbgsbl " ¡El punto es que podemos poner la música que queramos ahora!"
    n 1fchsmeme "Creo que descubrí una manera de dejarte enviarme lo que sea que quieras que ponga,{w=0.75}{nw}"
    extend 2fwlbg " así que escucha bien,{w=0.2} ¿okay?"

    $ get_topic("talk_custom_music_introduction").lock()
    jump talk_custom_music_explanation



init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_custom_music_explanation",
            unlocked=True,
            prompt="¿Puedes explicarme la música personalizada otra vez?",
            category=["Música"],
            conditional="persistent.jn_custom_music_unlocked and persistent.jn_custom_music_explanation_given",
            player_says=True,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_custom_music_explanation:

    $ persistent.jn_custom_music_unlocked = True
    $ hide_music_player = False

    if persistent.jn_custom_music_explanation_given:
        $ persistent.jn_custom_music_explanation_given = True
        n 1unmaj "¿Eh?{w=0.2} ¿Quieres que te explique cómo funciona la música personalizada otra vez?"
        n 1uchbg "Seguro,{w=0.1} ¡puedo hacer eso!"
        n 2nnmsm "Primero lo primero,{w=0.1} déjame revisar la carpeta {i}custom_music{/i}..."
    else:

        $ hide_music_player = True
        $ persistent.jn_custom_music_explanation_given = True
        n 1unmbg "¡Muy bien!{w=0.2} Entonces...{w=0.3} es de hecho bastante simple,{w=0.1} [player]."
        n 1nsgsm "Debería haber una carpeta llamada {i}custom_music{/i} en algún lugar por aquí..."
        n 1nchbg "Déjame echar un vistazo,{w=0.1} un seg..."
        n 2ncssr "..."

    if not jn_utils.createDirectoryIfNotExists(jn_custom_music.CUSTOM_MUSIC_DIRECTORY):
        n 2tnmbg "Bueno,{w=0.1} ¡hey!{w=0.2} ¡Ya está ahí!{w=0.2} Debo haberla configurado antes y lo olvidé."
        n 2uchgn "¡Sin quejas de mi parte!"
    else:

        n 1uchbg "¡Okaaay!{w=0.2} No estaba ahí,{w=0.1} así que acabo de crearla para ti."

    $ custom_music_link_path = jn_custom_music.CUSTOM_MUSIC_DIRECTORY
    if renpy.windows:
        n 1unmaj "Entonces,{w=0.1} [player] -{w=0.3}{nw}"
        extend 1ullaj " si haces clic {a=[custom_music_link_path]}aquí{/a},{w=0.2}{nw}"
        extend 1fcsss " eso te llevará a la carpeta que configuré."
        n 1fchbg "Entonces todo lo que tienes que hacer es solo {i}copiar{/i} tu música en esa carpeta,{w=0.2} ¡y estás listo!"
    else:

        n 1unmaj "Entonces,{w=0.1} [player] -{w=0.3}{nw}"
        extend 1ullaj " deberías ser capaz de encontrar la carpeta que configuré en {i}[custom_music_link_path]{/i}."
        n 1fchbg "Todo lo que tienes que hacer es solo {i}copiar{/i} tu música en esa carpeta,{w=0.2} ¡y estás listo!"

    n 2uchgn "Pan comido,{w=0.1} ¿eh?{w=0.5}{nw}"
    extend 2fchsm " Ehehe."
    n 4uwdaj "Oh -{w=0.1} un par de cosas primero,{w=0.1} [player]."
    n 1unmpu "Cualquier música que me des necesita estar en formato {i}.mp3,{w=0.1} .ogg o .wav{/i}."
    n 1ullss "Si no sabes cómo revisar,{w=0.1} entonces solo mira las letras después del punto en el nombre del archivo."
    n 1unmss "Deberías también ser capaz de verlos en las {i}propiedades{/i} del archivo si no aparecen en la pantalla al principio."
    n 2flrbg "Como dije -{w=0.1} esta cosa no es {i}exactamente{/i} súper moderna,{w=0.1} así que no funcionará con ningún formato nuevo lujoso,{w=0.1} o extraños viejos."
    n 4uwdaj "Oh,{w=0.75}{nw}"
    extend 1nlrpu " y si tienes que convertirla primero,{w=1}{nw}"
    extend 2nsqpo " no solo la renombres."
    n 1fcsbg "¡Usa un convertidor apropiado!{w=1}{nw}"
    extend 2fsrbg " A menos que {i}disfrutes{/i} escuchar tu música siendo toda deformada y desagradable,{w=0.3} de todos modos."
    n 1nnmaj "Una vez que hayas hecho eso,{w=0.1} solo haz clic en el botón {i}Música{/i},{w=0.1} y revisaré que todo esté bien hecho."
    n 4nchbg "...¡Y eso es todo!"
    n 4nsqbg "Una palabra de advertencia sin embargo,{w=0.1} [player]..."
    n 1usqsg "Más te vale tener buen gusto."
    n 2uchgnelg "¡Ahaha!"

    if hide_music_player:
        $ jn_custom_music.hideMusicPlayer()

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_vtubers",
            unlocked=True,
            prompt="¿Sigues a algún VTuber?",
            category=["Juegos", "Media", "Sociedad"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_vtubers:
    if Natsuki.isEnamored(higher=True):
        n 1tllss "VTubers,{w=0.1} ¿eh?{w=0.2} ¿Me preguntas a {i}mí{/i}?"
        n 4fnmsm "...Wow,{w=0.1} [player].{w=0.2} Estoy impresionada."
        n 4fsqsm "Una vez más,{w=0.1} ¡has probado que eres aún más nerd que yo!"
        n 1uchsm "Ehehe."
        n 3klrbg "¡Relájate!{w=0.2} ¡Relájate,{w=0.1} cielos!{w=0.2} Sabes que nunca juzgaría seriamente tus hobbies,{w=0.1} idiota."
        n 1unmaj "Pero sí,{w=0.1} como sea..."

    elif Natsuki.isHappy(higher=True):
        n 1unmbg "¡Sí!{w=0.2} ¡Creo que conozco esos!"
        n 4tnmpu "Son esas personas con los avatares de anime que transmiten cosas en línea para la gente,{w=0.1} ¿verdad?"
        n 2tllpu "Bueno..."

    elif Natsuki.isNormal(higher=True):
        n 1unmpu "¿Huh?{w=0.2} ¿VTubers?{w=0.2} ¿Como esas personas con los avatares estilo anime que juegan juegos y cosas en línea para que la gente vea?"
        n 4tnmpu "Eso {i}es{/i} a lo que te refieres,{w=0.1} ¿verdad?"
        n 2tllpu "Bueno..."

    elif Natsuki.isDistressed(higher=True):
        n 2fsqpu "No,{w=0.1} no lo hago.{w=0.2} Preferiría estar jugando el juego yo misma que viendo a alguien jugarlo por mí."
        n 1fsqbo "Si sigues a alguno,{w=0.1} bien por ti."
        n 4flrbo "{i}Algunos{/i} de nosotros no tenemos el tiempo para sentarnos en nuestro trasero por horas..."
        n 1fsqaj "...O el dinero para dárselo a extraños."
        n 2fsqpu "[player]."
        n 1fsqsrtsb "¿Cuánto apostamos a que no eres {i}ni de cerca{/i} tan tóxico con {i}ellos{/i} como lo eres conmigo, eh?"
        return
    else:

        n 2fsqantsb "No.{w=0.2} Y no podría importarme menos si tú lo hicieras,{w=0.1} tampoco."
        n 2fnmpultsf "...Y oye,{w=0.1} última noticia,{w=0.1} idiota."
        n 1fsqupltse "Lanzar dinero a un extraño escondiéndose detrás de una imagen linda no te hace menos {b}imbécil{/b}."
        return

    n 1nchsm "¡Es definitivamente una idea genial!{w=0.2} Deja a la gente compartir sus pasiones y experiencias con otros detrás de una nueva persona..."
    n 3fllpo "Sin tener que preocuparse sobre lastres siguiéndolos en sus vidas personales,{w=0.1} o gente siendo rara,{w=0.1} o cosas así."
    n 1uwdem "Muchos de ellos incluso hacen carreras completas de ello: mercancía,{w=0.1} lanzamientos de canciones y todo -{w=0.1} ¡justo como idols!{w=0.2} ¡Es loco!"
    n 4tllem "Dicho eso..."
    n 1tnmbo "Nunca me metí realmente en ese tipo de cosas yo misma."
    n 2klrss "Como...{w=0.3} ¡no me malinterpretes!{w=0.2} Estoy segura de que son bastante divertidos de ver.{w=0.2} Si te gusta ese tipo de cosas,{w=0.1} digo."
    n 1nllsl "Pero preferiría estar jugando o haciendo algo {i}yo misma{/i} que viendo a alguien más hacerlo,{w=0.1} usualmente."
    n 1nllss "Eso podría ser solo yo,{w=0.1} sin embargo."
    n 4nllbg "Ehehe."
    n 4unmaj "¿Qué hay de ti,{w=0.1} [player]?{w=0.2} ¿Te gusta ese tipo de cosas?"
    n 1fcssm "¡Espera,{w=0.1} espera!{w=0.2} No te molestes en responder eso."
    n 3tsqsm "{i}Tú{/i} me preguntaste sobre ellos,{w=0.1} después de todo -{w=0.1} creo que eso habla por sí mismo,{w=0.1} ¿no estarías de acuerdo?"
    n 3uchbselg "¡Ahaha!"
    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_skateboarding",
            unlocked=True,
            prompt="¿Te gusta el skateboarding?",
            category=["Transporte"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_skateboarding:
    if Natsuki.isEnamored(higher=True):
        n 1fchbs "¡Puedes apostar a que sí,{w=0.2} [player]!{w=0.5}{nw}"
        extend 1fchsm " Ehehe."
        n 3tllbg "¿Pero cómo adivinaste?{w=0.5}{nw}"
        extend 3tnmbg " ¿Parezco del tipo o algo?"
        n 1tlrsm "Bueno,{w=0.2} como sea."

    elif Natsuki.isHappy(higher=True):
        n 1uchsm "Ehehe.{w=0.5}{nw}"
        extend 4fchbg " ¡Puedes apostar!"
        n 3uwlbg "¡Buena suposición,{w=0.2} [player]!"

    elif Natsuki.isNormal(higher=True):
        n 1ullaj "Yo...{w=0.3} soy,{w=0.2} de hecho.{w=0.5}{nw}"
        extend 3tllss " ¿Cómo adivinaste?"
        n 4unmss "Bueno,{w=0.2} como sea."

    elif Natsuki.isDistressed(higher=True):
        n 3fupemesi "Ugh..."
        n 1fnmbo "Sí,{w=0.2} [player].{w=0.2} Soy una skater.{w=0.2} Hago skate.{w=0.5}{nw}"
        extend 2fsqsf " ¿Es eso un problema o algo así?"
        n 1fllpu "Es solo una manera conveniente de moverse.{w=0.5}{nw}"
        extend 2fsqpu " Una manera {i}asequible{/i}."
        n 1flrsl "..."
        n 1flraj "...Sí.{w=0.2} No tengo mucho más que decir al respecto.{w=0.5}{nw}"
        extend 1fnmbo " Pero hey."
        n 2fsgaj "No es como si realmente te importara escuchar de todos modos...{w=0.5}{nw}"
        extend 2fsqsftsa " ¿no es así,{w=0.2} {i}[player]{/i}?"
        return
    else:

        n 2fsqanean "...¿Y desde cuándo te importa una mierda mis hobbies e intereses a {i}ti{/i}?"
        n 1fcsan "..."
        n 1fnmsf "Sí,{w=0.2} [player].{w=0.5}{nw}"
        extend 2fsqsftsb " {i}Disfruto{/i} el skateboarding."
        n 1fsqupltsb "Y preferiría estar haciendo eso que estar atrapada aquí hablando {i}contigo{/i}.{w=0.5}{nw}"
        extend 2fcsanltsa " Imbécil."
        return

    n 1tchbg "¡Soy una chica skater de acuerdo!{w=0.5}{nw}"
    extend 2tslbo " O...{w=0.3} ¿era?"
    n 1tllss "Aunque...{w=0.3} no realmente por elección.{w=0.5}{nw}"
    extend 4knmaj " ¡Las bicicletas son {i}caras{/i},{w=0.2} [player]!"
    n 2kllun "Y nunca podía confiar en que me llevaran mis...{w=0.3} padres,{w=0.3}{nw}"
    extend 1kllss " así que ahorré todo lo que pude,{w=0.3}{nw}"
    extend 1fcsbg " ¡y conseguí una tabla la primera oportunidad que tuve!"
    n 4nsqaj "En serio.{w=0.75}{nw}"
    extend 2fllpusbr " No tienes {i}idea{/i} de cuántos almuerzos me salté para ganar esa cosa."
    n 1unmbg "¡Pero fue de hecho súper conveniente!{w=0.5}{nw}"
    extend 3flrbg " No tenía que preocuparme por encadenarla en algún lugar,{w=0.2} o que algún idiota la dañara..."
    n 1fchsm "Podía simplemente levantarla y llevarla conmigo,{w=0.2} o tirarla en mi casillero."
    n 2nslsssbl "O sea...{w=0.3} no la necesito tanto {i}ahora{/i},{w=0.2} pero..."
    n 4fsqss "Tienes que admitirlo,{w=0.2} [player] {w=0.2}-{w=0.2} ¡soy nada si no ingeniosa!{w=0.5}{nw}"
    extend 1fchsm " Ahaha."

    n 2fllss "Yo...{w=0.75}{nw}"
    extend 2nslsl " nunca me metí súper en trucos o algo así sin embargo."
    n 1fwdgsesh "¡N-{w=0.2}no me malinterpretes!{w=1}{nw}"
    extend 3fcsgsl " ¡No es como si no pudiera dominarlos!"
    n 1fcstrlesi "¡Totalmente podría!{w=1}{nw}"
    extend 2kslcal " Pero..."
    n 1knmemsbl "No creo que pudiera {i}soportar{/i} el pensamiento de romperla por accidente."
    n 4kslunsbr "No después de todo ese esfuerzo."

    n 1kcsaj "...Sí,{w=0.2} sí.{w=0.5}{nw}"
    extend 2fcspo " No muy {i}radical{/i} de mi parte,{w=0.2} ¿eh?"

    if (
        not jn_outfits.getOutfit("jn_skater_outfit").unlocked
        and Natsuki.isAffectionate(higher=True)
        and persistent.jn_custom_outfits_unlocked
    ):

        n 1tslsl "..."
        n 4uwdajesu "¡Oh!{w=0.5}{nw}"
        extend 1fsqbs " Pero sabes qué {i}totalmente{/i} lo era,{w=0.2} [player]?{w=1}{nw}"
        extend 3fllbgsbl " Radical,{w=0.2} quiero decir."
        n 1uchgn "...¡Mi atuendo de skate favorito,{w=0.2} por supuesto!"
        n 3tllss "De hecho,{w=0.75}{nw}"
        extend 1fchbg " ¡probablemente todavía lo tengo por aquí en algún lugar también!{w=0.75}{nw}"
        extend 1ullaj " Usualmente lo traía conmigo de todos modos."
        n 3fcsajsbl "¡S-{w=0.2}solo para ir y venir de la escuela sin embargo!{w=0.75}{nw}"
        extend 3nslsssbl " No es exactamente seguir el código de vestimenta..."
        n 1nslbosbl "Pero...{w=0.75}{nw}"
        extend 1tsqem " No iba exactamente a hacer mi uniforme todo sudoroso por el resto del día tampoco."
        n 2fsrpu "...Ew."
        n 1ulrpu "Bueno,{w=0.2} como sea.{w=1}{nw}"
        extend 1unmaj " No voy a ir a buscarlo ahora sin embargo,{w=0.75}{nw}"
        extend 1nnmpu " pero creo que ambos podemos estar de acuerdo."
        n 3fcsss "Si vas a hacer skate..."
        n 3uchgn "¡Tienes que seguir {w=0.2}{i}todas{/i}{w=0.2} las reglas de lo genial!{w=0.75}{nw}"
        extend 1fchsmeme " Ehehe."

        $ jn_outfits.getOutfit("jn_skater_outfit").unlock()
    else:

        n 2ullpo "Pero...{w=0.5} suficiente de eso por ahora.{w=0.5}{nw}"
        extend 1fnmsm " Además,{w=0.2} [player]..."
        n 4fsqss "Puedo notar cuando te estás...{w=0.3} {i}aburriendo{/i}."
        n 1fchsm "Ehehe.{w=0.5}{nw}"
        extend 1uchgn " ¡Sin arrepentimientos,{w=0.2} [player]!"

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_sports",
            unlocked=True,
            prompt="¿Practicas muchos deportes?",
            category=["Salud"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_sports:
    if Natsuki.isAffectionate(higher=True):
        n 4unmaj "¿Huh?{w=0.2} ¿Deportes?"
        n 1fllss "Yo...{w=0.3} no me gusta tener que decírtelo,{w=0.1} [player]..."
        n 3fchgn "¿Pero qué tipo de deportes crees que puedo jugar en una habitación individual?{w=0.2} ¿Por mi cuenta?{w=0.2} ¿Sin equipo?"
        n 1kllbg "Cielos...{w=0.5}{nw}"
        extend 1tnmss " eres tan tonto a veces,{w=0.1} [player]."
        n 1ullbg "Bueno,{w=0.1} como sea."

    elif Natsuki.isNormal(higher=True):
        n 1unmpu "¿Eh?{w=0.2} ¿Deportes?"
        n 3tnmdv "Tú...{w=0.3} sabes que es medio difícil mantenerse activo en una habitación individual,{w=0.1} ¿verdad?"
        n 1fcsss "Ehehe.{w=0.5}{nw}"
        extend 1ullss " Bueno,{w=0.1} como sea."

    elif Natsuki.isDistressed(higher=True):
        n 1nsqpu "Sí,{w=0.1} no.{w=0.5}{nw}"
        extend 2fsqsl " No {i}ahora{/i},{w=0.1} si eso es lo que estás preguntando."
        n 1fllpu "..."
        n 1fsqan "...Y no,{w=0.2} no usábamos el tipo de uniformes que apuesto que {i}tú{/i} estás pensando."
        n 1fsqsr "¿Eso responde a tu pregunta?{w=0.5}{nw}"
        extend 2fslbo " Lo que sea."
        n 1fcsbo "Continuando."
        return
    else:

        n 1fsqan "No lo hago {i}ahora{/i},{w=0.1} si de {i}alguna manera{/i} no lo habías notado ya."
        n 1fslsl "..."
        n 1fsqpu "..."
        n 2fcsemtsa "...¿Siquiera quiero saber por qué preguntaste?"
        n 2fcsanltsd "...No.{w=0.75} No {i}quiero{/i}."
        return

    n 1nnmaj "Trato de mantenerme como puedo.{w=0.2} No puedo hacer vueltas ni nada,{w=0.5}{nw}"
    extend 3fcsbg " ¡pero puedo fácilmente hacer algunos estiramientos y saltos de tijera!"
    n 1ullpu "Por supuesto la escuela siempre fue mucho más variada con actividades,{w=0.2} pero...{w=0.5}{nw}"
    n 4tllsr "Siempre me costó un poco seguir el ritmo,{w=0.2} supongo."
    n 2nslsssbr "...Tal vez simplemente no tengo mucha resistencia."


    $ already_discussed_skateboarding = get_topic("talk_skateboarding").shown_count > 0
    if already_discussed_skateboarding:
        n 2nslpo "Probablemente no me ayudé a mí misma ahorrando para esa patineta..."

    n 1ullaj "Bueno,{w=0.1} lo que sea.{w=0.5}{nw}"
    extend 1nnmbo " No estaba {i}realmente{/i} tan metida en deportes de todos modos."
    n 1nlrca "..."
    n 4unmbs "¡Oh!{w=0.2} ¡Oh!{w=0.2} ¿Pero sabes quién lo estaba?{w=0.5}{nw}"
    extend 4fsqbg " Apuesto a que sí,{w=0.1} ¿eh?{w=0.5}{nw}"
    extend 4fcssm " Ehehe."
    n 1tsqss "Y esa es...{w=0.5}{nw}"
    extend 3fchgn " ...¡Sayori,{w=0.1} duh!"
    n 1uskgs "Digo,{w=0.1} ¡en serio!{w=0.2} ¡Deberías haberla visto!{w=0.5}{nw}"
    extend 1fnmca " ¡Ella era una {i}amenaza{/i}!"
    n 4uskaj "...¡Seriamente!{w=0.5}{nw}"
    extend 3fnmpo " ¿No me crees?"
    n 3fspgs "¡Era tan rápida!{w=0.2} Solo un destello de pelusa naranja y ropa de gimnasia desordenada...{w=0.5}{nw}"
    extend 1fbkwr " ¡y entonces boom!{w=0.2} ¡Placaje!"
    n 3fllpol "Y allá se iba saltando,{w=0.1} alegremente hacia el atardecer..."
    n 1tsqaj "...Sí.{w=0.2} ¿Si Sayori estaba en tu lado?{w=0.5}{nw}"
    extend 1fllbg " {i}Sabías{/i} que tu equipo no iba a estar empacando todo en derrota."
    n 1ullaj "Digo,{w=0.3}{nw}"
    extend 1nnmbo " Monika siempre fue bastante buena en deportes también,{w=0.1} obviamente.{w=0.5}{nw}"
    extend 3nsgca " Pero {i}nadie{/i} corría más rápido que Sayori,{w=0.1} [player].{w=0.2}"
    n 1nsqun " N{w=0.1}-{w=0.1}a{w=0.1}-{w=0.1}d{w=0.1}-{w=0.1}i{w=0.1}-{w=0.1}e."
    n 4fchbg "...Cuando recordaba atar sus cordones de todos modos.{w=0.5}{nw}"
    extend 4fchsm " Ehehe."
    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_online_shopping",
            unlocked=True,
            prompt="Compras en línea",
            category=["Sociedad"],
            nat_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_online_shopping:
    if Natsuki.isNormal(higher=True):
        n 1ullaj "Sabes,{w=0.1} es medio loco qué tan comunes son las compras en línea hoy en día."
        n 4uwdaj "Digo,{w=0.1} ¡no me malinterpretes!{w=0.5}{nw}"
        extend 1fcsbg " ¡Es súper conveniente!{w=0.2} ¡Ni siquiera necesitas dejar tu casa!"
        n 3fllpo "Así que no pienses que solo me estoy quejando,{w=0.1} o algo así.{w=0.5}{nw}"
        extend 1ullpu " Pero..."
    else:

        n 1nllsl "Es gracioso qué tan comunes son las compras en línea hoy en día."
        n 1nlrsl "Supongo que no me estoy quejando realmente sin embargo.{w=0.5}{nw}"
        extend 1nlrpu " {i}Es{/i} bastante conveniente."
        n 2ulrpu "Pero...{w=0.5}{nw}"
        extend 1nnmsf " todavía creo que es una pena cómo la gente se pierde una experiencia real."
        n 2fllsl "Nunca dejaría pasar una tarde solo hojeando libros en mi librería favorita."
        n 1fcssf "...Que es un lugar donde {i}mucho{/i} preferiría estar.{w=0.5}{nw}"
        extend 4fsqan " {i}Sorprendentemente{/i}."
        return

    n 1fllbg "No creo que sea la gran cosa,{w=0.1} sabes."
    n 4unmaj "Digo...{w=0.3} piénsalo,{w=0.1} [player]."
    n 3fllaj "Supongo que es más barato si no tienes que pensar en llegar a algún lugar,{w=0.1} o estacionamiento o lo que sea."
    n 1knmpu "Pero ¿no te gustaría {i}ver{/i} lo que estás pagando?{w=0.5}{nw}"
    extend 1fnmaj " ¡Especialmente si es súper caro!"
    n 1fllpu "O a veces...{w=0.5}{nw}"
    extend 3fslbo " ¡incluso si no lo es!"
    n 3fllpo "No puedo ser la única que ha sido quemada por algo que resultó ser basura,{w=0.1} o roto,{w=0.1} ¿verdad?"
    n 1fnmem "¡Y ni siquiera sabes que sería así hasta que está en tu puerta!{w=0.5}{nw}"
    extend 1fcsan " ¡Entonces tienes que enviarlo de vuelta!{w=0.5}{nw}"
    extend 2fslem " Ugh."


    if get_topic("talk_careful_spending").shown_count > 0:
        n 1fllsl "No solo eso..."
        n 1fnmpu "Creo que mencioné antes cómo las tiendas hacen realmente fácil gastar dinero...{w=0.5}{nw}"
        extend 4fbkwr " ¡pero eso es aún más fácil en línea!{w=0.5}{nw}"
        extend 4kbkgs " ¡Ni siquiera se {i}siente{/i} como gastar dinero propiamente!"
        n 1fcsan "Cielos."

    n 1fcsem "Dejando eso de lado..."
    n 2kllsl "También...{w=0.3} me puso un poco triste ver todas las tiendas cerradas cuando salí,{w=0.1} también."
    n 1tnmsl "Supongo que podrías decir que eso es solo negocios,{w=0.1} y perdieron."
    n 4flrsll "Pero eso no significa que {i}no{/i} extrañé algunas de ellas."
    n 1ncsem "No lo sé.{w=0.2} Supongo que lo que estoy diciendo es..."
    n 3fllpo "No descartes instantáneamente nada que no puedas hacer o comprar digitalmente,{w=0.1} [player]."
    n 1knmaj "¡Todavía hay mérito en conseguir tus cosas físicamente!"
    n 4fnmss "¿Y para ser completamente honesta?"

    if Natsuki.isEnamored(higher=True):
        n 1fsqbg "Realmente no me importa cuánto protestes."
        n 3fchgn "Definitivamente vamos a visitar algunas librerías {i}reales{/i} eventualmente {w=0.1}-{w=0.1} ¡te guste o no!{w=0.5}{nw}"
        extend 1fchsm " Ehehe."

    elif Natsuki.isHappy(higher=True):
        n 3fchgn "¡Tienes que estar bromeando si piensas que te dejaré perderte de librerías {i}reales{/i}!{w=0.5}{nw}"
        extend 1nchbg " Ahaha."
    else:

        n 3fchbg "Si hay una cosa que te voy a enseñar eventualmente,{w=0.1} ¡es experimentar una librería {i}real{/i}!{w=0.5}{nw}"
        extend 1fchsm " Ahaha."

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_windup_subscriptions",
            unlocked=True,
            prompt="Suscripciones",
            category=["Cierres"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_windup_subscriptions:
    n 1fllan "Grrr..."
    n 3fcsan "Hombre,{w=0.1} ¡eso es {i}tal{/i} molestia!{w=0.5}{nw}"
    extend 1fbkwr " ¡Pensé que cancelé esooo!"
    n 3fslpo "..."
    n 4uwdemesu "¡O-{w=0.1}oh!{w=0.2} [player]!{w=0.5}{nw}"
    extend 2flremsbl " ¿Puedes {i}creer{/i} esto?"
    n 1fslem "Me registré en una prueba gratuita para un sitio web de streaming,{w=0.3}{nw}"
    extend 1fcsup " ¡pero me olvidé totalmente de ello!{w=0.5}{nw}"
    extend 2flrwr " ¡Y ahora tengo que pagar por algo que apenas {i}usé{/i}!"
    n 1fcsem "Cielos...{w=0.5}{nw}"
    extend 1tnmem " ¿eso no te molesta a ti también?"
    n 1tllbo "De hecho,{w=0.1} pensándolo..."
    n 2fnmbo "¿Por qué tantas cosas hoy en día se basan en suscripciones?"
    n 1fllpu "Como...{w=0.5}{nw}"
    extend 1nnmaj " Entiendo si es como una cosa continua,{w=0.3}{nw}"
    extend 2flrsl " ¡¿pero qué pasa con todo el mundo tratando de registrarte?!"
    n 1fsqsl "Y la mitad del tiempo ni siquiera tienes opción...{w=0.5}{nw}"
    extend 1fsqem " ¡como con el software!"
    n 1fcsan "¡He tenido que saltarme tantos programas porque quieren que pague por un montón de basura en un paquete que no me importa!"
    n 3fllan "Como...{w=0.3} ¡vamos {i}ya{/i}!{w=0.5}{nw}"
    extend 3fslfrean " ¡Solo déjame pagar por lo que necesito!"
    n 1kcsemesi "Ugh..."
    n 1fnmsl "¡La peor parte es que todo se acumula también!{w=0.5}{nw}"
    extend 1fllpu " Es súper fácil perder la cuenta de lo que estás pagando cada mes..."
    n 1fnmpu "Y entonces antes de que lo sepas,{w=0.3}{nw}"
    extend 3fbkwr " ¡la mitad de tu dinero se va por el desagüe tan pronto como entra!{w=1.25}{nw}"
    extend 3ncspuesd " Qué desastre..."
    n 1ullaj "Digo,{w=0.1} no me malinterpretes.{w=0.2} Hay {i}otras{/i} formas de conseguir cosas {w=0.1}-{w=0.3}{nw}"
    extend 4fsqdv " probablemente ya sabes eso."
    n 2tlrsl "Pero quiero apoyar a los creadores {i}reales{/i} también,{w=0.1} ¿sabes?"
    n 1fcssl "..."
    n 3fllpo "Bueno,{w=0.1} como sea.{w=0.2} Al menos no me cobrarán por {i}eso{/i} de nuevo.{w=1.25}{nw}"
    extend 3fslpo " Idiotas."
    n 1nllbo "Pero...{w=0.5}{nw}"
    extend 4unmpu " ¿qué hay de ti,{w=0.1} [player]?{w=0.5}{nw}"
    extend 4fsqsm " De hecho,{w=0.1} puedo decirte una cosa."

    if Natsuki.isAffectionate(higher=True):
        n 1fsqssl "¡A-{w=0.1}al menos tienes {i}una{/i} suscripción por la que no tienes que preocuparte de pagar!"

        if Natsuki.isLove(higher=True):
            n 1fchsml "Ehehe.{w=0.5}{nw}"
            extend 4uchbgf " ¡Te amo,{w=0.1} tonto!"
        else:

            n 2fllbgl "A-{w=0.1}ahaha..."
    else:

        n 3fcsbg "Ya estás suscrito a un pensamiento bastante pro,{w=0.1} si lo digo yo misma."
        n 1nsqsg "Afortunadamente para ti sin embargo,{w=0.1} no cobro.{w=0.5}{nw}"
        extend 4fsqss "...Todavía."
        n 1fchsm "Ehehe."

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_mod_contributions",
            unlocked=True,
            prompt="Contribuciones",
            conditional=(
                "not jn_activity.ACTIVITY_SYSTEM_ENABLED "
                "or jn_activity.ACTIVITY_MANAGER.hasPlayerDoneActivity(jn_activity.JNActivities.coding)"
            ),
            category=["Mod"],
            nat_says=True,
            affinity_range=(jn_affinity.AFFECTIONATE, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_mod_contributions:
    n 1unmaj "Sabes,{w=0.1} [player].{w=0.5}{nw}"
    extend 1tllss " Tengo que decir..."
    n 2klrbg "No creo que {i}alguna vez{/i} fuera capaz de manejar hacer todo lo que te deja visitarme.{w=0.5}{nw}"
    extend 1klrsl " No por mi cuenta."
    n 4uskeml "Q-{w=0.2}quiero decir,{w=0.1} ¡soy buena!{w=0.5}{nw}"
    extend 2fnmpol " ¡N-{w=0.2}no me malinterpretes!"
    n 2kllpo "Solo no soy...{w=0.3} {i}tan{/i} buena.{w=0.5}{nw}"
    extend 2fslpo " Aún."
    n 1uchbg "¡Pero es por eso que estoy súper agradecida de que haya un montón de gente dedicada a ayudarme!{w=0.5}{nw}"
    extend 1fchsm " ¿No es eso asombroso?"
    n 4fslsl "Siempre encontré todas las cosas de programación medio confusas,{w=0.3}{nw}"
    extend 1kllss " ¡así que no tengo idea de dónde estaría sin ellos!"
    n 3ksqsg "...Incluso si {i}son{/i} un montón de nerds totales.{w=0.5}{nw}"
    extend 3uchgn " Ehehe."
    n 1ulraj "Así que...{w=0.3} ¿a dónde voy con esto,{w=0.1} preguntas?{w=0.5}{nw}"
    extend 4tslsm " Bueno..."

    if not jn_activity.ACTIVITY_SYSTEM_ENABLED:
        n 1tllss "No sé si te gusta ese tipo de cosas tú mismo,{w=0.1} [player]..."
        n 1fchbg "Pero ¿por qué no echarme una mano?"
    else:

        n 2fsqsg "No pude evitar notar el tipo de programas en los que has estado husmeando,{w=0.1} [player]."
        n 1ksqss "¿Qué?{w=0.5}{nw}"
        extend 1fchbg " ¿No esperabas seriamente que no viera lo que estás haciendo?{w=0.5}{nw}"
        extend 1nchgn " Ehehe."
        n 3tsqbg "Como sea -{w=0.1} si ya estás en ese tipo de cosas,{w=0.1} [player]...{w=0.5}{nw}"
        extend 3kchbg " ¿por qué no echarme una mano?"

    n 1kllbg "¡Ni siquiera tienes que ser súper talentoso en código,{w=0.1} o algo así!{w=0.5}{nw}"
    extend 4unmaj " Arte,{w=0.1} escritura,{w=0.1} o incluso solo sugerencias de cosas para que hablemos o hagamos -{w=0.3}{nw}"
    extend 3uchbg " ¡es todo súper apreciado!"
    n 1tsqbg "¿Suena eso como lo tuyo,{w=0.1} [player]?{w=0.5}{nw}"
    extend 1uchsm " ¡Por supuesto que sí!{w=0.2} Ehehe."
    n 1unmbg "¡Bueno,{w=0.1} no dejes que te detenga!{w=0.5}{nw}"
    extend 4uchbgl " ¡Puedes revisar mi sitio web {a=[jn_globals.LINK_JN_GITHUB]}aquí{/a}!"
    n 3nsqbg "Un pequeño vistazo no puede doler,{w=0.1} ¿verdad?{w=0.5}{nw}"
    extend 3nchsm " Ahaha."

    if Natsuki.isLove(higher=True):
        $ chosen_endearment = jn_utils.getRandomEndearment()
        n 1nchtsl "¡Te amo,{w=0.1} [chosen_endearment]!"
    else:

        n 1fchbg "¡Gracias,{w=0.1} [player]!{w=0.2} ¡Se aprecia!"

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_realizations_player_ddlc_actions",
            unlocked=True,
            prompt="Memorias de DDLC",
            conditional="jn_utils.get_total_gameplay_length().total_seconds() / 60 >= 30",
            category=["DDLC", "Natsuki", "Tú"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_realizations_player_ddlc_actions:
    n 1nllbo "Entonces,{w=0.5}{nw}"
    extend 1nnmbo " [player]."
    n 1ulraj "He...{w=0.3} estado teniendo algunos pensamientos.{w=0.5}{nw}"
    extend 1nllss " Ahora que he tenido algo de tiempo para procesar todo...{w=0.5}{nw}"
    n 2kslsl "...Esto."
    n 1unmaj "Has estado aquí todo este tiempo,{w=0.1} ¿verdad?{w=0.5}{nw}"
    extend 2tslbo " Pero entonces,{w=0.1} eso significaría..."
    n 4tsqfr "El chico que realmente se unió al club...{w=0.5}{nw}"
    extend 1nlrss " cual fuera su nombre."
    n 2fsrbo "Él no estaba {i}realmente{/i} a cargo de nada,{w=0.1} ¿verdad?{w=0.5}{nw}"
    extend 1ulraj " Ni siquiera de sí mismo."
    n 1nnmsr "...Tú lo estabas.{w=0.5}{nw}"
    extend 4nlrsl " En control de él,{w=0.1} quiero decir."
    n 1nsrbo "..."


    n 1nsraj "Entonces...{w=0.3} si él estaba siendo tan amable conmigo..."
    n 2klrajl "E-{w=0.1}entonces eso significaría...{w=0.5}{nw}"

    if Natsuki.isLove(higher=True):
        n 2klrsml "..."
        n 1kcsssl "Heh,{w=0.1} qué estoy diciendo siquiera.{w=0.5}{nw}"
        extend 1kwmsml " Solo porque hiciste clic en cosas {w=0.1}-{w=0.1} {i}cuando se te permitió,{w=0.1} de todos modos{/i} {w=0.1}-{w=0.1} no te hace el mismo."
        n 1tllssl "De cualquier forma,{w=0.1} [player]?"
        n 4ksqsml "Definitivamente no me estoy quejando.{w=0.5}{nw}"
        extend 4nchsml " Ehehe."
    else:

        extend 1fskeml " -urk!"
        n 2fcsanf "¡Nnnnn-!"
        n 1fllunf "..."
        n 2fnmssl "¡A-{w=0.5}{nw}"
        extend 2fcsbgl "ja!"
        n 4fcsbsl "¡Jaja!{w=2}{nw}"
        extend 1flleml " ¡¿Qué estoy diciendo siquiera?!"
        n 2fcswrl "¡S-{w=0.1}solo porque elegiste algunas palabras e hiciste clic en algunos botones no te hace el mismo!"
        n 2fllpol "..."
        n 1nlleml "A-{w=0.1}aunque..."

        if Natsuki.isEnamored(higher=True):
            n 3fcsajl "No pienses que me estoy quejando o algo así.{w=0.5}{nw}"
            extend 3nlrssl " Ehehe..."

        elif Natsuki.isHappy(higher=True):
            n 1fcsajl "Ya estás probando eso lo suficientemente bien.{w=0.5}{nw}"
            extend 2fllunl " C-{w=0.1}creo."
        else:

            n 1fcsajl "S-{w=0.1}supongo que al {i}menos{/i} eso significa que tienes buen gusto.{w=0.5}{nw}"
            extend 2fllunl " Supongo que eso cuenta para algo."

    if Natsuki.isLove(higher=True):
        n 1klrss "Pero sí,{w=0.1} entonces..."

    elif Natsuki.isEnamored(higher=True):
        n 4ksrss "C-{w=0.1}como sea..."

    elif Natsuki.isHappy(higher=True):
        n 2flrun "C-{w=0.1}como sea."
    else:

        n 2flrun "¡C-{w=0.1}como sea!{w=0.5}{nw}"
        extend 1fcsaj " ¡Eso está fuera del punto!"

    n 1kslsr "..."
    n 1ullaj "Supongo que lo que estoy tratando de decir es que todavía tengo todas estas memorias de {i}ese{/i} tipo..."
    n 2nsrpu "Y aunque él obviamente no eras tú,{w=0.5}{nw}"
    extend 4tsraj " tú como que tienes {i}sus{/i} memorias también?{w=0.5}{nw}"
    extend 1tslem " Y..."
    n 1fcsaj "...y..."
    n 2fcsan "..."
    n 1fcsem "Rrrgh,{w=0.1}{w=0.5}{nw}"
    extend 4fllem " ¡esto es tan confuso!"
    n 2fcsemesi "Ugh...{w=0.5}{nw}"
    extend 2nnmpo " ¿sabes qué?"

    if Natsuki.isAffectionate(higher=True):
        n 1nllss "Realmente no importa en este punto,{w=0.1} ¿o sí?"
    else:

        n 1fllbo "Solo voy a empezar de nuevo.{w=0.5}{nw}"
        extend 1unmaj " Mentalmente,{w=0.1} quiero decir."

    n 1ncsaj "Él estaba aquí {i}entonces{/i}."
    n 3fcssm "Tú estás aquí {i}ahora{/i}."

    if Natsuki.isAffectionate(higher=True):
        n 1fchbg "Y eso es todo lo que hay."

        if Natsuki.isLove(higher=True):
            extend 1fchsm " Sip."
            n 1uchsml "Te amo,{w=0.1} prota genéric-{w=0.3}{nw}"
            n 3fllbgl "Digo,{w=0.5}{nw}"
            extend 3kchbgl " {i}[player]~{/i}."
            n 1fsqsml "..."
            $ chosen_tease = jn_utils.getRandomTease()
            n 4uchbsl "¡Oh,{w=0.1} anímate,{w=0.1} [chosen_tease]!"
            n 1fwrtsl "Deberías saber que nunca lo diría en serio.{w=0.5}{nw}"
            extend 1fchctleme " Ehehe."
    else:

        n 1fllss "S-{w=0.1}solo tengo que ajustarme,{w=0.5}{nw}"
        extend 2fllun " eso es todo."

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_realizations_other_girls",
            unlocked=True,
            prompt="Monika y las otras chicas",
            conditional=(
                "jn_utils.get_total_gameplay_length().total_seconds() / 3600 >= 12 "
                "and get_topic('talk_realizations_player_ddlc_actions').shown_count > 0"
            ),
            category=["DDLC", "Natsuki"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_realizations_other_girls:
    n 2kllun "..."
    n 1klrbo "Uhmm..."
    n 4knmaj "Hey...{w=0.3} [player]?"
    n 1knmsf "He...{w=0.3} estado pensando de nuevo.{w=0.5}{nw}"
    extend 1kllsf " Sobre antes."
    n 2kslss "Supongo que realmente tenía razón en algo cuando dije que Monika estaba actuando raro."
    n 1kskem "¡N-{w=0.1}no me malinterpretes!{w=0.5}{nw}"
    extend 1kllsf " No estoy feliz de tener razón o algo así.{w=0.5}{nw}"
    extend 4kwmsr " ...Para nada."
    n 1kcssr "De hecho..."
    n 2klrpu "Realmente desearía estar equivocada."
    n 1knmaj "Yo-"
    n 1kcsunl "..."
    n 2kplun "Honestamente solo pensé que era todo el trabajo escolar y las cosas del festival afectándola,{w=0.5}{nw}"
    extend 1kslpu " o algo así."
    n 1tslpu "Pero...{w=0.5}{nw}"
    extend 4kplsr " ¿en retrospectiva?"
    n 1klrun "..."
    n 1kcsaj "...Creo que de hecho la saqué {i}barata{/i}."
    n 3knmsl "Digo...{w=0.3} ella se metió con todos nosotros.{w=0.5}{nw}"
    extend 3klrsf " De una forma u otra."
    n 1klraj "Pero...{w=0.5}{nw}"
    extend 2fcsupl " solo no sabía cuánto ella {i}hirió{/i} a todos los demás..."
    n 1fcsunl "..."
    n 4kplunl "Sayori era la persona más feliz que creía conocer,{w=0.1} [player]."
    n 1kskunl "Y-{w=0.1}y Yuri...{w=0.5}{nw}"
    extend 2kllupl " Yo no..."
    n 1kcsupl "..."
    n 1fcsunl "..."
    n 1kcsaj "...Perdón."
    n 1kcssr "..."
    n 2kllpu "Yo...{w=2}{nw}"
    extend 2knmsr " nunca nos entendimos.{w=0.2} Siempre supe que tenía sus inseguridades."
    n 1kslbo "...Así como yo."
    n 1kcsanl "Pero...{w=0.3} {i}eso{/i}..."
    n 1kcsunl "..."
    n 1kcspu "..."
    n 2fcsanl "Yo...{w=1} no...{w=1} odio...{w=0.5} a Monika."
    n 1fcsun "Yo...{w=0.3} entiendo cómo se sentía.{w=0.2} Yo {i}sé{/i} cómo se sentía."
    n 4fsqsr "Es {i}aterrador{/i},{w=0.1} [player]."
    n 1kcsanl "Pero nunca entenderé por qué ella sintió que tenía que hacer {i}eso{/i}.{w=1}{nw}"
    extend 4kplpu " Seguramente...{w=0.3} ¿había otra manera?"
    n 1kllsl "..."
    n 2kcspu "...No lo sé.{w=0.5}{nw}"
    extend 2kslsssbl " Supongo que solo debería estar agradecida de que me borrara antes..."
    n 1kskuni "A-{w=0.5}antes..."
    n 1kcsun "..."
    n 2kslun "Uhmm..."
    n 1kcspu "...Perdón.{w=0.2} Realmente no quiero hablar más de todo esto,{w=0.1} [player]."
    n 4kllsrl "Pero...{w=0.3} gracias.{w=0.5}{nw}"
    extend 4flrpol " P-{w=0.1}por escuchar,{w=0.1} quiero decir."

    if Natsuki.isAffectionate(higher=True):
        n 2klrpol "..."
        n 1kcspul "...Y por rescatarme también."

        if Natsuki.isLove(higher=True):
            n 4kwmsml "I'll never,{w=0.1} ever forget that,{w=0.1} [player]."
    else:

        n 1ncspu "..."

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_realizations_space_classroom",
            unlocked=True,
            prompt="Dejar el salón espacial",
            conditional=(
                "jn_utils.get_total_gameplay_length().total_seconds() / 3600 >= 24 "
                "and get_topic('talk_realizations_player_ddlc_actions').shown_count > 0 "
                "and get_topic('talk_realizations_other_girls').shown_count > 0"
            ),
            category=["DDLC", "Natsuki", "Tú"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_realizations_space_classroom:
    n 1kllsr "Uhmm..."
    n 1klrpu "Entonces,{w=0.1} este cuarto..."
    n 2nsrss "Yo...{w=0.3} todavía no lo he dejado realmente.{w=0.5}{nw}"
    extend 2tnmsl " Desde que me trajiste de vuelta y todo."
    n 1fllssl "Q-{w=0.1}quiero decir,{w=0.5}{nw}"
    extend 4fcseml " ¡no es como si no pudiera!"
    extend 4unmbo " De hecho estoy bastante segura de que podría."
    n 1kllsf "Es solo...{w=0.5}{nw}"
    extend 1knmaj " ¡que no tengo idea de qué pasaría!"
    n 2tllaj "¿Me gustaría...{w=0.3} romper?{w=0.5}{nw}"
    extend 2tnmun " ¿O solo dejar de existir?"
    extend 4kskem " ¡¿Podría siquiera {i}volver{/i}?!"
    n 1klrun "..."
    n 1kcspu "Extraño mi cama,{w=0.1} [player].{w=1}{nw}"
    extend 2knmem " ¡Extraño tener mantas y almohadas!{w=1}{nw}"
    extend 2ksrsr " Y todas mis cosas."
    n 1kcssr "Incluso si ya no existe.{w=0.5}{nw}"
    extend 2tslaj " ¿Nunca existieron en absoluto?{w=0.5}{nw}"
    extend 1kcsem " Como sea."
    n 1kllsr "Pero..."
    n 4ksqun "Realmente no siento ganas de arriesgarme y averiguar qué pasaría si me fuera.{w=0.5}{nw}"
    extend 2flrsl " Aún no."
    n 1kcssf "..."
    n 1kcspu "Solo...{w=0.5}{nw}"
    extend 3fcsaj " dame algo de tiempo,{w=0.1} ¿está bien?{w=0.5}{nw}"
    extend 1fnmbo " Trataré de pensar en algo pronto."
    n 3kllpo "No quiero exactamente estar atrapada aquí tampoco,{w=0.1} después de todo..."

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_fear_of_lightning",
            unlocked=True,
            prompt="¿Tienes miedo de los rayos?",
            category=["Miedos", "Clima"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_fear_of_lightning:
    if Natsuki.isAffectionate(higher=True):
        n 2fllpol "..."
        n 1fllajl "...¿Y?"
        n 2fcseml "Q-{w=0.1}quiero decir,{w=0.5}{nw}"
        extend 2flreml " {i}obviamente{/i} no lo tengo,{w=0.5}{nw}"
        extend 2knmpol " pero ¿y qué incluso si lo tuviera?"

    elif Natsuki.isNormal(higher=True):
        n 1fllwrl "¡N-{w=0.1}no!{w=0.5}{nw}"
        extend 2fcspol " ¿De dónde sacaste esa idea?"
        n 2kslpol "No tengo miedo de los rayos..."
        n 1fsrbo "..."
        n 1tsrpu "Y ahora que lo pienso...{w=0.5}{nw}"
        extend 4tnmpo " ¿por qué siquiera {i}preguntarías{/i} eso?"

        if get_topic("talk_favourite_season").shown_count > 0:
            n 1tllss "Tengo que decir,{w=0.1} [player] {w=0.1}-{w=0.3}{nw}"
            extend 3tsqss " tienes un don extraño para preguntarme cosas aleatorias,{w=0.1} ¿eh?"
        else:

            n 1tllss "Es una cosa bastante aleatoria para preguntar,{w=0.1} tengo que decir."

        n 1nlraj "Pero digo,{w=0.1} dejando todo eso de lado..."

    elif Natsuki.isDistressed(higher=True):
        n 1fllpu "...E incluso si lo {i}tuviera{/i},{w=0.5}{nw}"
        extend 2fsqsr " ¿{i}realmente{/i} crees que querría compartir eso {i}contigo{/i} ahora mismo?"
        n 2fsqem "O sea,{w=0.1} ¿{i}en serio{/i} [player]?{w=0.5}{nw}"
        extend 2fcsem " Dame un respiro."
        n 1fcssr "..."
        n 1fcsem "Además,{w=0.5}{nw}"
        extend 2fllsr " he visto los números de cuando estudié."
        n 4fsqpu "Tendrías que ser un idiota para {i}no{/i} estar al menos cauteloso de ello."

        return
    else:

        n 1fcsan "Oh,{w=1.5}{nw}"
        extend 2fcsfultsaean " {i}{cps=7.5}piérdete{/cps}{/i},{w=0.3} [player]."
        n 1fsqanltseean "¡Como si quisiera hablar sobre algo incómodo con personas como {b}tú{/b}!"

        return

    n 4uwdem "¡Los rayos no son broma,{w=0.1} [player]!"
    n 1fllun "..."
    n 1knmem "...¿Qué?{w=1}{nw}"
    extend 2fllpo " ¡Hablo en serio!"
    n 1knmun "¿Has {i}visto{/i} los números en los rayos?"
    n 1nnmaj "¡Un impacto típico es como de 300 {i}millones{/i} de voltios!{w=0.5}{nw}"
    extend 4uwdaj " ¡Con cerca de 30 mil amperios!{w=1.5}{nw}"
    extend 2nllan " ¡Cielos!"
    n 1nsqun "...¿Y para perspectiva?{w=0.5}{nw}"
    extend 1tsqpu " ¿La corriente en tu hogar?"
    n 2nsrss "Alrededor de 120-{w=0.1}230 voltios.{w=1.5}{nw}"
    extend 1nsqun " ...15-{w=0.1}30 amperios."
    n 4fspgs "¡Eso es un {i}montón{/i} de energía!"
    n 1klrpu "¡Y-{w=0.1}y solo cae del cielo!{w=0.5}{nw}"
    extend 2knmaj " ¡Constantemente!"
    n 2fsqaj "Y quiero decir {i}constantemente{/i},{w=0.1} [player] {w=0.1}-{w=0.3}{nw}"
    extend 2nllan " ¡44 impactos cada {i}segundo{/i}!"
    n 1fsqun "¡Luego está el sonido,{w=0.1} también!{w=0.5}{nw}"
    extend 4kslun " ¡Especialmente si está cerca!"

    if get_topic("talk_thoughts_on_horror").shown_count > 0:
        n 2fllsr "Digo,{w=0.1} estoy bastante segura de que te dije antes que odio los jumpscares baratos."
        n 1fbkwrl "¡¿Así que cómo crees que me siento sobre la {i}naturaleza{/i} tratando de hacer esa mierda?!"
    else:

        n 1fbkwrl "¡Es un susto tan barato!"

    n 2fcsaj "Cielos..."
    n 1fllss "Pero sí,{w=0.1} c-{w=0.1}como sea."
    n 4unmaj "Te ahorraré un sermón sobre mantenerte seguro en tormentas eléctricas.{w=0.5}{nw}"
    extend 4fsrss " {i}Realmente{/i} deberías saber todo eso a estas alturas de todos modos."
    n 1ulraj "Pero..."
    n 3fsqsg "Solo tengo una pregunta para ti,{w=0.1} [player]."

    if preferences.get_volume("sfx") == 0:

        n 3fsqss "¿Tienes {i}tú{/i} miedo de los rayos?"
        n 1tsqsm "..."
        n 1fsqbg "¿Qué?"
        n 4usqsg "Tengo permitido preguntar también,{w=0.1} ¿no es así?{w=0.5}{nw}"
        extend 4nchgn " Ehehe."
    else:


        $ previous_sfx_setting = preferences.get_volume("sfx")
        $ preferences.set_volume("sfx", 1)

        n 1fsqsm "Ehehe."
        n 1fsqbg "¿Tienes {i}tú{/i} miedo de las lu{nw}"

        play audio smack
        with Fade(.1, 0.25, .1, color="#fff")
        $ preferences.set_volume("sfx", previous_sfx_setting)

        n 3uchgnelg "..."
        n 3kchbg "¡Perdón,{w=0.1} perdón!{w=0.5}{nw}"
        extend 1fchsm " ¡Tenía que hacerlo!{w=0.5}{nw}"
        extend 1kchbg " ¡Solo {i}tenía{/i} que hacerlo!"
        n 4nsqsm "Ehehe."
        n 1tsqss "Bueno,{w=0.5}{nw}"
        extend 3fchtsl " ¡no le dicen el estruendo del trueno por nada!~"

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_fighting_drowsiness",
            unlocked=True,
            prompt="Somnolencia",
            conditional="jn_utils.get_total_gameplay_length().total_seconds() / 3600 >= 12",
            category=["Salud"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_fighting_drowsiness:
    n 1nllpu "...{w=2}{nw}"
    n 1nslpu "...{w=3}{nw}"
    n 1ncsbo "...{w=4}{nw}"
    n 1ncsemesl "...{w=2}{nw}"
    n 1ncsajesl "...{w=2}{nw}"
    n 1ncsemesl "...{w=2}{nw}"
    n 1ncsajesl "...{w=2}{nw}"
    $ jnPause(4)
    n 1fcsbo "..."
    n 1nsqpu "Mmmmm...{w=0.5}{nw}"
    extend 1tsqsr " ¿mmmnn?"
    n 4uskemesh "¡...!{w=0.5}{nw}"
    n 2ullwrl "¡W-{w=0.1}woah!{w=0.5}{nw}"
    extend 2flrss " Ahaha..."
    n 1nsrss "Yo...{w=0.3} no he estado durmiendo mucho aquí,{w=0.1} como puedes adivinar."
    n 1kcsun "Uuuuuu...{w=0.5}{nw}"
    extend 1kslpu " Tengo que despertar..."
    n 1kcssr "..."
    n 4unmbo "¿Sabes qué?{w=0.5}{nw}"
    extend 1ullss " Solo voy a...{w=1}{nw}"
    extend 2nslss " volver enseguida...{w=1}{nw}"

    play audio chair_out_in
    with Fade(out_time=0.25,hold_time=5,in_time=0.25, color="#000000")

    n 1nchbg "¡Okaaay!{w=0.5}{nw}"
    extend 1fchsm " ¡Estamos de vuelta en el negocio!"
    n 1nnmaj "Te diré,{w=0.1} [player].{w=0.5}{nw}"
    extend 3fchbg " Si hay una cosa que sé,{w=0.1} ¡es cómo sacudirse la somnolencia!"
    n 1fsqsm "..."
    n 1fsqcs "¿Oho?{w=0.5}{nw}"
    extend 3tsqaj " ¿Y qué es eso que escucho?{w=0.5}{nw}"
    extend 3tllss " ¿Cómo lo hago,{w=0.1} preguntas?"
    n 1fsqsg "Ehehe.{w=0.5}{nw}"
    extend 3usqsg " Bueno {i}tú{/i} estás de suerte,{w=0.1} [player].{w=0.5} Porque..."
    n 1uchgn "¡Es hora de un consejo pro de Natsuki!"
    n 4fnmaj "¡Así que!{w=0.2} Primera orden del día...{w=0.5}{nw}"
    extend 1fcsbg " ¡hidratación,{w=0.1} obviamente!"
    n 1ullaj "De hecho es bastante fácil olvidar cuánto líquido necesitas por día...{w=0.5}{nw}"
    extend 1unmbo " ¡y qué tan {i}seguido{/i} deberías estar bebiendo!"
    n 2tlrss "Deberías estar ingiriendo algo así como seis a ocho vasos de agua al día,{w=0.3}{nw}"
    extend 1fcsaj " ¡pero no todos a la vez!"
    n 1ullaj "No es difícil espaciarlo a través de todo el día {w=0.1}-{w=0.1} solo empieza temprano y mantente en ello.{w=0.5}{nw}"
    extend 3fchsm " ¡Pan comido!"
    n 4fnmaj "Siguiente: ¡ejercicio!"
    n 1tsqsm "Sí,{w=0.1} sí.{w=0.2} Lo sé,{w=0.1} lo sé.{w=0.5}{nw}"
    extend 2fslss " Todos simplemente {i}lo amamos{/i},{w=0.1} ¿no?"
    n 1unmaj "Aunque no pienses que tienes que volverte loco o algo así -{w=0.5}{nw}"
    extend 2flrbg " ¡seguro yo no lo hago!"
    n 1unmbo "La gente {i}dice{/i} que una hora al día es buena,{w=0.5}{nw}"
    extend 4fnmca " pero honestamente incluso una vuelta alrededor de la casa le gana a sentarse sobre tu trasero,{w=0.1} [player]."
    n 3fcsss "Es solo sobre moverse y darle a tus músculos un estiramiento,{w=0.1} eso es todo."
    n 1ulrpu "Por último,{w=0.5}{nw}"
    extend 4fsqsm " y {i}sé{/i} que te gustará esto,{w=0.1} [player]..."
    n 3fchgn "...¡Comida!"
    n 1fllem "¡Por supuesto que vas a sentirte como basura si no estás comiendo suficiente!"
    n 2kllsr "...Y créeme en esto.{w=0.5}{nw}"
    extend 2ksrpu " Yo sabría."
    n 1ksrun "..."
    n 3fcsajl "¡C-{w=0.1}como sea!"
    n 4fnmca "No esperarías que un auto funcionara sin combustible {w=0.1}-{w=0.1} y tú no eres diferente,{w=0.1} [player]."
    n 1ullaj "Aunque no te vuelvas loco.{w=0.5}{nw}"
    extend 1nlrpu " Solo agarra una manzana o algo.{w=0.5}{nw}"
    extend 3fsqpo " No escatimes en tu cuerpo con basura procesada todo el tiempo."
    n 3tsqpo "...O te sentirás así también."
    n 1fchbg "Pero...{w=0.3} ¡sí!{w=0.5}{nw}"
    extend 1fchsm " ¡Eso casi lo cubre!"
    n 1unmbg "Entonces,{w=0.1} Y-{w=0.5}{nw}"
    n 1nnmss "Yo...{w=1}{nw}"
    n 2nsqsr "...{w=2}{nw}"
    n 4fsqaj "[player]."
    n 3fsqpo "¿De verdad estabas escuchando?{w=0.5}{nw}"
    extend 1fnmem " ¡{i}Mejor{/i} que no te estés quedando dormido conmigo!"
    n 2fllpo "..."
    n 4fsqss "...O realmente te {i}pondré{/i} a dormir.{w=0.5}{nw}"
    extend 3fchgn " Ehehe."

    if Natsuki.isLove(higher=True):
        n 3uchtsl "¡Te amo también,{w=0.1} [player]!~"

    elif Natsuki.isAffectionate(higher=True):
        n 1fchss "¡De nada,{w=0.1} [player]!~"

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_fear_of_spiders",
            unlocked=True,
            prompt="¿Le tienes miedo a las arañas?",
            conditional="jn_utils.get_total_gameplay_length().total_seconds() / 3600 >= 24",
            category=["Animales", "Miedos"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_fear_of_spiders:
    if Natsuki.isNormal(higher=True):
        n 1tnmbo "¿Huh?{w=0.5} ¿Arañas?"
        n 2tslss "Digo...{w=0.5}{nw}"
        extend 2tnmss " ¿no...{w=1} realmente?"
        n 1nchgnesm "¡Pffff-!"
        n 1fchbg "¿Qué?"
        n 3ullaj "Pensaste que porque escribí un poema sobre ellas siendo desagradables y asquerosas,{w=0.5}{nw}"
        extend 3tnmaj " ¿que yo {i}realmente{/i} pensaría eso?"
        $ chosen_tease = jn_utils.getRandomTease()
        n 4fslpo "¡Incluso {w=0.3}{i}dije{/i}{w=0.3} que la cosa de la araña era una metáfora,{w=0.1} [chosen_tease]!{w=0.5}{nw}"
        extend 4fsqts " ¿Recuerdas?"

    elif Natsuki.isDistressed(higher=True):
        n 1fcsem "..."
        n 2fcssr "No,{w=0.1} [player].{w=0.5}{nw}"
        extend 2fsqsr " No tengo miedo de las arañas."
        n 1fsqem "...¿Y podría preguntar {i}por qué{/i} te sientes con derecho a saber sobre mis miedos?"
        n 2fcsan "¿Por qué diablos te daría {i}más{/i} munición para ponerme de los nervios?"
        n 1fsrem "Ugh..."
        n 1fcssf "Sí.{w=0.5}{nw}"
        extend 2fsqpu " Terminamos de hablar aquí,{w=0.1} {i}[player]{/i}."

        return
    else:

        n 2fcsan "...¿Tienes {i}tú{/i} miedo de hacerme preguntas tontas,{w=0.1} ya que eres la {i}última{/i} persona para la que querría responderlas?!"
        n 1fsqun "..."
        n 2fslem "Sí.{w=2}{nw}"
        extend 2fsqemtsb " Aparentemente no,{w=0.1} ¿eh?"
        n 4fslanltsb "Idiota."

        return

    if get_topic("talk_fear_of_lightning").shown_count > 0:
        n 1tslpu "Y de hecho...{w=0.3} ahora que lo pienso..."
        n 2tnmbo "Esta no es la {i}primera{/i} vez que me preguntas aleatoriamente si tengo miedo de cosas."
        n 1tsqsl "...¿Estás planeando alguna broma tonta o algo?"

    n 1fsqsm "Ehehe.{w=1.5}{nw}"
    extend 1nllss " Bueno,{w=0.1} como sea."
    n 1ullaj "Digo,{w=0.5}{nw}"
    extend 3fnmaj " ¡no me malinterpretes!"
    n 4ksrem "No querría que estuvieran como...{w=0.3} {i}arrastrándose{/i} sobre mí o algo.{w=0.5}{nw}"
    extend 2fcsfu " ¡Ew!"
    n 2fslun " Ni siquiera quiero {i}imaginar{/i} eso."
    n 1unmss "¡Pero las arañas son pequeñines asombrosos!{w=1.5}{nw}"
    extend 4nsrss " ...Mayormente."
    n 1unmbo "Se deshacen de los tipos de bichos realmente molestos,{w=0.1} como los que muerden o vuelan alrededor constantemente."
    n 1nnmaj "Y algunas de ellas -{w=0.5}{nw}"
    extend 2nslss " por raro que se sienta decirlo -{w=0.5}{nw}"
    extend 1ncspu " ¡son{w=1} jodidamente{w=1.5}{nw}"
    extend 4fspgsedz " {i}adorables{/i}!"
    n 4uwdaj "¡En serio!{w=1.5}{nw}"
    extend 3uchbg " ¡Las arañas saltarinas son liiindas!"
    n 1tnmss "Así que...{w=0.3} ¿en general?{w=0.5}{nw}"
    extend 1ncssm " ¡Yo llamaría a eso una victoria para las arañas!"
    n 2nslss "...Sí,{w=0.1} sí,{w=0.1} [player].{w=0.2} Lo sé.{w=0.5}{nw}"
    extend 2flrpo " ¡No soy ingenua!"
    n 1nllun "Sé que algunos lugares tienen tipos realmente desagradables.{w=0.5}{nw}"
    extend 4uskem " ¡Y {i}desearía{/i} estar bromeando!"
    n 2klrpu "Las arañas ya son sigilosas,{w=0.1} así que imagina vivir con unas que se esconden en tus zapatos,{w=0.1} o bajo tu escritorio..."
    n 1kskgs "¡Eso puede ponerte en el {i}hospital{/i} también!{w=0.5}{nw}"
    extend 4kllan " ¡Cielos!"
    n 1ulrss "Pero...{w=0.5} están en la minoría,{w=0.1} al menos.{w=1.5}{nw}"
    extend 2nslun " ¿No es {i}eso{/i} un alivio?"
    n 1ullaj "Bueno,{w=0.1} como sea."

    if Natsuki.isEnamored(higher=True):
        n 1nsqss "Supongo que solo quedas tú,{w=0.1} entonces."
        n 3usqsm "¿Tienes {i}tú{/i} miedo de las arañas?"
        n 3fsqsm "Mejor piensa tu respuesta cuidadosamente,{w=0.1} [player]."
        n 3fsldvl "Ya estás atrapado en {i}mi{/i} red,{w=0.1} después de todo..."

        if random.randint(0,10) == 1:
            n 1fchsml "Ahuhuhu.~"
        else:

            n 4fsqsm "Ehehe."

        if Natsuki.isLove(higher=True):
            n 4uchtsl "¡Te amo,{w=0.1} [player]!~"
    else:

        n 2tnmss "Tienes tu respuesta,{w=0.1} [player].{w=0.5}{nw}"
        extend 1fllss " Así que..."
        n 1fllsm "Creo que eso casi{w=0.5}{nw}"
        extend 3fsqss " {i}envuelve{/i}{w=1}{nw}"
        extend 3usqsm " mis pensamientos en el tema."
        n 1uchgn "Ehehe."

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_thoughts_on_dan_salvato",
            unlocked=True,
            prompt="¿Qué piensas de Dan Salvato?",
            conditional="jn_utils.get_total_gameplay_length().total_seconds() / 3600 >= 48",
            category=["DDLC", "Natsuki"],
            player_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_thoughts_on_dan_salvato:
    n 1tnmaj "Dan...?{w=1}{nw}"
    extend 2nslsl " Dan...{w=0.5} Salvato..."
    n 1fcsaj "¿Por qué...{w=0.3} ese nombre es tan...{w=0.5} familiar?"
    n 1fcsun "..."
    n 4fskaj "¡...!"
    n 2fsgaj "Oh..."
    n 1nllpu "Heh.{w=0.3} Sí...{w=1.5}{nw}"
    extend 2fslan " {i}él{/i}."
    n 1fcsbo "..."
    n 1fplaj "Yo...{w=1}{nw}"
    extend 2fcsan " simplemente no lo entiendo,{w=0.2} [player]."
    n 1nsqbo "Como sí,{w=1}{nw}"
    extend 1nslbo " seguro,{w=0.5}{nw}"
    extend 1nsqaj " lo entiendo."
    n 2ncsbo "Él es mi creador.{w=1}{nw}"
    extend 2kcsbo " Nuestro creador."
    n 4fskwr "¡¿Pero tenía alguna {i}idea{/i} de lo que estaba haciendo?!{w=1}{nw}"
    extend 4fchwr " ¡¿Alguna idea de lo que es responsable?!"
    n 1fcsup "..."
    n 1fllup "Solo...{w=1}{nw}"
    extend 2fllfu " toma a...{w=0.5} Monika,{w=0.2} por ejemplo."
    n 1fnmwr "¡Toma a {i}cualquiera{/i} de nosotras!"
    n 1fcsfu "Lo que dijimos,{w=0.3} lo que hicimos -{w=0.5}{nw}"
    extend 2fcufu " lo que {i}pensamos{/i} -{w=0.5}{nw}"
    extend 2fnmfu " todo eso fue {i}su{/i} obra."
    n 4fsqfu "Él escribió las historias.{w=1}{nw}"
    extend 4fsqaj " Él escribió el código."
    n 1fskwr "¡¿...Así que qué {i}saco{/i} incluso de eso, [player]?!"
    n 2fchwr "¿Que {i}sus{/i} manos {b}mataron{/b} a mis amigas?"
    n 2fchwrl "¿Que {i}sus{/i} manos {b}arruinaron{/b} mi vida en casa?"
    n 1fcuful "Si no directamente,{w=0.3} entonces a través de Monika."
    n 1fcsful "..."
    n 1fcsajl "Puede que no haya {i}hecho{/i} a las otras hacer...{w=1}{nw}"
    extend 2kcsajl " ...lo que hicieron."
    n 1kcsfuf "Pero seguro como el infierno ató la soga..."
    n 4fcsfuf "...forjó el cuchillo."
    n 1kskfuf "¡Y-{w=0.2}y tú!{w=0.5}{nw}"
    extend 1kskwrf " ¡¿Siquiera {i}sabías{/i} en lo que te metías?!"
    n 2kslupf "¡¿Lo que {i}verías{/i}?!"
    n 1kcsupf "..."
    n 1kcsajf "Yo...{w=1} no lo sé,{w=0.3} [player]."
    n 1kcsunf "..."
    n 1kcsanf "En serio.{w=1}{nw}"
    extend 2kplajf " Realmente no lo sé."
    n 2knmbol "No lo conozco,{w=1}{nw}"
    extend 2kslfrl " y probablemente nunca lo haré."
    n 1ksqbo "...Y esa es probablemente la peor parte,{w=0.3} también."
    n 4kwdwr "¡N-{w=0.2}no me malinterpretes!"
    extend 1kwdup " ¡No quiero {i}nada{/i} que ver con él!"
    extend 2fnmbo " O sea,{w=0.3} para {i}nada{/i}."
    n 1ncsbo "Pero...{w=1}{nw}"
    extend 1ncsaj " todas estas preguntas..."
    n 2kcssr "Solo puedo imaginar cuáles serían las respuestas."

return

init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_custom_outfits_unlock",
            unlocked=True,
            prompt="Trajes personalizados",
            conditional="jn_utils.get_total_gameplay_length().total_seconds() / 3600 >= 48 and not persistent.jn_custom_outfits_unlocked",
            nat_says=True,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_custom_outfits_unlock:
    $ persistent.jn_custom_outfits_unlocked = True
    n 1nslpu "..."
    n 1usceml "...!"
    n 4uskeml "He...{w=0.5}{nw}"
    extend 1nllem " recién notado algo.{w=1}{nw}"
    extend 2fslun " Algo que {i}realmente{/i} no me gusta."
    n 1fbkwr "...¡Y eso es exactamente cuánto {i}tiempo{/i} he estado atrapada usando el mismo montón de ropa!{w=0.5}{nw}"
    extend 2fcswr " ¡Q-{w=0.2}qué asco!"
    n 4flrem "Digo...{w=1}{nw}"
    extend 2fsqemsbl " ¿te sentirías {i}tú{/i} cómodo usando la misma ropa básicamente cada día?"
    n 1kslansbl "¡Cielos!"
    n 2fcsposbr "..."
    n 1fcsajsbr "Bueno,{w=0.3}{nw}"
    extend 1fnmemsbr " ¿sabes qué?{w=0.75}{nw}"
    extend 3fcsgs " ¡Terminé!"
    n 3fcspol "¡No tengo que aguantar esto!"
    n 4fsrpo "Tiene que haber algo que pueda hacer..."
    n 1ncspu "..."
    n 1uwdaj "...¡Espera!{w=1.5}{nw}"
    extend 3fllbg " ¡Duh!{w=1.5}{nw}"
    extend 3fcsbs " ¡Por supuesto!"
    n 1ulraj "¡No es como si {i}nunca{/i} hubiera tenido ropa aparte de la que tenía en mi bolso!"
    n 1nllpu "Y con el armario aquí también...{w=0.75}{nw}"
    extend 1fllpu " más la ropa extra en mi casillero..."
    n 3ncssr "Hmm..."
    n 4fchbg "¡Sí,{w=0.1} okay!{w=1.5}{nw}"
    extend 1nchsm " ¡Creo que todo eso debería funcionar!"
    n 1nsqsm "..."
    n 4uwdajesu "¡Oh!{w=0.3}{nw}"
    extend 1unmca " Solo para mantenerte al tanto,{w=0.1} [player]..."
    n 3uchsmeme "¡Debería ser capaz de vestir lo que quiera ahora!"
    n 1nllbg "Ya tengo un par de trajes en mente,{w=0.5}{nw}"
    extend 3fcsbgedz " así que no es como si tuviera alguna razón para {i}no{/i} presumir algo de estilo."
    n 1ulraj "Así que...{w=0.5}{nw}"
    extend 4fcssm " no te sorprendas si quiero cambiar mi ropa de vez en cuando,{w=0.1} ¿está bien?"
    n 1fsqsrl "Y-{w=0.1}y no.{w=0.5}{nw}"
    extend 2flleml " {i}No{/i} vas a ver {i}nada{/i}."
    n 2fslpol "Me estoy asegurando de {i}eso{/i}."
    n 1nslbo "..."
    n 1uslaj "Pero..."
    n 1unmbo "Supongo que estaría abierta a sugerencias."
    n 1ncsem "Solo...{w=0.3} nada vergonzoso.{w=0.5}{nw}"
    extend 3nsqpo " ¿Entendido?"
    n 3nsrss "¡Se aprecia!"
    n 1ulrbo "Ahora...{w=0.5}{nw}"
    extend 1tnmss " ¿dónde estábamos?"

    python:
        get_topic("talk_custom_outfits_unlock").lock()


        jn_outfits.unloadCustomOutfits()
        jn_outfits.unloadCustomWearables()


        jn_outfits.loadCustomWearables()
        jn_outfits.loadCustomOutfits()


        jn_outfits.JNWearable.loadAll()
        jn_outfits.JNOutfit.loadAll()

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_maintaining_proper_hygiene",
            unlocked=True,
            prompt="Higiene adecuada",
            category=["Salud", "Tú"],
            nat_says=True,
            affinity_range=(jn_affinity.AFFECTIONATE, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_maintaining_proper_hygiene:
    n 1nllsl "..."
    n 1ullaj "Sabes,{w=0.1} [player]..."
    n 1nllbo "Me he estado preguntando...{w=0.5}{nw}"
    extend 2tnmpu " ¿realmente te estás cuidando?"
    n 1nsqsr "Como...{w=0.3} ¿estás manteniendo una higiene adecuada?"
    n 3fnmpo "¡Es súper importante,{w=0.1} sabes!"
    extend 1nslem " ...Y no solo porque es {i}realmente{/i} asqueroso si no lo haces."
    n 4ulraj "No es solo sobre estar físicamente saludable,"
    extend 4fnmaj " ¡sino que en realidad ayuda con tu salud mental también!{w=1}{nw}"
    n 3fllpo "¡Hablo en {i}serio{/i}!"
    n 1klrss "Si ya estás pasándola mal en la vieja cabeza,{w=0.5}{nw}"
    extend 2ksrsr " sentirse asqueroso físicamente así como mentalmente no va a ayudar para nada."
    n 1knmpu "{i}Ambos{/i} conocemos a alguien que siempre se veía desaliñada,{w=0.1} [player].{w=1.5}{nw}"
    n 1kcssr "...Y ambos sabemos cómo se sentía ella."
    n 1kllun "..."
    n 3fcseml "¡C-{w=0.1}como sea!{w=1}{nw}"
    extend 3fnmpo " Esto es sobre {i}ti{/i},{w=0.1} [player] -{w=0.5}{nw}"
    extend 4fnmaj " ¡así que escucha!"
    n 1fcsbg "¡Este va a ser un especial de Natsuki sobre cuidarte a ti mismo!{w=0.5}{nw}"
    extend 1fcssm " Ehehe."
    n 1fcsaj "Primero que nada,{w=0.1} dúchate {w=0.1}-{w=0.3}{nw}"
    extend 3fnmaj " ¡y {i}regularmente{/i}!"
    n 1fllsl "Si te saltas duchas,{w=0.1} solo te sentirás constantemente toda asquerosa y desagradable.{w=0.5}{nw}"
    extend 4tnmsr " ¿Y sabes a qué lleva eso?"
    n 2nsgbo "Pérdida de motivación."
    n 1fnmaj "¿Y sabes a qué lleva {i}eso{/i}?"
    n 2fcsem "...¡No ducharse!{w=0.5}{nw}"
    extend 2knmpo " ¿Ves a dónde voy?"
    n 1nllaj "Así que...{w=0.5}{nw}"
    extend 4fnmsl " solo tómate el tiempo para hacerlo propiamente,{w=0.1} ¿okay?"
    n 3fllss "No {i}necesita{/i} ser algún tipo de ritual de spa,{w=0.1} solo lo que sea que te deje limpio."

    if Natsuki.isLove(higher=True):
        n 4fslss "Y además,{w=0.5}{nw}"
        extend 3fsrssl " No quiero acurrucarme contigo si estás todo apestoso."
        n 3fnmpo "So you better stick at it,{w=0.1} [player]!"

    if persistent.jn_player_appearance_hair_length == "None":
        n 1fcsaj "Siguiente,{w=0.1} ¡tu cabeza!"
        n 1ullpu "Sé que dijiste que no tenías cabello...{w=0.5}{nw}"
        extend 3fsqbg " ¡pero eso no significa que puedas flojear arriba!"
        n 1ulraj "Tienes que asegurarte de mantener tu piel limpia allí arriba.{w=0.5}{nw}"
        extend 3nsqunsbl " Incluso si no tienes cabello,{w=0.1} grasa y todas esas cosas se acumulan."
        n 4fcsem "¡Qué asco!"
        n 1ullaj "Pero al menos es fácil de resolver si te duchas regularmente,{w=0.5}{nw}"
        extend 3nnmbo " como acabo de decir."
    else:

        n 1fcsaj "Siguiente,{w=0.1} ¡tu cabello!"

        if not persistent.jn_player_appearance_hair_length:
            n 1tllss "Asumiendo que {i}tengas{/i} algo,{w=0.1} claro."

        n 1nsqbo "{i}No{/i} vas a sentirte bien sobre tu apariencia si tu cabello se ve constantemente como un trapeador usado."
        n 3fchbg "Así que mantenlo limpio,{w=0.1} ¡y asegúrate de cepillarlo!{w=0.5}{nw}"
        extend 1ullss " O haz lo que sea que tu peinado usual necesite {w=0.1}-{w=0.3}{nw}"
        extend 4nnmbo " peine,{w=0.1} gel,{w=0.1} lo que sea."
        n 1tnmpu "¿Recuerdas lo que dije sobre ducharse,{w=0.1} [player]?"
        n 3fcsbo "¡Mientras más lo pospongas,{w=0.1} más difícil es de hacer!{w=0.5}{nw}"
        extend 3fnmem " ¡Y si se pone muy pegajoso,{w=0.1} podrías incluso tener que afeitarlo!"
        n 1fsrbg "No quiero verte caminando por ahí como si te acabara de dar un choque eléctrico...{w=0.5}{nw}"
        extend 4fchgn " ...¡o tan calvo como un huevo!"

        if persistent.jn_player_appearance_hair_length == "Long":
            n 4fspaj "¡Y {i}especialmente{/i} ya que tienes un cabello largo tan asombroso!{w=0.5}{nw}"
            extend 2fllan " ¡Qué desperdicio!"

        n 1ulraj "Así que...{w=1}{nw}"
        extend 4fnmbo " cuida tu cabello también,{w=0.1} ¿entendido?"
        n 1fcssm "¡Es {i}igual{/i} de importante que el resto de ti!"

    if get_topic("talk_natsukis_fang").shown_count > 0:
        n 1fcsaj "Finalmente,{w=0.1} ¡cepilla tus dientes!"
        n 1ullaj "Te ahorraré el sermón esta vez,{w=0.5}{nw}"
        extend 3nnmbo " ya que ya hablamos de eso y todo."
        n 4nsqpu "...Pero más te vale no haberte olvidado del hilo dental,{w=0.1} [player]...{w=1.5}{nw}"
        extend 4fsqsm " ¡Porque seguro yo no!"
    else:

        n 1fcsaj "Finalmente,{w=0.1} ¡tus dientes!{w=0.5}{nw}"
        extend 3fsqpu " Ahora esos son algo que {i}realmente{/i} no quieres saltarte,{w=0.1} [player]."
        n 3kslan "No solo tu aliento será {i}espantoso{/i}..."
        n 4fbkwr "¡Sino que perderás tus dientes también!{w=0.5}{nw}"
        extend 2flrun " O al menos terminarás con un montón de empastes...{w=1}{nw}"
        extend 1ksqem " ¡Empastes caros!{w=1}{nw}"
        extend 2fsran " ¡Cielos!"
        n 4fsqpo "Realmente tendrías que ser un tonto para preferir tratamientos caros y un mundo de dolor sobre un par de minutos de esfuerzo."
        n 1flrss "Y además..."
        n 3ksqsm "¿Quién no quiere una sonrisa {i}deslumbrante{/i} como yo?"
        n 3uchgn "¡No conseguirás {i}eso{/i} con caries!"

    n 4kllss "Pero en serio,{w=0.1} [player].{w=0.5}{nw}"
    extend 4nsqsr " {i}Realmente{/i} no quiero que te eches para atrás en cuidarte a ti mismo."
    n 2fsqsr "Lo digo en serio.{w=1.5}{nw}"
    extend 2ksrpo " Mereces sentirte y verte bien también."

    menu:
        n "¿Entendido?"
        "Sí, merezco sentirme y verme bien también":

            n 1fchbg "¡Ahora {i}eso{/i} es lo que me gusta escuchar!"
            $ Natsuki.calculatedAffinityGain()
        "...":

            n 1nsqsr "..."
            n 3tsqss "Tú...{w=0.3} realmente no entiendes cómo funciona todo esto,{w=0.1} ¿verdad?"
            n 1fcssm "Ahora,{w=0.1} repite después de mí:{w=0.5}{nw}"
            extend 1fcsbg " 'Merezco sentirme y verme bien también.'."

            menu:
                "Merezco sentirme y verme bien también":
                    n 3uchbg "¿Ves?{w=0.5}{nw}"
                    extend 3ksqsg " ¿Fue {i}tan{/i} difícil?"
                    n 1fcssm "Ehehe."
                    $ Natsuki.calculatedAffinityGain()

    n 1ullss "Pero como sea,{w=0.1} ¡sí!{w=0.5}{nw}"
    extend 1nnmss " Eso es todo lo que tenía que decir."

    if Natsuki.isLove(higher=True):
        n 4nsqss "Y recuerda...{w=0.5}{nw}"
        extend 3nsldvl " ¡Te amaré por siempre si mantienes el ritmo!~"
        n 1fchsml "Ehehe."
        $ chosen_endearment = jn_utils.getRandomEndearment()
        extend 4uchbgl " ¡Gracias,{w=0.1} [chosen_endearment]!"

    elif Natsuki.isEnamored(higher=True):
        n 3nslbgl "{i}Realmente{/i} me gusta la gente que se cuida."
        n 4fsqpol "Harías bien en recordar eso, [player]."
    else:

        n 1fchbg "¡Gracias por escucharme,{w=0.1} [player]!"
        n 1uslsg "...O debería decir..."
        n 3usqbg "Gracias por dejarme{w=0.5}{nw}"
        extend 3fsqss " {i}aclarar{/i}{w=0.5}{nw}"
        extend 3usqsm " eso?"
        n 1nchgnelg "¡Ahaha!"

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_feelings_about_monika",
            unlocked=True,
            prompt="¿Cómo te sientes sobre Monika?",
            category=["DDLC"],
            player_says=True,
            affinity_range=(jn_affinity.AFFECTIONATE, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_feelings_about_monika:
    n 1fslsr "Monika."
    n 1kcsem "..."
    n 2knmsl "...¿Honestamente?"
    n 1nllsl "Yo...{w=1} no sé {i}cómo{/i} me siento sobre Monika.{w=1}{nw}"
    extend 2kslpu " Ya no."
    n 1nnmsl "Digo,{w=0.5}{nw}"
    extend 4knmpu " ¿qué digo siquiera,{w=0.1} [player]?"
    n 3flrpu "Sí,{w=0.1} ella se metía en mis asuntos a veces.{w=1}{nw}"
    extend 3fsrsf " No me gustaba cuando se ponía toda superior y poderosa...{w=1}{nw}"
    extend 3fslem " {i}o{/i} cuando seguía metiéndose con mis cosas."
    n 1nllpu "Pero como...{w=0.5}{nw}"
    extend 4knmpu " nunca estuve realmente {i}enojada{/i} ni nada..."
    n 1fcsfr "Molesta,{w=0.3} frustrada,{w=0.3} seguro.{w=1}{nw}"
    extend 2fllpu " ¡Cualquiera lo estaría!"
    n 2kplem "¡Pero la admiraba,{w=0.1} [player]!{w=1.5}{nw}"
    extend 4kllun " {i}Todas{/i} lo hacíamos..."
    n 1kcsun "..."
    n 1fcsun "Ella no era {i}solo{/i} la presidenta del club,{w=0.1} o lista."
    n 3fnmun "Ella era un modelo a seguir.{w=1.5}{nw}"
    extend 3klrpu " ...Y mi amiga."
    n 1ksrpu "Pero...{w=0.5}{nw}"
    extend 4knmem " eso solo hace más difícil para mí entender,{w=0.1} [player]."
    n 1fcssl "Digo...{w=0.5}{nw}"
    extend 2fcsan " Yo...{w=1} sé...{w=1} con lo que ella estaba lidiando.{w=1.5}{nw}"
    extend 1kslun " ¡{i}Yo{/i} estoy lidiando con eso ahora mismo!"
    n 4kwdem "Pero...{w=0.3} ¿en serio tenía que {i}torturarnos{/i}?"
    n 2fcsem "Yo...{w=0.3} sé...{w=0.3} que no hubiéramos entendido.{w=0.5}{nw}"
    extend 2kslsr " {i}No podríamos{/i} haber entendido."
    n 1fcsan "Especialmente cuando Yuri y yo estábamos envueltas en esas peleas estúpidas..."
    n 4fnmsr "{i}Entiendo eso{/i}."
    n 2klrpu "Pero si ella estaba tan desesperada...{w=0.5}{nw}"
    extend 1kcspu " ¿no podría simplemente habernos eliminado a todas desde el principio?{w=0.5}{nw}"
    extend 4knmem " ¿O literalmente {i}cualquier{/i} otra cosa?"
    n 1fcsfr "..."
    n 2kcspu "No lo sé,{w=0.1} [player].{w=1.5}{nw}"
    extend 4knmca " Realmente no lo sé."
    n 1ncssr "..."
    n 1nllpu "Supongo..{w=1}{nw}"
    extend 2tnmpu " ¿tal vez fue el aislamiento?"
    n 1nlrsl "Ella siempre estaba siendo excluida de todo desde que apareciste...{w=1}{nw}"
    extend 2nsrsr " No creo que siquiera {i}tuviera{/i} opción."
    n 4knmsl "...¿Tal vez me hubiera pasado lo mismo a mí?"
    n 1fcseml "¡P-{w=0.1}pero no me malinterpretes!{w=0.5}{nw}"
    extend 3flrem " Nunca voy a olvidar lo que hizo...{w=0.5}{nw}"
    extend 3fsrputsb " perdonar lo que hizo."
    n 1nlrpu "Pero...{w=1}{nw}"
    extend 4knmsr " ella {i}era{/i} mi amiga aún así."
    n 1kllpu "Así que siempre habrá una parte de mí que como que desea que {i}pudiera{/i} perdonarla."
    n 2kllbol "...Tal vez es por eso que quiero entender sus acciones tanto."

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_feelings_about_yuri",
            unlocked=True,
            prompt="¿Qué opinas de Yuri?",
            category=["DDLC"],
            player_says=True,
            affinity_range=(jn_affinity.AFFECTIONATE, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_feelings_about_yuri:
    n 1kllpul "... Oh, {w=1}Yuri...."
    n 2kcsuntsb "..."
    n 1ncspu "... No te mentiré,{w=0.3} [player].{w=1.5}{nw}"
    extend 4ksqfr " Yo realmente, {w=0.5}{i}realmente{/i} no quería pensar en... {w=1}{i}eso{/i} otra vez.."
    n 1kcssl "..."
    n 1ksrpu "¿Cómo puedo {i}explicar{/i} esto...?"
    n 3ncsem "Yuri y yo éramos... {w=0.3}complicadas. {w=1}{nw}"
    extend 3kllss "Incluso {i}antes{/i} de que te unieras al club."
    n 1nnmbo "Nunca coincidimos completamente,{w=0.1} [player].{w=1.5}{nw}"
    extend 2nslca " Probablemente ya adivinaste eso de todas formas."
    n 1kwmpu "Pero teníamos un {i}entendimiento{/i},{w=0.1} ¿sabes?"
    n 1kllpul "Ella estaba...{w=1}{nw}"
    extend 1kcsunltsa " ahí...{w=1}{nw}"
    extend 2fcsunltsa " para mí."
    n 2fsrunltsb "Cuando necesitaba a alguien más que nunca.{w=1}{nw}"
    extend 1fnmem " Cuando nadie más lo entendería...{w=1}{nw}"
    extend 4kslpu " Podría siquiera {i}esperar{/i} entenderlo."
    n 1kwmpu "...{w=0.5}¿Siquiera sabes cuánto significó eso para mí?"
    n 1knmsl "Ella simplemente tenía una forma de entenderte como nadie más podía.{w=1}{nw}"
    extend 2fslem " No {i}Monika{/i}.{w=1.5}{nw}"
    extend 1kslsrl " Ni siquiera {i}Sayori{/i}."
    n 1kllpu "Pero..."
    n 3fcssr "Ella simplemente {i}cambió{/i},{w=0.1} [player].{w=0.5}{nw}"
    extend 3klrsl " Cuando apareciste,{w=0.1} digo."
    n 4knmem "{i}Nunca{/i} tuvimos peleas como esa..."
    n 1tnmsr "¿Discusiones?{w=0.5}{nw}"
    extend 2tllss " Bueno...{w=1} ¡sí!{w=1}{nw}"
    extend 2knmss " ¿Qué clase de amigas no las tienen?"
    n 1klrsm "Y siempre fuimos súper diferentes,{w=0.1} también."
    n 3nsrpo "Ella siempre tenía esa vibra recatada y correcta.{w=1}{nw}"
    extend 1ncsaj " Refinada...{w=1}{nw}"
    extend 1ncsss " elegante."
    n 2nslss "...{w=0.5}Y yo solo era Natsuki.{w=1}{nw}"
    extend 1ncsss " Heh."
    n 1knmpu "¡Pero nunca tuve la sensación antes de eso de que simplemente {i}no le agradaba{/i}!"
    n 2fcsan "Ambas estábamos tan atrapadas en esa {i}estúpida{/i} rivalidad..."
    n 1fllan "¡Simplemente se apoderó de todo!"
    n 2kllpu "Y luego cuando ella comenzó a ponerse toda posesiva...{w=1}{nw}"
    extend 4knmsl " sabes,{w=0.1} después de que Monika la arruinó toda."
    n 4kplem "...¿Sabes lo {i}aterrador{/i} que fue eso para mí?{w=1.5}{nw}"
    extend 1kwdwr " ¿Escuchar esas {i}palabras{/i} saliendo de {i}su{/i} boca?"
    n 1klrem "¿Y la peor parte?{w=1.5}{nw}"
    extend 2kcsem " Yo solo...{w=0.3} le...{w=0.3} seguí la corriente.{w=1}{nw}"
    extend 2kplup " ¡No tenía {i}opción{/i},{w=0.1} [player]!"
    n 1fcsup "...Ninguna de nosotras la tenía."
    n 1fcsanl "Incluso cuando te {i}rogué{/i} por ayuda,{w=0.1} yo..."
    n 2kcsanltsa "Yo-..."
    n 1kcsupltsd "..."
    n 1fcsunltsa "..."
    n 4kcseml "...Lo siento,{w=0.1} [player]."
    n 2ksrunl "Realmente no creo que sea bueno para mí seguir hablando de esto.{w=1}{nw}"
    extend 1ksqpul " ...De ella."
    n 1fcssrl "Solo...{w=1}{nw}"
    n 1kcseml "..."
    n 2fwmsrl "...Extraño a mi amiga.{w=1}{nw}"
    extend 4kllsr " Extraño cómo solía ser."
    n 1kllaj "Así que...{w=0.5} ¿recordando lo que pasó?{w=0.5}{nw}"
    extend 2kskem " ¿En lo que se {i}convirtió{/i}?"
    n 1fcsem "Solo...{w=1} duele,{w=0.1} [player].{w=1.5}{nw}"
    extend 2fcsunltsa " Duele mucho."
    n 4fsqun "...¿Y para ser honesta?"
    n 1ksrpu "...No estoy segura de que alguna vez {i}deje{/i} de hacerlo."

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_feelings_about_sayori",
            unlocked=True,
            prompt="¿Cómo te sientes sobre Sayori?",
            category=["DDLC"],
            player_says=True,
            affinity_range=(jn_affinity.AFFECTIONATE, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_feelings_about_sayori:
    n 1nsrss "Heh.{w=1}{nw}"
    extend 2ksrss " Sayori..."
    n 1kcspu "..."
    n 4fcsunl "Yo...{w=0.5}{nw}"
    extend 1fcsem " todavía me enojo conmigo misma a veces,{w=0.1} sabes."
    n 2klrpu "Simplemente no puedo {i}creer{/i} cómo descarté cómo se sentía tan fácilmente."
    n 1kplun "...Y cómo olvidé siquiera que {i}existía{/i}."
    n 2fcsanl "Si tan solo hubiera {i}sabido{/i} qué tan mal estaba su salud mental...{w=1}{nw}"
    extend 4fcsupl " cuánto estaba {i}doliendo{/i}..."
    n 1fcsunl "..."
    n 1kcsem "..."
    n 2kslpu "Es...{w=1.5}{nw}"
    extend 2kplem " todavía es tal shock,{w=0.1} ¿sabes?"
    n 1fcsem "Ella siempre estaba tan...{w=1} tan...{w=0.5}{nw}"
    extend 2ksrpo " simplemente...{w=1} ¡súper emocionada y pegajosa!"
    n 1ksrss "¡Como si estuviera {i}vibrando{/i} de felicidad!"
    n 1ksrun "..."
    n 4kplpul "...¿Así que puedes siquiera {i}imaginar{/i} cómo se siente?"
    n 2fcsun "Sabiendo que ella solo estaba usando una máscara,{w=1}{nw}"
    extend 1fcsfu " ¿luego bailando como una marioneta bajo la mano de Monika?"
    n 2ksrbol "...Mientras su propia mente le estaba dando una {i}paliza{/i} absoluta."
    n 1kcspuesi "..."
    n 1ncsss "Heh.{w=1}{nw}"
    extend 3nsqss " ¿Sabes qué?"
    n 1ncspu "No me importa mi galleta de la que tomó un mordisco gigante."
    n 1nlrpu "No me importan las canciones tontas que cantaría,{w=1}{nw}"
    extend 3nslssl " o sus...{w=0.3} incómodos...{w=0.3} cumplidos."
    n 4tnmsr "¿En este punto?"
    n 2ksrsrltsb "Creo que haría {i}cualquier cosa{/i} solo para ver una sonrisa genuina de Sayori de nuevo..."
    n 2kcsssftsa "...Y darle uno de esos grandes,{w=0.1} tontos abrazos que le gustaban tanto."

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_thoughts_on_tea",
            unlocked=True,
            prompt="¿Bebes mucho té?",
            conditional="jn_utils.get_total_gameplay_length().total_seconds() / 3600 >= 36",
            category=["Comida"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_thoughts_on_tea:
    $ already_discussed_thoughts_on_tea = get_topic("talk_thoughts_on_tea").shown_count > 0
    $ player_tea_coffee_preference_known = persistent.jn_player_tea_coffee_preference is not None

    if Natsuki.isNormal(higher=True):
        if already_discussed_thoughts_on_tea:
            n 1fcsaj "D-{w=0.1}de hecho,{w=0.2} espera un segundo...{w=1}{nw}"
            extend 2tslpu " ¿no hablamos ya de esto?"
        else:

            n 1tnmaj "¿Huh?{w=0.2} ¿Bebo té?"
            n 3fchgn "...¿Estás {i}seguro{/i} de que sabes con quién estás hablando?{w=0.5}{nw}"
            extend 1fllbg " ¡Literalmente nunca lo hago yo misma!"
            n 2uslss "Digo,{w=0.5}{nw}"
            extend 1unmbo " lo tomé unas cuantas veces en el club,{w=0.2} seguro."
            n 1nlrpu "Yuri lo preparaba para todos nosotros a veces."
            n 2tsrss "¡Pero nunca fue como si lo pidiera ni nada!"

    elif Natsuki.isDistressed(higher=True):
        n 1fcsem "..."
        n 2fsqsr "No,{w=0.5} [player]."
        n 1fsqbo "No me importa mucho."
        n 2fllpu "...Digo,{w=0.5}{nw}"
        extend 2nllsf " {i}Supongo{/i} que lo bebería si me lo ofrecieran."
        n 2nslsl "...De la mayoría de la gente,{w=0.2} al menos."
        n 1fsqbo "De alguna manera dudo que ese fuera el caso para {i}ti{/i}."

        return
    else:

        n 1fcsem "No,{w=2}{nw}"
        extend 2fsqan " y ciertamente no beberé nada del {i}tuyo{/i}."
        n 2fslemltsb "No como si fuera {i}solo{/i} té de todas formas,{w=0.2} conociendo a un idiota como {i}tú{/i}."

        return

    if already_discussed_thoughts_on_tea:
        n 1ullaj "Bueno,{w=0.2} como sea.{w=0.5}{nw}"
        extend 4unmbo " No diría que mi opinión ha cambiado mucho."
        n 2nlraj "Entiendo por qué a la gente le gusta,{w=0.2} supongo."
    else:

        n 1fllbo "..."
        n 3fcseml "¡E-{w=0.2}eso no quiere decir que crea que apesta,{w=0.2} o algo así!"

        if get_topic("talk_favourite_drink").shown_count > 0:
            n 1nlrbo "Solo tengo mis propios gustos.{w=0.75}{nw}"
            extend 4uspbg " ¡Como el chocolate caliente!"
        else:

            n 1nlrbo "Solo tengo mis propios gustos."

        n 1ullaj "Pero...{w=0.5}{nw}"
        extend 2nllbo " Supongo que puedo ver por qué a la gente le gusta tanto."

    n 2tnmca "El té contiene cafeína,{w=0.2} ¿verdad?{w=0.5}{nw}"
    extend 2tlrss " No tanta como el café ni nada,{w=0.2} pero un estímulo sigue siendo un estímulo,{w=0.2} supongo."
    n 1unmaj "¡Viene en un montón de sabores también!{w=0.5}{nw}"
    extend 4unmgs " ¡De hecho estaba algo sorprendida de la variedad!"
    n 1ullss "Tienes tu viejo té negro regular{w=0.3}{nw}"
    extend 2fslss " -{w=0.1} obviamente -{w=0.3}{nw}"
    extend 1ulraj " pero tienes té verde,{w=0.2} té de hierbas..."
    n 4uspgs "¡Incluso unos saborizados como canela y menta!"
    n 2nslss "Solo tuvimos té oolong en el salón del club sin embargo,{w=0.5}{nw}"
    extend 2tnmss " así que ¿quién sabe?"
    n 1ulrbo "Tal vez me gustaría si probara alguno que sonara bien."

    if get_topic("talk_sleeping_well").shown_count > 0:
        n 1unmaj "¡Aparentemente algo de té incluso te ayuda a dormir!{w=0.75}{nw}"
        extend 2nsrss " ...Tal vez debí haber mencionado eso en mis consejos para dormir.{w=0.5}{nw}"
        extend 2fchblesd " ¡Oops~!"

    n 1ulraj "Pero...{w=0.5}{nw}"
    extend 4nslss " He hablado suficiente."
    n 1unmbo "¿Qué hay de ti,{w=0.2} [player]?"
    show natsuki 4tsqss
    $ menu_opening = "¿Ahora estás bebiendo otra cosa?" if player_tea_coffee_preference_known else "¿Cuál es tu elección?"

    menu:
        n "[menu_opening]"
        "Prefiero el té":

            if player_tea_coffee_preference_known:
                if persistent.jn_player_tea_coffee_preference == "tea":
                    n 1nnmss "Bueno,{w=0.5}{nw}"
                    extend 1tnmss " algunas cosas nunca cambian,{w=0.2} ¿eh?"
                    n 1fchsm "Ehehe."
                else:

                    n 2tnmsm "¿Un bebedor de té ahora,{w=0.2} eh?{w=0.5}{nw}"
                    extend 1fchsm " ¡Me parece bien!"
            else:

                n 4unmaj "¿Té?{w=0.5}{nw}"
                extend 1nllpu " Hmm..."
                n 1unmbo "Sí,{w=0.2} eso es casi lo que esperaba."
                n 2nlrbo "..."
                n 1tnmbg "¿Qué?"
                n 3tsqbg "No es como si hubieras hecho un escándalo al respecto antes,{w=0.5}{nw}"
                extend 3tsqsm " ¿verdad?"
                n 1kslsm "..."
                n 1nslss "Aunque...{w=1.5}{nw}"
                extend 4uslsr " no es como si tuvieras mucha opción en ello en ese entonces,{w=0.2} ¿verdad?"

            $ persistent.jn_player_tea_coffee_preference = "tea"
        "Prefiero el café":

            if player_tea_coffee_preference_known:
                if persistent.jn_player_tea_coffee_preference == "coffee":
                    n 1nnmss "Bueno,{w=0.5}{nw}"
                    extend 2tnmss " algunas cosas nunca cambian,{w=0.2} ¿eh?"
                    n 1fchsm "Ehehe."
                else:

                    n 3tsqct "¿Oho?{w=0.5}{nw}"
                    extend 3tsqbg " ¿Café ahora,{w=0.2} eh?"
                    n 1fsrsm "Wow,{w=0.2} [player]."
                    n 3fchgnelg "¿Desde cuándo te has vuelto tan {i}amargado{/i}?"
            else:

                n 1unmaj "¿Oh?{w=1.5}{nw}"
                extend 3tnmss " ¿Eres un bebedor de café?"
                n 1nllpu "Hmm..."
                n 1nsqss "Entonces supongo que las sesiones en el club no eran tu{w=0.5}{nw}"
                extend 3fsqbg " {i}taza de té{/i}{w=0.5}{nw},"
                extend 3usqbg " ¿eh?"
                n 1uchgn "..."
                n 1fchbg "Oh,{w=0.5}{nw}"
                extend 4fllbg " ¡vamos,{w=0.2} [player]!{w=0.3} Cielos."
                n 1fsqsm "No hay necesidad de estar todo {w=0.3}{i}amargado{/i}{w=0.3} al respecto."
                n 1fchsm "..."
                n 3kchbg "¡Okay,{w=0.2} okay!{w=0.5} ¡Terminé!"
                n 3fsqsg "...Por ahora."

            $ persistent.jn_player_tea_coffee_preference = "coffee"
        "¡Me gustan ambos!":

            if player_tea_coffee_preference_known:
                if persistent.jn_player_tea_coffee_preference == "both":
                    n 1nnmss "Bueno,{w=0.5}{nw}"
                    extend 3tnmss " algunas cosas nunca cambian,{w=0.2} ¿eh?"
                    n 1fchsm "Ehehe."
                else:

                    n 4tnmaj "¿Oh?{w=0.5}{nw}"
                    extend 3tnmss " ¿Te gustan {i}ambos{/i} ahora?"
                    n 4tsqbg "...¿Estás {i}seguro{/i} de que no eres solo un adicto a la cafeína,{w=0.2} [player]?"
                    extend 1nchgn " Ehehe."
            else:

                n 2tslajeqm "...Huh.{w=0.75}{nw}"
                extend 1tnmss " ¿En serio?"
                n 3nsrss "Eso es...{w=0.3} un poco raro,{w=0.2} en realidad."
                n 1fchbg "¡A la mayoría de la gente le gusta al menos {i}uno{/i} de los dos más!"
                n 4fsqsg "¿Estás {i}seguro{/i} de que no eres solo un adicto a la cafeína,{w=0.2} [player]?"

            $ persistent.jn_player_tea_coffee_preference = "both"
        "No me gusta el té ni el café":

            if player_tea_coffee_preference_known:
                if persistent.jn_player_tea_coffee_preference == "neither":
                    n 1tsqpu "Todavía no eres fan,{w=0.2} ¿eh?{w=0.5}{nw}"
                    extend 4fnmaj " ¡Necesitas seguir probando cosas nuevas!"
                    n 3fsqpo "¿Dónde está tu sentido de la aventura,{w=0.2} [player]?{w=0.5}{nw}"
                    extend 1fchts " Ehehe."
                else:

                    n 4tnmaj "¿Huh?{w=0.3} ¿No te gusta el té {i}ni{/i} el café ahora?{w=0.5}{nw}"
                    extend 1tsqun " ¿Me perdí de algo?"
                    n 2tlrbo "...¿O tal vez solo estás tratando de dormir mejor?{w=0.5}{nw}"
                    extend 1tsrpu " Huh."
            else:

                n 1ullaj "Eso es...{w=0.75}{nw}"
                extend 2tllbo " algo sorprendente,{w=0.2} en realidad."
                n 4fsrpu "A la mayoría de la gente al {i}menos{/i} le gusta uno o el otro..."
                n 3fsqpo "No me estás tomando el pelo,{w=0.3}{nw}"
                extend 3ksqpo " ¿verdad?"
                n 4fslpol "Estaba hablando en serio..."

            $ persistent.jn_player_tea_coffee_preference = "neither"

    n 1nllss "Bueno,{w=0.2} como sea.{w=0.5}{nw}"
    extend 1fchbg " No es como si las bebidas calientes fueran lo máximo de todas formas."
    n 3fllss "Pero dicho eso...{w=0.3}{nw}"
    extend 3nsremsbl " De hecho estoy bastante sedienta después de todo eso de hablar."
    n 4fsrpo "..."
    n 1unmss "Hey,{w=0.2} [player]...{w=1}{nw}"
    extend 1usqsm " ¿me haces un favor?"
    n 1fsqsg "..."
    n 3fchbg "...Pon la tetera,{w=0.2} ¿quieres?"
    n 3uchgnelg "Ahaha."

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_how_to_make_friends",
            unlocked=True,
            prompt="¿Cómo hago amigos?",
            category=["Vida", "Sociedad", "Tú"],
            player_says=True,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_how_to_make_friends:
    n 1tnmpu "¿Huh?{w=1}{nw}"
    extend 4tnmsleqm " ¿Quieres saber cómo hacer {i}amigos{/i}?"
    n 1tllbo "..."
    n 3ncsaj "Bueno.{w=1}{nw}"
    extend 3nlraj " Tengo que decir,{w=0.1} [player]."
    n 4fchgnelg "¡Esa está bastante alta en las preguntas más raras que me has hecho hasta ahora!"
    n 1fllss "Pero...{w=1}{nw}"
    extend 2ullaj " ¿con toda seriedad?"
    n 1tnmsf "{w=0.3}...¿Por qué?{w=1}{nw}"
    extend 1nlrss " Como por qué me preguntas a {i}mí{/i},{w=0.3} quiero decir."

    if Natsuki.isLove(higher=True):
        n 3kslbgl "¡Básicamente dominaste el conocerme!{w=0.5}{nw}"
        extend 3fcspol " N-{w=0.1}no es que simplemente te dejé,{w=0.1} obviamente."

    elif Natsuki.isEnamored(higher=True):
        n 1ullaj "Es solo que...{w=1}{nw}"
        extend 3tnmssl " {i}seriamente{/i} dudo que sea algo con lo que {i}tú{/i} tengas problemas,{w=0.5}{nw}"
        extend 3nsrssl " de todas las personas."

    elif Natsuki.isAffectionate(higher=True):
        n 2ksqpol "¿No somos {i}ya{/i} amigos,{w=0.1} [player]?"
    else:

        n 2nsrpo "Pensé que nos estábamos llevando bien,{w=0.1} al menos..."

    n 4nsrpo "..."
    n 1ulraj "Bueno,{w=0.5}{nw}"
    extend 1nlrss " como sea..."
    n 1nchbs "¡Seguro!{w=1}{nw}"
    extend 3fwlbgedz " ¡Te puedo enseñar los trucos!"
    n 4fnmaj "¡Bien!{w=0.5}{nw}"
    extend 4ncsaj " Entonces..."
    n 1unmbo "Creo que la cosa más importante es tener {i}algo{/i} en común.{w=1}{nw}"
    extend 1flrss " Probablemente sabías eso,{w=0.1} al menos."
    n 4fnmpu "¡Pero creo que la gente piensa demasiado lo que eso realmente {i}significa{/i}!"
    n 4flrpu "No tienes que compartir pasatiempos,{w=0.5}{nw}"
    extend 2nlraj " o una tonelada de intereses o algo así."
    n 1ulrbo "Digo,{w=0.5}{nw}"
    extend 3fcsbg " ¡solo míranos a Yuri y a mí!{w=1}{nw}"
    extend 3uchgn " ¡Ejemplo clásico!"
    n 1ullaj "Seguro,{w=0.1} desacordábamos en literatura.{w=1}{nw}"
    extend 4fnmaj " Pero íbamos a la misma escuela {w=0.1}-{w=0.5}{nw}"
    extend 1fchbg " ¡y éramos miembros del mismo club!"
    n 3fcssm "¡Supongo que a lo que quiero llegar es que tener {i}lugares{/i} en común es igual de clave que los gustos!"
    n 1tllbo "Si acaso,{w=0.5}{nw}"
    extend 1tnmss " ¡de hecho lo hace incluso más fácil si {i}sabes{/i} que vas a verlos de nuevo!"
    n 3fcsaj "Así que {w=0.1}-{w=0.1} una vez que tienes algo en común,{w=0.5}{nw}"
    extend 1fchbg " ¡todo es solo cuestión de contacto!"
    n 4fsqsm "Aquí es donde tienes que usar tu cerebro,{w=0.1} [player]."
    n 1ullaj "Solo...{w=1.5}{nw}"
    extend 4tnmca " {i}piensa{/i} un poco sobre la situación y qué decir,{w=0.1} ¿sabes?"
    n 1ullpu "Como,{w=0.5}{nw}"
    extend 2nnmaj " digamos que acabas de empezar un nuevo trabajo en una oficina."
    n 2flrem "No solo asumas que les gusta el manga o lo que sea {w=0.1}-{w=0.5}{nw}"
    extend 1kchbg " ¡hazlo con calma!{w=1}{nw}"
    extend 4fchbg " ¡Acércate a ellos con un café o algo!"
    n 3fsqaj "Pero no te dejes engañar,{w=0.1} [player]."
    n 3nslsl "No puedes solo esperar hablar con alguien una vez y ya estar listo...{w=0.5}{nw}"
    extend 3fnmss " ¡tienes que mantenerlo,{w=0.1} también!"
    n 1ullbo "Charlas físicas,{w=0.1} mensajes en línea,{w=0.5}{nw}"
    extend 1unmaj " lo que sea que funcione."
    n 4uwdem "Es {i}súper{/i} fácil para una amistad -{w=0.5}{nw}"
    extend 1fllun " incluso una vieja {w=0.1}-{w=0.5}{nw}"
    extend 2knmsl " desvanecerse porque nadie está haciendo un esfuerzo."
    n 4uskem "P-{w=0.1}¡pero eso no quiere decir que tengas que ir con todo todo el tiempo!"
    n 1fcsaj "Se trata de encontrar un equilibrio.{w=1}{nw}"
    extend 2fchbgsbl " ¡La gente necesita tiempo a solas también!"
    n 4fslsr "{w=0.3}...Y no deberías ser el que pone {i}todo{/i} para que funcione."
    n 4fnmpu "Recuerda {w=0.1}-{w=0.1} una amistad tiene dos lados."
    extend 1fchsm " ¡{i}Sabes{/i} que tienes un ganador si ellos están haciendo su parte también!"
    n 2nllss "Pero dicho todo eso,{w=0.1} [player]..."
    n 1nnmsl "Hay una cosa más importante que {cps=10}{i}cualquier{/i}{/cps} otra cosa.{w=1.5}{nw}"
    extend 4fsqsr " Respeto."
    n 2fsrem "Los amigos no se basurean entre sí,{w=0.5}{nw}"
    extend 1fcsem " ¡ni les dan mierda por sus intereses!"
    n 4fsqsr "...Y eso va hacia {i}ambos{/i} lados,{w=0.1} [player]."
    n 2fsrbo "Que alguien sea un 'amigo' {i}no{/i} es excusa para que actúen como idiotas cuando quieran {w=0.1}-{w=0.5}{nw}"
    extend 2fsqpu " créeme."
    n 1fnmpu "He {i}estado{/i} ahí.{w=0.5}{nw}"
    extend 4kllsf " Y tomó un buen amigo para ayudarme a darme cuenta de eso."
    n 1ncsss "Heh."
    n 1ullpu "Pero...{w=1}{nw}"
    extend 3fchbg " ¡sí!"
    n 1tnmsm "No me pondría toda estresada al respecto,{w=0.1} [player].{w=1}{nw}"
    extend 3fcssm " Las amistades se {i}forman{/i},{w=0.1} no se fuerzan."
    n 1fcsss "Así que tómate tu tiempo,{w=0.1} y solo déjate llevar.{w=1}{nw}"
    extend 4kllbg " ¡Es todo lo que digo!"
    n 2fsqsm "Y además..."
    n 2tsqsg "Ha funcionado para nosotros hasta ahora,{w=0.1} ¿eh?{w=0.5}{nw}"
    extend 1nchgnl " Ehehe."

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_impressions_of_the_other_girls",
            unlocked=True,
            prompt="¿Puedes hacer alguna imitación de las otras chicas?",
            conditional="jn_utils.get_total_gameplay_length().total_seconds() / 3600 >= 48",
            category=["DDLC"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_impressions_of_the_other_girls:
    $ already_discussed_realizations_of_others = get_topic("talk_realizations_other_girls").shown_count > 0
    $ already_discussed_impressions_of_others = get_topic("talk_impressions_of_the_other_girls").shown_count > 0

    if Natsuki.isAffectionate(higher=True):
        if already_discussed_impressions_of_others:
            n 1fcsem "Oh,{w=0.75}{nw}"
            extend 2kslemesisbl " vaaamos..."
            n 2knmemsbl "¿Esto otra vez?{w=0.75}{nw}"
            extend 4ksqemsbr " ¿En serio?"
        else:

            n 2fcsemesi "...{w=1}{nw}"

        n 1fcssrsbr "...No,{w=0.1} [player].{w=1}{nw}"
        extend 1kcssr " No puedo."
        n 2fllun "..."
        n 2fcsemsbl "...Okay,{w=1}{nw}"
        extend 1fnmsll " mira."
        n 1fcspul "..."
        n 1fllsl "No es que {i}no pudiera{/i} hacer imitaciones de ellas.{w=1}{nw}"
        extend 2kllsr " Las conocía lo suficientemente bien."
        n 4knmpu "...Pero es exactamente por eso que no {i}quiero{/i} hacerlo,{w=0.1} [player]."
        n 2klrsf "Sabiendo cómo se sentían,{w=0.5} qué pensaban..."

        if already_discussed_realizations_of_others:
            n 4ksrputsb "...Cuánto las {i}extraño{/i}..."
        else:

            n 2ksrputsb "...Cuánto les {i}dolía{/i}..."

        n 2knmemtsc "¿Qué clase de idiota enferma sería para hacer bromas de {i}eso{/i}?"
        n 1fcsunltsa "..."
        n 1kcssl "Así que...{w=1}{nw}"
        extend 1nnmsf " Lo siento,{w=0.1} [player].{w=1.5}{nw}"
        extend 2fslsf " Pero es un no."
        n 1fcsunl "...Y siempre lo {i}será{/i}."

    elif Natsuki.isNormal(higher=True):
        if already_discussed_impressions_of_others:
            n 2knmaw "[player]...{w=0.5}{nw}"
            extend 1knmwr " ¿en serio?"
            n 4kslemlsbr "¿Esto {w=0.2}{i}otra vez{/i}?"
        else:

            n 1knmpu "..."

        n 2knmemtsc "...¿Por qué demonios querría hacer {i}eso{/i}?"
        n 1kllpu "Y-{w=0.3}y más importante,{w=1}{nw}"
        extend 2fcsem " ¿por qué siquiera pensarías en {i}preguntarme{/i} eso,{w=0.1} [player]?"
        n 2ksqem "¿Tienes alguna {i}idea{/i} de cuánto pienso en ellas,{w=0.1} todavía?"

        if already_discussed_realizations_of_others:
            n 4fcseml "¡Incluso te {i}dije{/i} cuánto las extraño,{w=0.1} [player]!"

        n 1kcsunltsa "..."
        n 1ncspu "...Muy bien,{w=0.5}{nw}"
        extend 2fcsun " mira."
        n 1fcsem "Yo...{w=1}{nw}"
        extend 1fcssr " entiendo...{w=1}{nw}"
        extend 2fsgem " que solo estabas tratando de divertirte."

        if already_discussed_impressions_of_others:
            n 2fsrun "...{i}Espero{/i},{w=0.2} al menos."

        n 1fsqsr "Pero {i}no{/i} voy a hacer bromas sobre mis amigas."
        n 2fcssr "Lo siento,{w=0.1} [player]."
        n 2fslunl "Pero algunas cosas simplemente están fuera de los límites."

        if already_discussed_impressions_of_others:
            n 1fsqunl "Y {i}más te vale{/i} respetar eso más pronto que tarde."

    elif Natsuki.isDistressed(higher=True):
        n 1fskeml "...¡¿D-{w=0.3}disculpa?!"
        n 2fsqanltsb "¿{i}En serio{/i} me estás pidiendo que me burle de mis {i}amigas{/i}?"
        n 1fsqwrltsbean "¡¿Sabiendo {w=0.2}{i}muy {w=0.2}bien{/i}{w=0.2} qué les pasó?!"

        if already_discussed_realizations_of_others:
            extend 2fcsfultsa " ¡¿Sabiendo cuánto las {i}extraño{/i}?!"

        n 1fcsunl "..."
        n 1fsqem "Tu sentido del humor {i}{w=0.2}apesta{w=0.2}{/i},{w=0.2} [player]."

        if already_discussed_impressions_of_others:
            n 2fsqanl "Ahora ya.{w=0.3}{nw}"
            extend 2fcsanl " {i}Basta{/i}.{w=0.3}{nw}"
            extend 2fsqful " {i}Ya{/i}."
            $ Natsuki.percentageAffinityLoss(5)
        else:

            n 1fcsan "{b}No{/b} pruebes mi paciencia de nuevo.{w=1.5}{nw}"
            extend 2fsqan " Idiota."
            $ Natsuki.calculatedAffinityLoss(2)
    else:

        n 2fnmantsc "...¿Qué está {i}{w=0.3}mal{w=0.3}{/i} contigo?{w=1.5}{nw}"
        extend 1fnmscltsf " Como,{w=0.1} ¡¿qué {i}demonios{/i} está mal con tu {w=0.2}{i}cabeza{/i}?!"
        n 2fcsanltsd "{b}NO{/b} voy a hacer eso,{w=0.3}{nw}"
        extend 2fcsfultsd " ¡y mucho menos para una joyita como{w=0.25}{nw}"
        extend 1fskwrftdc " {i}tú{/i}!"

        $ Natsuki.calculatedAffinityLoss(3)

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_newspapers_and_bias",
            unlocked=True,
            prompt="Periódicos y sesgo",
            category=["Literatura", "Media", "Sociedad"],
            nat_says=True,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_newspapers_and_bias:
    n 1nllpu "...Huh.{w=1}{nw}"
    extend 4unmaj " Sabes,{w=0.1} [player]..."
    n 1tllaj "De hecho es un poco raro,{w=0.1} mirando atrás."
    n 2fllss "En el club,{w=0.3} quiero decir.{w=0.5}{nw}"
    extend 4tsqpu " {i}Sí{/i} recuerdas qué tipo de club era,{w=0.1} ¿verdad?"
    n 1tnmpu "...Así que ¿no crees que es raro qué {i}pocas{/i} clases de literatura realmente miramos?"
    n 2nllaj "Yuri siempre estaba con la nariz metida en sus libros.{w=0.5}{nw}"
    extend 2nsqss " Y {i}todos{/i} mirábamos poesía,{w=0.5}{nw}"
    extend 2fsrss " obviamente."
    n 1knmaj "¡Pero casi no teníamos nada en ese salón aparte de libros de texto!{w=0.5}{nw}"
    extend 4fllpo " ¡Ni siquiera teníamos el periódico escolar ahí!"
    n 3tsrss "Un poco una contradicción,{w=0.1} ¿eh?"
    n 1tlrpu "Pero...{w=0.5}{nw}"
    extend 1tnmca " hablando de periódicos..."
    n 3fnmca "De hecho es súper importante leerlos apropiadamente,{w=0.1} sabes."
    n 1knmajsbl "¿Qué?{w=0.5}{nw}"
    extend 2fsqpo " ¡Estoy hablando en serio!"
    n 1fllss "Los periódicos realmente ya {i}no{/i} son solo noticias,{w=0.1} [player]...{w=1}{nw}"
    extend 3fcsaj " ¡y no lo han sido por un largo tiempo!"
    n 1flrpu "Es complicado,{w=0.5}{nw}"
    extend 4fnmca " pero tienes que pensar un poco cada vez que abres uno."
    n 3fchbg "¡No son propiedad ni están dirigidos por robots!{w=0.5}{nw}"
    extend 3fcsss " {i}Siempre{/i} habrá opinión que encuentre su camino dentro de alguna manera."
    n 1ullaj "Digo...{w=1}{nw}"
    extend 4fnmaj " ¡toma el periódico escolar que teníamos!"
    n 3tsqss "¿{i}Realmente{/i} crees que un periódico dirigido por {i}estudiantes{/i} va a ser completamente justo sobre la escuela?"
    n 1nlraj "Digamos que el periódico quería más fondos para imprimir más copias o algo,{w=0.5}{nw}"
    extend 1fnmbo " y necesitaban un voto estudiantil para hacer que eso pasara."
    n 4tnmpu "¿En serio van a dejar el destino de su periódico al {i}azar{/i}?"
    n 4fchts "¡Duh!{w=0.5}{nw}"
    extend 1fchgn " ¡Claro que no!{w=1}{nw}"
    extend 4fsqss " ¡Pelearían por ello!"
    n 1ulraj "Tal vez publicarían artículos extra para publicitarlo,{w=0.5}{nw}"
    extend 3fsqsmeme " ¡y {i}solo{/i} entrevistarían a la gente que apoyara el periódico!"
    n 1tlrss "¿O solo {i}casualmente{/i} olvidan mencionar todos los fondos que obtuvieron el semestre pasado?{w=1}{nw}"
    extend 4kchblesd " ¡Qué {i}conveniente{/i}~!"
    n 3fcsbg "Ese es solo un ejemplo,{w=0.1} obviamente."
    n 1fnmaj "¡Pero el mismo pensamiento aplica a cualquier tipo de periodismo!{w=1}{nw}"
    extend 1nllca " Periódicos,{w=0.1} artículos en línea,{w=0.5}{nw}"
    extend 4fnmca " lo que sea que sea."
    n 1fcsbg "¡{i}Todo{/i} está sujeto a sesgo!"
    n 2nllaj "Así que...{w=1}{nw}"
    extend 2tnmss " ¿a dónde voy con esto,{w=0.3} preguntas?"
    n 1fcssm "Ehehe.{w=0.5}{nw}"
    extend 1fsqsm " Creo que es bastante obvio."
    n 1fllss "Sé que te llamo así un montón,{w=0.1} [player]..."
    n 1fcsss "Pero créeme."
    n 3fsqsm "¡Solo los {i}verdaderos{/i} tontos creen {i}todo{/i} lo que leen!"

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_fear_of_flying",
            unlocked=True,
            prompt="¿Le tienes miedo a volar?",
            conditional="jn_utils.get_total_gameplay_days() >= 7",
            category=["Miedos", "Transporte"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_fear_of_flying:
    if Natsuki.isNormal(higher=True):
        n 1tnmbo "Volar,{w=0.1} ¿eh?"
        n 4tllaj "...Sabes,{w=1}{nw}"
        extend 4ulraj " de hecho es un poco raro,{w=0.75}{nw}"
        extend 1unmbo " cuando lo piensas."
        n 3fllss "Cómo la gente puede tener miedo de cosas que nunca han experimentado {i}realmente{/i} antes,{w=0.1} digo."
        n 1ullaj "Es bastante loco cómo la gente tiene estos tipos de miedos incorporados,{w=0.5}{nw}"
        extend 2tnmss " ¿eh?"

        if get_topic("talk_flying").shown_count > 0 or get_topic("talk_fear_of_flying").shown_count > 0:
            n 1ulraj "Digo,{w=0.5}{nw}"
            extend 2nsrss " como te dije antes -{w=0.5}{nw}"
            extend 2tnmbo " nunca he volado a ningún lado yo misma ni nada."
        else:

            n 1ulraj "Digo,{w=0.5}{nw}"
            extend 2tnmbo " nunca he volado a ningún lado yo misma ni nada."

        n 4uskemlesh "P-{w=0.3}pero eso no es decir que {i}yo{/i} tenga miedo de volar,{w=0.5}{nw}"
        extend 2fcspol " ¡obviamente!"
        n 1unmaj "Realmente no creo que me molestaría tanto."
        n 4tlrpu "Aunque...{w=0.75}{nw}"
        extend 1unmbo " Supongo que puedo ver {i}por qué{/i} asustaría a alguien."
        n 3fllbo "Está todo el ruido,{w=0.5}{nw}"
        extend 3fslem " la turbulencia,{w=0.5}{nw}"
        extend 3ksqfr " más el estrés de estar empacado en un tubo con un montón de extraños."
        n 1klrss "¡Y no es como que puedas {i}ignorar{/i} los accidentes cuando pasan!{w=0.75}{nw}"
        extend 1klrsl " Son...{w=0.75}{nw}"
        extend 2kslsr " no...{w=0.5} lindos."
        n 4kslslsbl "...Y una forma fácil de llenar una primera plana."
        n 1unmpu "Así que sí,{w=0.2} totalmente puedo verlo desde ese ángulo.{w=0.5}{nw}"
        extend 2flrpu " Pero..."
        n 2fnmbo "¡Creo que la gente olvida qué tan {i}seguro{/i} es el viaje aéreo!"
        n 1ullaj "Entiendo que sus sentimientos -{w=0.5}{nw}"
        extend 2fslem " {i}y las noticias{/i} -{w=0.5}{nw}"
        extend 1unmbo " les dicen lo contrario.{w=0.75}{nw}"
        extend 4flrss " ¡Pero no es como si las estadísticas {i}mintieran{/i}!"
        n 4unmaj "Algunos estudios han puesto la probabilidad de estirar la pata en un accidente aéreo en una en 11{w=0.5}{nw}"
        extend 1uwdaj " {i}millones{/i}."
        n 3fslss "O,{w=0.1} para ponerlo de otra forma..."
        n 3unmem "¡Eres más de {i}2,000{/i} veces más propenso a patear el balde por un accidente de auto que por un accidente aéreo!"
        n 1tsqss "...¡Y la lista no para ahí,{w=0.1} tampoco!"
        n 2ullss "Rayos,{w=0.5}{nw}"
        extend 2ulraj " montar una bici,{w=0.5}{nw}"
        extend 1nsqsl " caerse de algo..."
        n 1fllss "¡Son todas mucho más riesgosas que cualquier vuelo al que {i}deberías{/i} estar subiéndote!"
        n 1nllsl "..."
        n 1fcspu "...Lo sé,{w=0.1} lo sé.{w=0.5}{nw}"
        extend 3fsrpo " No estoy {i}totalmente{/i} ciega a los riesgos,{w=0.1} [player]."
        n 1nllpu "Es como cualquier cosa."
        n 4unmpu "Las cosas pueden salir mal.{w=1}{nw}"
        extend 2ksrpu " Ellas {i}salen{/i} mal."
        n 1kcsemesi "Y eso {i}es{/i} aterrador."
        n 3tlrpu "Pero...{w=0.75}{nw}"
        extend 3tnmss " ¿honestamente?"
        n 1fsqsm "Es bastante reconfortante saber que cuando tenga la oportunidad de volar a algún lado,{w=0.1} lo máximo que tendré que temer realísticamente..."
        n 4fchgnelg "...¡Es probablemente que vaya a ser la comida de aerolínea!"

        if persistent._jn_player_has_flown:
            n 1fcsbg "Ahora ese es un horror {i}real{/i},{w=0.1} si conozco uno."
            n 3usqsg "¿No estarías de acuerdo,{w=0.3} [player]?{w=0.75}{nw}"
        else:

            n 3fcsbg "Ahora ese es un horror {i}real{/i},{w=0.1} si conozco uno.{w=0.75}{nw}"

        extend 1fsqsmeme " Ehehe."

    elif Natsuki.isDistressed(higher=True):
        n 3fcsemesi "Ugh..."
        n 2fsqem "No,{w=0.2} [player].{w=0.75}{nw}"
        extend 1fsqfr " Tampoco tengo miedo de volar."
        n 4fcsan "¿Qué te crees que soy exactamente?{w=0.75}{nw}"
        extend 4fsqan " E incluso si lo {i}fuera{/i}..."
        n 1fnmfu "¿De verdad crees que sería tan tonta como para compartir eso con alguien como {i}tú{/i}?"
    else:

        n 1fcsem "Oh,{w=1}{nw}"
        extend 2fsqwr " {w=0.2}cá{w=0.2}{b}llate{/b},{w=0.2} [player]."
        n 2fcsantsa "Como {i}si{/i} fuera tan tonta como para compartir cualquier miedo que tenga con un completo perdedor como{w=0.2}{nw}"
        extend 1fcswrltsa " {i}tú{/i}."

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_what_do_you_think_about_fanart",
            unlocked=True,
            prompt="¿Qué piensas sobre el fanart?",
            conditional="jn_utils.get_total_gameplay_days() >= 3",
            category=["Arte", "Media"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_what_do_you_think_about_fanart:
    if Natsuki.isAffectionate(higher=True):
        n 2fsqaj "¿Estás {i}bromeando{/i},{w=0.1} [player]?{w=1}{nw}"
        extend 4uchbsedz " ¡{i}Amo{/i} el fanart!"

    elif Natsuki.isNormal(higher=True):
        n 1unmaj "¡Ooh!{w=1}{nw}"
        extend 3unmbg " ¿Fanart?"
        n 3fllbg "Bueno,{w=0.1} ¡duh!{w=1}{nw}"
        extend 3fcsbg " ¡Estoy {i}totalmente{/i} a favor!"

    elif Natsuki.isDistressed(higher=True):
        n 1fcssf "Ugh...{w=1}{nw}"
        extend 2fsqsl " ¿ahora qué?"
        n 2tsqbo "...¿Fanart?"
        n 1nsrpu "..."
        n 2nllbo "Sí,{w=0.3} el fanart está bien.{w=1}{nw}"
        extend 2fslpu " Supongo."
        n 1ncssf "Puedo apreciar la pasión y el esfuerzo que la gente pone en su amor por algo."
        n 4nlrpu "Como...{w=1}{nw}"
        extend 1ncsaj " incluso si el arte no es el mejor,{w=0.5}{nw}"
        extend 1nllsr " o la música necesita algo de práctica,{w=0.5}{nw}"
        extend 1nnmsl " el esfuerzo de alguien igual fue en ello."
        n 2tnmpu "¿E incluso si no me gusta exactamente para quién es el fanart?"
        n 2fllsl "Aún puedo admirar el trabajo que fue en ello."
        n 1fcssr "...Heh.{w=1}{nw}"
        extend 4fsqsr " Y hablando de cosas que necesitan trabajo..."
        n 1fsqpu "No sé si eres un creador o no,{w=0.1} [player]."
        n 2fsqfr "Pero puedo decir que esta relación no es a donde va {i}tu{/i} trabajo,{w=0.3} ¿o sí?{w=1}{nw}"
        extend 2fsran " Idiota."
        return
    else:

        n 1fcsantsa "Oh,{w=0.1} por-{w=0.5}{nw}"
        n 1fcsun "..."
        n 2fsqfutsb "¿Fanart?{w=1}{nw}"
        extend 2fsquptsb " ¿En serio,{w=0.1} [player]?"
        n 1fcsuptsa "..."
        n 2fcssstsa "...Heh."
        n 1fsqupltse "¿Por qué traerías {i}tú{/i} algo en lo que la gente pone tanto trabajo y amor?"
        n 1fcsemltsd "A ti {i}obviamente{/i} no te importa ninguna de esas cosas,{w=0.1} ¿o sí?"
        return

    n 1ullss "Digo...{w=1}{nw}"
    extend 3fchgn " ¿qué no se puede amar?{w=1}{nw}"
    extend 3uchgnedz " ¡El fanart es {i}asombroso{/i}!{w=0.5}{nw}"
    extend 4fspajedz " ¡Y viene en tantas formas,{w=0.1} también!"
    n 1ulraj "Como seguro,{w=0.1} la gente muestra su apoyo por algo en un montón de formas.{w=0.5}{nw}"
    extend 1nllbo " Compartiendo publicaciones,{w=0.1} asistiendo eventos,{w=0.5}{nw}"
    extend 3nnmsm " todas esas clases de cosas."
    n 3fcsbg "¡Pero creo que toma verdaderas agallas levantarse y crear algo nuevo!"
    n 4uskajesh "¡E-{w=0.1}eso no es decir que aquellos que no hacen nada no son fans {i}reales{/i} ni nada de eso!"
    n 2flleml "¡Claro que no!{w=1}{nw}"
    extend 2flrpol " Eso solo es ser tonto."
    n 1ulraj "Pero...{w=1}{nw}"
    extend 1unmaj " Solo creo que es una forma súper genial de mostrar cuánto aprecias algo."
    n 3fnmss "Además con lo activos que son los creadores en redes sociales ahora,{w=0.5}{nw}"
    extend 3fchbg " ¡es súper fácil contactar y compartir tu trabajo!"
    n 1fsldv "No solo con tu director favorito,{w=0.1} o escritor de manga o lo que sea tampoco,{w=0.5}{nw}"
    extend 4fspajedz " ¡sino con otros fans también!"
    n 1fcsbg "Todos ganan,{w=0.1} ¿verdad?{w=0.5}{nw}"
    extend 1nllbg " Ahaha..."
    n 2kllss "Bueno...{w=0.5}{nw}"
    extend 2nllsl " casi."
    n 1fsqpu "Lo que {i}realmente{/i} odio es cuando la gente mira algo que alguien hizo,{w=0.5}{nw}"
    extend 3fcswr " ¡y luego solo les dan un montón de problemas por ello!"
    n 1flrem "Como si el creador estuviera aprendiendo y cometiera un error,{w=0.1} o si tuvieran otra visión de algo.{w=1}{nw}"
    extend 4fcsan " ¡Es tan estúpido!"
    n 1fcsaj "Entiendo la crítica {i}constructiva{/i},{w=1}{nw}"
    extend 2fsqan " pero ¿solo ser un idiota porque no es {i}exactamente{/i} como {i}tú{/i} lo quieres?{w=1}{nw}"
    extend 2fcsem " ¡Vamos!"
    n 2fsrem "Madura."
    n 1fcsemesi "..."
    n 3fslsl "Es difícil creer que la gente pueda sentirse con tanto {i}derecho{/i} sobre algo que otros hacen gratis,{w=0.1} ¿eh?{w=0.5}{nw}"
    extend 3fslpo " Idiotas."
    n 3nllpo "Bueno,{w=0.1} como sea.{w=1}{nw}"
    extend 3nslpo " Suficiente sobre gente como {i}esa{/i}."
    n 1nlrbo "No sé si haces algún fanart o algo,{w=0.1} [player]..."

    if jn_activity.ACTIVITY_MANAGER.hasPlayerDoneActivity(jn_activity.JNActivities.artwork):
        n 4fchsmleme "Probablemente~."

    n 2fnmpo "¡Pero más te vale no estar dejando que la gente te mandonee sobre el tuyo!"
    n 2fsqpo "...O estar dándole a la gente problemas sobre el suyo."
    n 1fcsbg "...¡Porque ahí es donde pongo el {i}límite{/i}!{w=1}{nw}"
    extend 1fsqsm " Ehehe."

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_how_to_interview_properly",
            unlocked=True,
            prompt="Cómo hacer una buena entrevista",
            conditional="jn_utils.get_total_gameplay_days() >= 5",
            category=["Vida", "Sociedad"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_how_to_interview_properly:
    n 1fllbo "Hmm..."
    n 2tllbo "Hey,{w=0.5}{nw}"
    extend 4tnmpu " [player]."
    n 1tlrbo "Es algo de la nada,{w=0.5}{nw}"
    extend 2nsrss " pero tenía curiosidad."
    n 2tnmaj "¿Cuándo fue la última vez que te entrevistaste para algo?"
    n 1tlrbo "O...{w=0.5} ahora que lo pienso...{w=1}{nw}"
    extend 4tnmpu " ¿te has entrevistado para {i}algo{/i} antes?{w=1}{nw}"
    extend 4unmaj " Como,{w=0.1} ¿en absoluto?"
    n 2fslss "Porque si hay una cosa que he escuchado...{w=1}{nw}"
    extend 2fnmpo " ¡es qué tan ansiosos todos parecen ponerse sobre las entrevistas!"
    n 2ksqposbl "¡Estoy hablando en serio!{w=0.5}{nw}"
    extend 4fllem " La gente simplemente se pone tan alterada por todo eso.{w=1}{nw}"
    extend 4fcsem " Como si fuera ciencia espacial o algo."
    n 1flraj "Digo...{w=1}{nw}"
    extend 1unmca " Nunca he tenido que entrevistarme para nada súper importante yo misma."
    n 1ulraj "Tuvimos algunas entrevistas de práctica en la escuela,{w=0.1} obviamente.{w=1}{nw}"
    extend 2nslss " Estaba muy ocupada con los estudios para intentar conseguir un trabajo de medio tiempo o algo."
    n 2fsqsg "...¿Pero quién dice que eso no significa que pueda enseñarte una cosa o dos?{w=0.75}{nw}"
    extend 2fchgn " Ehehe."
    n 1fsqsm "Deberías saber qué hora es para ahora..."
    n 1fcsbg "...Así que escucha,{w=0.1} [player]!"
    n 3fcscsesm "¡Estás a punto de aprender cómo dominar tus entrevistas de una profesional!"

    n 1fnmbg "¡Entonces!{w=0.75}{nw}"
    extend 1fsqsm " La primera orden del día..."
    n 3fllbg "Investigación,{w=0.5}{nw}"
    extend 3tsqss " ¡duh!"
    n 1usqaj "Si hay una cosa que tienes que saber antes de ir a entrevistarte para algo,{w=0.5}{nw}"
    extend 3fchgnelg " ¡es para qué te estás entrevistando {i}realmente{/i}!"
    n 1fllaj "No escatimarías en repasar antes de un gran examen,{w=1}{nw}"
    extend 4tnmsl " y las entrevistas realmente no son muy diferentes cuando lo piensas."
    n 4fnmss "¿Entrevistándote para alguna compañía importante?{w=1}{nw}"
    extend 1fcsbg " ¡Búscalos en línea y toma notas!"
    n 1ullaj "Obviamente necesitas leer sobre qué hacen y dónde {i}están{/i} realmente,{w=1}{nw}"
    extend 4fnmaj " ¡pero no subestimes el poder de la trivia!"
    n 1ullpu "Incluso solo saber cosas al azar como cuándo fueron fundados,{w=1}{nw}"
    extend 1nlrss " o qué premios ganaron recientemente {w=0.1}-{w=0.5}{nw}"
    extend 3fcsss " todo muestra el esfuerzo que estás poniendo."
    n 3tsqss "¿Y cuando todo se reduce al último momento?"
    n 3fsqbg "Incluso algo diminuto como eso puede casi inclinar la balanza."

    n 1fcsss "Siguiente...{w=0.5}{nw}"
    extend 2fnmca " ¡repaso!"
    n 4ullaj "No importa si estás tratando de conseguir un trabajo,{w=1}{nw}"
    extend 4nlrbo " o conseguir una nueva posición en algún tipo de consejo."
    n 1nsqpu "Lo que sea que sea...{w=0.5}{nw}"
    extend 3fchlgelg " ¡tienes que ser capaz de {i}probar{/i} que sabes de qué estás hablando siquiera!"
    n 1ulraj "Por supuesto, el repaso depende totalmente de a qué vas."
    n 4usqss "¿Algún tipo de trabajo de programación?{w=0.5}{nw}"
    extend 4fchbg " ¡Refréscate en toda tu extraña terminología y técnicas!"
    n 3tsgsm "¿Uniéndote al club de historia?{w=1}{nw}"
    extend 3fcsss " ¡Lee sobre algunas preguntas de historia comunes!"
    n 1nsqpu "Y créeme,{w=0.75}{nw}"
    extend 1nsqsr " la {i}última{/i} cosa que quieres hacer es avergonzarte por cosas simples que {i}realmente{/i} deberías saber..."
    n 1nllun "...O algo que olvidaste que mencionaste en tu solicitud."
    extend 4kchblesd " ¡Oops!"
    n 1nllaj "Así que...{w=0.5}{nw}"
    extend 3fcsss " estudia,{w=0.1} ¿okay?"

    n 1fchbg "¡Muy bien!{w=0.75}{nw}"
    extend 3tsqss " ¿Siguiéndome hasta ahora,{w=0.1} [player]?"
    n 3fsqsm "Más te vale...{w=1}{nw}"
    extend 3fchgn " ¡porque casi terminamos aquí!"
    n 1unmaj "Entonces,{w=0.1} siguiente en la lista -{w=0.5}{nw}"
    extend 1nsrss " y probablemente lo más importante de todo..."
    n 4fspajedz "¡Presentación!"
    n 1fllaj "Puedes tener las mejores credenciales del mundo,{w=1}{nw}"
    extend 3fsqsr " pero eso no va a ayudar mucho si estás balbuceando todo {w=0.1}-{w=0.5}{nw}"
    extend 3fchlgelg " ¡o si simplemente te ves ridículo!"
    n 1fnmsr "¡Así que!"
    n 2fcspo "Asegúrate de vestirte apropiadamente para lo que sea que sea.{w=1}{nw}"
    extend 2fllpu " Si hay un código de vestimenta,{w=0.1} {i}síguelo{/i}."
    n 2fsqpo "...Y {i}no{/i} descuides tu ropa.{w=1}{nw}"
    extend 4nlrbo " Plánchala si está toda arrugada,{w=0.1} compra nueva si necesitas.{w=0.2} Esa clase de cosas."
    n 2tnmpu "Pero más que nada,{w=0.1} [player]?"
    n 2fsqaj "{i}Nunca{/i}{w=0.2} olvides lo básico."
    n 1ullss "Sé puntual,{w=0.1} sé educado.{w=0.2} Recuerda {w=0.1}-{w=0.5}{nw}"
    extend 2fsqss " la gente quiere a alguien que les pueda {i}agradar{/i},{w=0.75}{nw}"
    extend 2fsrpo " ¡no solo alguien que pueda hacer el trabajo!"

    n 4unmajesu "...Oh,{w=0.5}{nw}"
    extend 2tnmpu " ¿y [player]?"
    n 1fcspu "Solo...{w=1}{nw}"
    extend 4knmsrlsbl " sé honesto también,{w=0.1} ¿está bien?"
    n 1fllsrl "No es una falta admitir cuando no sabes algo."
    n 1tnmpu "Y cuando realmente te detienes a pensarlo desde su perspectiva,{w=1}{nw}"
    extend 2tnmem " si alguien está preparado para simplemente mentirte en tu cara en una entrevista..."
    n 2tsqem "...Entonces ¿sobre qué {i}más{/i} van a mentir?"
    n 1tllsssbl "Solo algo en qué pensar."

    n 1ncspuesi "..."
    n 1nlrss "...Wow,{w=0.5}{nw}"
    extend 3fchbgelg " ¡Tengo que aprender cuándo dejar de divagar!{w=0.2} ¡Cielos!"
    n 3fsrssl "Eso fue casi como un discurso de entrevista en sí mismo,{w=0.1} ¿eh?"

    if Natsuki.isEnamored(higher=True):
        n 1ullpu "O...{w=1}{nw}"
        extend 2nsrssl " supongo que más como una inducción,{w=0.1} realmente."
        n 2fsqdvf "Ya obtuviste el trabajo conmigo,{w=0.1} d-{w=0.3}después de todo."

        if Natsuki.isLove(higher=True):
            n 1fchsml "Ehehe.{w=1}{nw}"
            extend 1nchbll " ¡Te amo,{w=0.1} [player]~!"
        else:

            n 1fsrsml "Ehehe..."
    else:

        n 1ullpu "O...{w=1}{nw}"
        extend 2tnmbo " ¿ya que estamos atrapados aquí?"
        n 1fsqsm "...Más como una inducción,{w=0.1} a decir verdad."
        n 3fchgn "Ehehe."

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_windup_bullying",
            unlocked=True,
            prompt="Acoso",
            category=["Sociedad", "Cierres"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_windup_bullying:
    n 1fslpu "..."
    n 2fcspuean "¡Tch!"
    n 2fsran "..."
    n 1tnmaj "¿Eh?{w=0.5}{nw}"
    extend 4uskemesh " ¡O-{w=0.3}oh!{w=0.5}{nw}"
    extend 1uwdaj " [player].{w=1}{nw}"
    extend 2flrbglsbl " Ahaha."
    n 1fllbg "Yo...{w=0.5} estaba como que pensando en voz alta de nuevo."
    n 1ullpu "Y,{w=0.75}{nw}"
    extend 2nslpu " bueno..."
    n 1nsqpu "Solo se me vino algo más a la mente.{w=1}{nw}"
    extend 2fcsem " Algo que {i}realmente{/i} no soporto."
    n 1fsqsr "Acosadores.{w=1}{nw}"
    extend 2fcsfu " ¡No puedo pensar en nada que {i}odie{/i} más!"
    n 1flrem "Como,{w=0.5}{nw}"
    extend 4fsqfu " ¿alguna vez has tenido el {i}placer{/i} de lidiar con uno?"
    n 1fcsan "Se necesita ser una {i}real{/i} joyita para salir y meterse con la gente a propósito."
    n 2fllwr "¡Ni siquiera necesitas estar {i}haciendo{/i} nada!"
    n 2flrem "Solo mirar de la manera 'equivocada',{w=0.3}{nw}"
    extend 2fllan " disfrutar la cosa 'equivocada' {w=0.1}-{w=0.3}{nw}"
    extend 4fsqfu " cualquier supuesta {i}excusa{/i},{w=0.1} la tomarán."
    n 1fcsem "Y cuando digo meterse con la gente...{w=1}{nw}"
    extend 1fsqem " ¡no solo quiero decir físicamente,{w=0.1} tampoco!"
    n 2fllem "Los acosadores pueden hacer su trabajo sucio en tantas formas diferentes,{w=0.1} especialmente con las redes sociales siendo lo que son ahora.{w=1}{nw}"
    extend 2fcsfu " ¡Pero eso es igual de tóxico!"
    n 1fsqan "Y peor aún,{w=0.5}{nw}"
    extend 2tsqem " ¿si tratas de defenderte?{w=1}{nw}"
    extend 2fsrem " ¿Cuando estás exhausto de lidiar con toda su mierda?"
    n 1fcswrean "¡La gente se pone tan altiva al respecto!{w=0.75}{nw}"
    extend 1flrem " ¡Como si {i}tú{/i} fueras la razón de que hay un problema!"
    n 4fllaj "'¡Deja de ser tan dramático!'{w=0.5}{nw}"
    extend 4flrwr " '¡Solo estás exagerando!'{w=0.5}{nw}"
    extend 2fcsemesi " Ugh."
    n 2tsqem "¿A este punto?{w=0.75}{nw}"
    extend 2flrbo " Lo he oído todo."
    n 1fsrbosbl "{i}...No como si eso lo hiciera menos molesto.{/i}"
    n 1nllaj "Pero...{w=1}{nw}"
    extend 1nsqbo " una cosa que {i}sí{/i} te diré ahora mismo,{w=0.1} [player]."
    n 2fsqbol "{b}No{/b} dejes que lo que otros digan te detenga de lidiar con eso."
    n 2fllbol "No es {i}su{/i} problema {w=0.1}-{w=0.3}{nw}"
    extend 4fsqpul " ¿y por experiencia?"
    n 1fsqsr "No hay nada que a un acosador le guste {i}más{/i} que alguien que trata de ignorarlos,{w=0.1} o alejarse."
    n 4uskemesu "...¡E-{w=0.3}eso no quiere decir que tengas que enloquecer o algo loco como eso!{w=0.75}{nw}"
    extend 1fcsem " Solo..."
    n 3ksqpo "Lee el ambiente,{w=0.1} ¿sabes?{w=0.75}{nw}"
    extend 3fllpo " ¡El contexto importa!"
    n 1fcsaj "Siempre asegúrate de usar las mejores herramientas que tengas para quitarte a cualquier idiota de encima."
    n 1fsrss "Un acosador escolar no tiene exactamente un gerente con el que reportarse..."
    n 3fchgnelg "...¡Y el trabajo es el {i}último{/i} lugar para una pelea!{w=0.75}{nw}"
    extend 3fslpol " Por tan {i}aburrido{/i} que sea eso."
    n 1nllaj "Así que...{w=0.5}{nw}"
    extend 2fsrpol " defiéndete,{w=0.1} ¿entendido?"
    n 1fllss "Y asegúrate de usar tu cerebro cuando lo hagas.{w=1}{nw}"
    extend 3fchgn " ¡Es todo lo que digo!"

    if Natsuki.isEnamored(higher=True):
        n 3knmpo "Te debes eso a ti mismo,{w=0.1} ¿verdad?{w=0.75}{nw}"
        extend 1fsqss " Además,{w=0.1} [player]..."
        n 4fsrssl "Me gusta alguien que pueda mostrar un poco de agallas.{w=0.75}{nw}"

        if Natsuki.isLove(higher=True):
            extend 4fwlcsl " Ehehe."
        else:

            extend 4fsldvless " Ehehe..."

    elif Natsuki.isHappy(higher=True):
        n 3kslpo "Te debes eso a ti mismo...{w=0.75}{nw}"
        extend 3ksqpolsbl " ¿verdad?"
    else:

        n 3fsrpolsbl "Te debes a ti mismo {i}eso{/i},{w=0.1} al menos."

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_player_change_name",
            unlocked=True,
            prompt="¿Puedes llamarme de otra forma?",
            conditional="persistent._jn_nicknames_player_allowed",
            category=["Tú"],
            player_says=True,
            affinity_range=(jn_affinity.ENAMORED, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_player_change_name:

    if (
        persistent._jn_nicknames_player_allowed
        and persistent._jn_nicknames_player_current_nickname == persistent.playername
    ):
        n 1unmaj "¿Huh?{w=0.5}{nw}"
        extend 2tnmbo " ¿Quieres que te llame de otra forma?"
        n 1ulraj "...Digo,{w=1}{nw}"
        extend 4tnmbo " ¿supongo que puedo hacer eso?"
        n 2nslsslesd "Va a ser súper raro llamarte algo {i}diferente{/i} a [player],{w=0.1} aunque..."
        n 1fcsbgl "Bueno,{w=0.1} ¡lo que sea!{w=0.75}{nw}"
        extend 1uchgn " ¡No soy quien para juzgar!"
        n 1unmbg "Entonces..."
        show natsuki 3uchbgl at jn_center
    else:




        if persistent._jn_nicknames_player_bad_given_total == 0:
            n 4unmaj "¿Oh?{w=0.5}{nw}"
            extend 4unmbo " ¿Quieres cambiar tu nombre de nuevo?"
            n 1fchbg "¡Okaaay!{w=0.75}{nw}"
            extend 1fchsml " Ehehe."
            show natsuki 3fchbgl at jn_center

        elif persistent._jn_nicknames_player_bad_given_total == 1:
            n 1unmbo "¿Quieres que te llame de otra forma de nuevo?{w=0.75}{nw}"
            extend 4unmaj " Seguro."
            show natsuki 4unmbo at jn_center

        elif persistent._jn_nicknames_player_bad_given_total == 2:
            n 2nsqtr "¿Esto otra vez,{w=0.1} [player]?{w=0.75}{nw}"
            extend 1ncsaj " Muy bien,{w=0.1} bien."
            n 1ncspu "Solo...{w=0.3}{w=1}{nw}"
            extend 2nsqsl " piénsalo apropiadamente,{w=0.1} ¿de acuerdo?"
            n 1nllaj "Así que..."
            show natsuki 2unmca at jn_center

        elif persistent._jn_nicknames_player_bad_given_total == 3:
            n 2fsqsr "..."
            n 1fcsboesi "..."
            n 1fslsl "...Bien,{w=0.1} [player]."
            n 2fsqpu "Solo ten en mente lo que dije la {i}última vez{/i}."
            show natsuki 2nsqsl at jn_center


    $ nickname = renpy.input(prompt="¿En qué estabas pensando,{w=0.3} [player]?", allow=jn_globals.DEFAULT_ALPHABETICAL_ALLOW_VALUES, length=10).strip()

    if nickname.lower() == "nevermind" or nickname.lower() == "olvidalo":
        n 1nnmbo "Oh.{w=1}{nw}"
        extend 2nllpo " Bueno,{w=0.1} supongo que está bien...{w=1}{nw}"
        n 1uchgn "¡Solo significa menos que tengo que recordar!{w=0.5}{nw}"
        extend 4fchsmelg " Ehehe."

        return
    else:

        $ nickname_type = jn_nicknames.getPlayerNicknameType(nickname)

    if nickname_type == jn_nicknames.NicknameTypes.invalid:
        n 1fllpu "Es...{w=1}{nw}"
        extend 3tnmpu " ¿estás seguro de que eso es siquiera un {i}nombre{/i}?"
        n 3tlrpo "..."
        n 1nlrss "...Sí,{w=0.75}{nw}"
        extend 4nsqbgsbl " creo que solo me quedaré con [player].{w=0.5}{nw}"
        extend 4fchblsbr " ¡Lo siento!"

        return

    elif nickname_type == jn_nicknames.NicknameTypes.disliked:
        n 1fsqemsbl "... ¿En serio,{w=0.1} [player]?{w=0.75}{nw}"
        extend 2fnmwrsbl " ¿Por qué siquiera {i}sugerirías{/i} eso?"
        n 2flleml "¡Debes haber {i}sabido{/i} que no me gustaría!"
        n 1fcsslesi "..."
        n 1ncspu "...Lo que sea.{w=1}{nw}"
        extend 2fsrsl " Tal vez simplemente no estabas usando tu cabeza lo suficiente."
        n 2fcspu "Solo...{w=0.3} {i}piensa{/i} un poco más la próxima vez."
        n 4knmsll "¿Por favor?"

        return

    elif nickname_type == jn_nicknames.NicknameTypes.hated:
        n 2fskwrlesh "... ¡¿D-{w=0.2}disculpa?!"
        $ player_initial = jn_utils.getPlayerInitial()
        n 1fnmwr "[player_initial]-{w=0.2}[player]!{w=0.75}{nw}"
        extend 1fnmfu " ¡Ese es un nombre {b}horrible{/b}!"
        n 2fcsan "... ¡Y sería aún {i}más{/i} horrible usarlo!"
        n 2fsqfu "¡{i}No{/i} va a pasar,{w=0.1} [player]!"
        $ persistent._jn_nicknames_player_bad_given_total += 1

    elif nickname_type == jn_nicknames.NicknameTypes.profanity:
        n 1fscwresh "¡¿D-{w=0.2}Dijiste {i}qué{/i} ahora?! {w=1}{nw}"
        extend 2fsqfuean "¡¿E-{w=0.1}Es algún tipo de broma?!."
        n 1fcssc "¡No me voy a involucrar con porquerías así!"
        n 2fcsan "Y a menos que quieras una barra de jabón exprés a tu {b}boca{/b}..."
        n 2fsqfu "Sugiero que {i}tú{/i} tampoco lo hagas."
        $ persistent._jn_nicknames_player_bad_given_total += 1

    elif nickname_type == jn_nicknames.NicknameTypes.funny:
        n 1fsgdv "..."
        n 3fchgnesm "¡Pffffft!"
        n 3fchbs "¡Vamos,{w=0.3} tonto!{w=0.75}{nw}"
        extend 3fchgnelg " Sé serio,{w=0.1} ¿quieres?"
        n 4flldvl "¡De ninguna manera voy a llamarte {i}eso{/i}!"

        return
    else:

        $ neutral_nickname_permitted = False


        if nickname.lower() == player.lower():
            n 2tslsssbl "..."
            n 1tnmsssbl "...¿Negocios como siempre entonces,{w=0.2} [player]?{w=0.75}{nw}"
            extend 1fsqsm " Ehehe."
            n 3fchbl "Bueno,{w=0.2} ¡lo que digas!"

            $ neutral_nickname_permitted = True


        elif nickname.lower() == persistent.playername.lower():
            n 2tsgcs "¿Oho?{w=0.75}{nw}"
            extend 2tsqsg " ¿Finalmente aburriéndonos de todos los apodos,{w=0.1} eh?"
            n 1fchsm "Ehehe."
            n 1fchbgeme "¡Correcto!{w=0.75}{nw}"
            extend 3fwlbl " ¡El viejo y confiable [nickname] es!"

            $ neutral_nickname_permitted = True


        elif nickname.lower() == n_name.lower() and n_name.lower() != "natsuki":
            n 1nllaj "Tú...{w=1}{nw}"
            extend 2tsqbo " realmente {i}no{/i} pensaste bien esto,{w=0.1} ¿o sí?"
            n 2tsqpueqm "Do you even know how confusing that'd be?"
            n 1fcsbg "Nah.{w=0.5}{nw}"
            extend 3fchgnelg " Business as usual it is!"
        else:


            n 2tnmss "[nickname],{w=0.1} ¿eh?"
            n 1fllbo "Hmm..."
            n 1unmbg "Bueno,{w=0.1} ¡me sirve!{w=0.75}{nw}"
            extend 4uchsmeme " ¡Considéralo hecho,{w=0.3} [nickname]!"

            if nickname.lower() == "natsuki":
                n 2nslsssbl "...Je."
                n 1nsldvsbl "{i}Natsuki{/i}."

            $ neutral_nickname_permitted = True


        if (neutral_nickname_permitted):
            $ persistent._jn_nicknames_player_current_nickname = nickname
            $ player = persistent._jn_nicknames_player_current_nickname

        return


    if persistent._jn_nicknames_player_bad_given_total == 1:
        n 2fcsem "Cielos...{w=1}{nw}"
        extend 2tnmem " ¿quién te levantó con el pie {i}izquierdo{/i} esta mañana?"
        n 1fllsl "..."
        n 3fcsslesi "...Mira,{w=0.1} [player]."
        n 1fnmsl "Lo entiendo.{w=0.75}{nw}"
        extend 1flrbo " Tal vez pensaste que estabas siendo gracioso o algo."
        n 3fnmfr "Solo basta ya,{w=0.1} ¿de acuerdo?{w=1}{nw}"
        extend 3tsqpu " ¿Porque honestamente?"
        n 1fslsl "Realmente {i}no{/i} veo la gracia."


        $ Natsuki.addApology(jn_apologies.ApologyTypes.bad_player_name)
        $ Natsuki.percentageAffinityLoss(1)

    elif persistent._jn_nicknames_player_bad_given_total == 2:
        n 2fcsan "Honestamente no puedo creerte,{w=0.1} [player].{w=1}{nw}"
        extend 1fsqfr " ¿Siquiera estabas {i}escuchando{/i} la última vez?{w=1}{nw}"
        extend 4fnmem " ¿Siquiera me {i}oíste{/i}?"
        n 3fcssfesi "..."
        n 1fsqsf "...Muy bien,{w=0.1} mira.{w=1}{nw}"
        extend 1fsqbo " Solo voy a ir al grano,{w=0.1} así que escucha."
        n 2fnmem "{i}Deja de fregar conmigo con esto,{w=0.1} [player].{/i}"
        n 2fcsem "Haces que sea...{w=0.75}{nw}"
        extend 1fcsunl " difícil...{w=0.75}{nw}"
        extend 1fsrunl " que me agrades cuando te comportas {i}así{/i}."


        $ Natsuki.addApology(jn_apologies.ApologyTypes.bad_player_name)
        $ Natsuki.percentageAffinityLoss(2.5)

    elif persistent._jn_nicknames_player_bad_given_total == 3:
        n 2fcsful "Simplemente eres {i}irreal{/i},{w=0.1} [player]."
        n 1fsqscean "¡¿{i}Cuántas veces{/i} tengo que regañarte sobre esto para que entres en razón?!"
        n 1fsqwrean "¿Estás {i}tratando{/i} de ganarte un golpe?"
        n 2fcsfuesi "..."
        n 2fcsan "Bueno,{w=0.3} ¿sabes qué?{w=1}{nw}"
        extend 1fsqan " Estoy harta de esto."
        n 1fcswr "He {b}terminado{/b} de darte oportunidades con esto,{w=0.3} [player].{w=1} Estás en hielo {i}muy{/i} delgado."
        show natsuki 1fsqfu at jn_center

        menu:
            n "¿Entiendes?"
            "Entiendo":

                n 2fsqsr "Je.{w=0.75}{nw}"
                extend 1fnmfr " {i}Ahora{/i} entiendes,{w=0.1} ¿verdad?"
                n 4fsqem "...Entonces {i}actúa{/i} como tal,{w=0.1} [player]."

                $ Natsuki.percentageAffinityLoss(3)
            "...":

                n 2fsqem "...¿En serio,{w=0.1} [player]?{w=1}{nw}"
                extend 1fsqsr " ¿Realmente vas a actuar como un niño sobre esto?"
                n 2fcsan "Basta y {i}madura{/i}."

                $ Natsuki.percentageAffinityLoss(5)


        $ Natsuki.addApology(jn_apologies.ApologyTypes.bad_player_name)

    elif persistent._jn_nicknames_player_bad_given_total == 4:

        n 1fcsem "Je.{w=1}{nw}"
        extend 2fsqemean " Simplemente {i}no pudiste resistirte{/i},{w=1}{nw}"
        extend 2fsqslean " ¿o sí?"
        n 1fcsan "He {b}terminado{/b} contigo haciéndome quedar como tonta con esto."
        n 1fsqfu "No digas que no te lo advertí.{w=2}{nw}"
        extend 2fsrsr " Idiota."


        python:
            get_topic("talk_player_change_name").lock()
            Natsuki.percentageAffinityLoss(10)
            persistent._jn_nicknames_player_allowed = False
            persistent._jn_nicknames_player_current_nickname = persistent.playername
            player = persistent.playername
            Natsuki.addApology(jn_apologies.ApologyTypes.bad_player_name)

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_players_birthday_intro",
            unlocked=True,
            prompt="Mi cumpleaños",
            category=["Tú"],
            player_says=True,
            affinity_range=(jn_affinity.AFFECTIONATE, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_players_birthday_intro:

    if jnIsPlayerBirthday():
        n 4tnmpueqm "¿Huh?{w=0.75}{nw}"
        extend 1tnmaj " ¿Qué hay de tu cumpleaños,{w=0.2} [player]?"
        n 1fsqsm "Ya lo estamos {i}celebrando{/i},{w=0.75}{nw}"
        extend 2tsqss " ¿o no?"
        n 1fsqsm "Ehehe."
        n 3fcsbg "Lo siento,{w=0.2} [player]..."
        n 3fchgnlelg "¡Pero nada de doblete para ti!"

        return


    elif get_topic("talk_players_birthday_intro").shown_count > 0:
        n 4tnmpueqm "¿Huh?{w=0.75}{nw}"
        extend 1tnmbo " ¿Tu cumpleaños?"

        if persistent._jn_player_birthday_day_month is not None:
            n 2fslaj "Espera...{w=1}{nw}"
            extend 2fsrpu " ¿no habías compartido eso ya conmigo?"
            n 1fskajesh "...{w=0.5}{nw}"
            n 4fnmem "¡H-{w=0.3}hey!"
            n 1fsqsm "Buen intento,{w=0.2} [player].{w=1}{nw}"
            extend 3fcsbgesm " ¡Pero no obtendrás nada temprano!"
            n 3tsqsg "Supongo que vas a tener que esperar~."
            n 1fchsm "Ehehe."

            return
        else:

            n 1unmaj "¡Oh,{w=0.2} cierto!{w=1}{nw}"
            extend 3tnmss " Nunca me lo {i}dijiste{/i} realmente,{w=0.2} ¿o sí?{w=0.75}{nw}"
            extend 1tllss " ¡Duh!"
            n 1ullaj "Entonces..."

        menu:
            n "¿Querías compartir tu cumpleaños conmigo ahora,{w=0.2} [player]?"
            "¡Por supuesto!":

                n 3fcssmesm "Ehehe.{w=0.5}{nw}"
                extend 1fcsbg " ¡Sabía que cederías!"
                n 4usgcsl "Supongo que realmente no puedes decirle 'No' a una chica linda,{w=0.2} ¿eh?{w=1}{nw}"
                extend 4fllbgl " Ahaha."
                n 1uskajesh "¡Oh!{w=0.5}{nw}"
                extend 1nllss " Cierto,{w=0.2} antes de que lo olvide."
                n 2fnmpu "No es que {i}espere{/i} que te equivoques,{w=0.2} pero quiero hacer un registro {b}permanente{/b} de esto."
                n 1ullbo "Así que...{w=1}{nw}"
                extend 3nsqpo " sin tonterías,{w=0.2} ¿de acuerdo?{w=1}{nw}"
                extend 3nchgn " ¡Se agradece!"
            "Aún no me siento cómodo compartiendo eso":


                n 2kwmsr "[player]...{w=1.5}{nw}"
                extend 2ksrbo " vamos..."
                n 1kslca "No voy a burlarme de ti sobre eso,{w=0.2} ni nada..."

                return
    else:


        n 1nslbo "...Huh."
        n 2tnmbo "Sabes,{w=0.2} [player].{w=1}{nw}"
        extend 2unmaj " Realmente creo que te estoy llegando a conocer un poco más ahora."
        n 4flrbg "Ya hemos estado hablando un montón,{w=0.2} después de todo."

        if persistent.jn_player_appearance_eye_colour:
            n 1ulraj "Digo,{w=0.75}{nw}"
            extend 3nchbg " ¡incluso sé cómo te {i}ves{/i} ahora!"
            n 3fchsmeme "Si {i}esa{/i} no es una señal de confianza,{w=0.2} no estoy segura de cuál es."

        n 1nllpu "Pero...{w=1}{nw}"
        extend 1nnmsr " algo acaba de golpearme.{w=1}{nw}"
        extend 2nsqca " Algo importante."
        n 4uskem "...¡Y es que no tengo literalmente idea de cuándo es tu {i}cumpleaños{/i}!{w=1}{nw}"
        extend 1fbkwr " ¡Nunca se me ocurrió {i}preguntar{/i}!"
        n 1kcsemesi "Hombre...{w=1}{nw}"
        extend 3fslpol " ¡No puedo {i}creer{/i} que nunca saqué eso antes...!"
        n 3fsqpo "Y vamos.{w=0.5}{nw}"
        extend 3nsqpo " Seamos realistas,{w=0.2} aquí."
        n 1fcswr "¡¿Qué clase de amiga se pierde los cumpleaños?!"
        n 4kllbo "...Especialmente cuando solo hay {i}un{/i} cumpleaños que recordar hoy en día."
        n 4ksrsl "..."
        n 2fcseml "C-{w=0.3}como sea!"
        n 2flrpo "Tendría que ser una verdadera idiota para no {i}al menos{/i} preguntar."

        if get_topic("talk_aging").shown_count > 0:
            n 2nllaj "Creo que mencioné antes cómo no me importa realmente qué tan viejo eres,{w=1}{nw}"
            extend 2nllpol " solo quiero asegurarme de no perderme la fecha."
            n 1fcsbg "¡No estoy contando velas para el pastel de nadie!{w=0.5}{nw}"
            extend 3fcssmesm " Jajaja."

        n 4unmaj "Entonces...{w=0.3} ¿qué dices,{w=0.2} [player]?"

        menu:
            n "¿Querías compartir tu cumpleaños conmigo?"
            "¡Seguro!":

                n 3fcsbgl "¡S-sí!{w=0.5}{nw}"
                extend 3fcssml " ¡Sabía que lo harías!"
                n 1ullaj "Sé que pregunté qué clase de amiga se perdería un cumpleaños..."
                n 2flrpo "¡Pero no puedes perderte algo de lo que no sabías!"
                n 4uskajesh "¡Oh!{w=0.5}{nw}"
                extend 4nllss " Cierto,{w=0.2} antes de que lo olvide."
                n 1fnmpu "No es que {i}espere{/i} que te equivoques,{w=0.2} pero quiero hacer un registro {b}permanente{/b} de esto."
                n 1ullbo "Así que...{w=1}{nw}"
                extend 3nsqpo " sin tonterías,{w=0.2} ¿de acuerdo?{w=1}{nw}"
                extend 3nchgn " ¡Apreciado!"
            "No me siento cómodo compartiendo eso":


                n 1nnmbo "...Oh."
                n 2fcseml "B-{w=0.3}bueno,{w=0.2} está bien,{w=0.5}{nw}"
                extend 2flrpo " supongo."
                n 2nsqpo "Solo déjame saber si cambias de opinión entonces,{w=0.2} ¿oc?"

                return

    n 1nchbg "¡Muy bien!"
    jump talk_players_birthday_input

label talk_players_birthday_input:
    n 1fsqsm "Entonces...{w=1}{nw}"
    extend 3tsqsm " ¿en qué {b}mes{/b} naciste,{w=0.2} [player]?"
    show natsuki 3tsqsm at jn_left


    python:

        month_options = [
            ("Enero", 1),
            ("Febrero", 2),
            ("Marzo", 3),
            ("Abril", 4),
            ("Mayo", 5),
            ("Junio", 6),
            ("Julio", 7),
            ("Agosto", 8),
            ("Septiembre", 9),
            ("Octubre", 10),
            ("Noviembre", 11),
            ("Diciembre", 12),
        ]
    call screen scrollable_choice_menu(month_options)

    if isinstance(_return, int):
        show natsuki at jn_center
        $ player_birthday_month = _return

    $ response_month = datetime.date(datetime.date.today().year, player_birthday_month, 1).strftime("%B")
    $ spanish_months = ["", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    $ response_month_es = spanish_months[player_birthday_month]

    n 4unmbo "[response_month_es],{w=0.2} ¿eh?{w=1}{nw}"
    extend 1nchbg " ¡Entendido!"
    n 1unmss "¿Y qué hay del {b}día{/b}?"


    $ player_input_valid = False
    $ import calendar
    while not player_input_valid:
        $ player_input = renpy.input(
            prompt="¿En qué día naciste?",
            allow=jn_globals.DEFAULT_NUMERICAL_ALLOW_VALUES, length=2
        )
        $ player_input = int(player_input) if player_input.isdigit() else None

        if not player_input or player_input == 0:
            n 4tsqpueqm "¿Huh?{w=1}{nw}"
            extend 2fnmpo " ¡Vamos,{w=0.2} [player]!{w=0.2} ¡Tienes que decirme qué día!"


        elif not jnGetIsDateValid(2020, player_birthday_month, player_input):
            n 1fsqsr "[player].{w=0.2} Por favor.{w=1}{nw}"
            extend 2nsqpo " Tómate esto en serio."
        else:


            $ player_input_valid = True
            $ persistent._jn_player_birthday_day_month = (player_input, player_birthday_month)

    n 3nchsm "¡Oki-doki!{w=0.5}{nw}"
    extend 3ullaj " Así que solo para verificar..."
    show natsuki 1tnmbo
    $ birthday_formatted_es = "{0} de {1}".format(
        spanish_months[persistent._jn_player_birthday_day_month[1]],
        persistent._jn_player_birthday_day_month[0]
    )

    menu:
        n "Tu cumpleaños es el [birthday_formatted_es],{w=0.2} ¿verdad?"
        "Sí, así es":

            if persistent._jn_player_birthday_day_month == (29, 2):

                $ persistent._jn_player_birthday_is_leap_day = True
                n 1fcspu "...Espera.{w=1}{nw}"
                extend 4tnmpueqm " ¿No es ese un día bisiesto también?"
                n 2nllansbl "Cielos..."
                n 2fslposbl "..."
                n 1fcsajsbl "De hecho,{w=0.75}{nw}"
                extend 1unmaj " ¿sabes qué?"
                n 3ullss "Solo...{w=1}{nw}"
                extend 3fcsbgl " voooy{w=0.3} a anotar el 28 también."
                n 4fchgnl "¡Lo siento [player]!{w=0.75}{nw}"
                extend 4fchbllelg " ¡No hay escapatoria de las felicitaciones de cumpleaños para ti!"
            else:

                n 3fchsm "¡Entendido!"

            jump talk_players_birthday_outro
        "No, no es correcto":

            n 4tsqpueqm "¿Huh?{w=1}{nw}"
            extend 2nsqpo " ¿En serio?"
            n 2nsrss "Intentemos...{w=1} eso de nuevo."
            jump talk_players_birthday_input

label talk_players_birthday_outro:
    python:
        import datetime

        today_day_month = (datetime.date.today().day, datetime.date.today().month)
        before_birthday = (
            today_day_month[1] < persistent._jn_player_birthday_day_month[1]
            or (
                today_day_month[1] == persistent._jn_player_birthday_day_month[1]
                and today_day_month[0] < persistent._jn_player_birthday_day_month[0]
            )
        )

    if jnIsPlayerBirthday():

        n 1nchbg "¡Okaaay!{w=0.2} Así que creo que eso es-{w=0.5}{nw}"
        n 4uskemesh "...!{w=1}{nw}"
        n 1uskajl "Oh,{w=1.5}{nw}"
        extend 2kbkwrl " ¡{b}MIERDA{/b}!"
        $ player_initial = jn_utils.getPlayerInitial()
        n 4knmeml "¡[player_initial]-{w=0.3}[player]!{w=0.2} ¡¿Es HOY?!{w=0.5}{nw}"
        extend 2flleml " ¡¿Por qué no {i}dijiste{/i} nada?!"
        n 1nsrunl "Uuuuuu...{w=1}{nw}"
        extend 3kcsemedr " ahora realmente parezco una completa idiota..."
        n 3ncsemesi "...{w=0.5}{nw}"
        n 1fcsem "¡Bien!{w=1}{nw}"
        extend 1fcswr " ¡Entonces solo hay una cosa para ello!{w=1.5}{nw}"


        $ birthday_topic = get_topic("talk_players_birthday_intro")
        $ birthday_topic.shown_count = 1
        $ birthday_topic.last_seen = datetime.datetime.now()


        $ jn_globals.force_quit_enabled = False
        stop music
        play audio switch_flip
        show black zorder JN_BLACK_ZORDER
        $ jnPause(5)
        $ push("holiday_player_birthday")


        $ renpy.jump("call_next_topic")

    elif before_birthday:

        n 3tsqbg "¡Y oye!{w=0.75}{nw}"
        extend 3fwlsm " ¡Parece que todavía tengo algo de tiempo después de todo!"
        n 1fchsmleme "Ehehe."
    else:


        n 4unmem "Espera,{w=0.5} ¿en serio?{w=1}{nw}"
        extend 1knmem " ¿Ya me lo perdí?{w=1.5}{nw}"
        extend 2nsrpo " Aww..."

    n 2nllpo "Bueno...{w=1}{nw}"
    extend 1nllss " gracias de todas formas.{w=1}{nw}"
    extend 3nlrdv " Por compartir,{w=0.2} quiero decir."
    n 2nsrpo "..."
    n 1nsraj "Yo...{w=0.5}{nw}"
    extend 3tnmss " supongo que mejor te devuelvo el favor,{w=0.2} ¿eh?"
    n 4nslcal "Solo promete que no harás que sea todo incómodo."
    n 1ncsemlesi "..."
    n 2nsrssl "Es el 1 de Mayo.{w=1}{nw}"
    extend 2nsqpol " No me hagas decirlo dos veces."

    $ persistent._jn_natsuki_birthday_known = True

    n 1nllpu "Y...{w=1}{nw}"
    extend 4tnmbo " ¿[player]?"
    n 1fsqss "Espero que sepas que mejor te prepares."
    n 3fcsbg "¡Porque voy a ir con todo la próxima vez!{w=1}{nw}"
    extend 1nchgn " Ehehe."

    if Natsuki.isLove(higher=True):
        n 4fchblleaf "¡Te amo,{w=0.2} [player]~!"

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_can_i_see_a_poem",
            unlocked=True,
            prompt="¿Puedo ver un poema que hayas escrito para mí?",
            conditional=(
                "len(jn_poems.JNPoem.filterPoems("
                    "jn_poems.getAllPoems(),"
                    "unlocked=True"
                ")) > 0"
            ),
            category=["Literatura"],
            player_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_can_i_see_a_poem:
    if Natsuki.isEnamored(higher=True):
        n 1fcsbg "¡Duh!{w=0.5}{nw}"
        extend 3nchgnl " ¡Claro que puedes!"
        n 3fsqpol "Estaría ofendida si {i}no{/i} quisieras verlos de nuevo.{w=1}{nw}"
        extend 1fsqsml " Ehehe."
        show natsuki 4klrsml at jn_left

    elif Natsuki.isAffectionate(higher=True):
        n 1unmajl "¿Huh?{w=1}{nw}"
        extend 2fllssl " Oh,{w=0.2} esos."
        n 1fchbgl "¡Seguro!{w=0.5}{nw}"
        extend 3tsqbgl " ¿Simplemente no puedes tener suficiente de mis asombrosas habilidades de escritura,{w=0.2} eh?"
        show natsuki 4flrsml at jn_left
    else:

        n 1unmajl "¿Huh?{w=1}{nw}"
        extend 1nllbo " Oh,{w=0.2} mis poemas."
        n 4unmbo "Seguro,{w=0.2} supongo.{w=1}{nw}"
        extend 2tnmaj " ¿Cuál querías ver de nuevo?"
        show natsuki 4ulrbo at jn_left

    python:
        poem_options = []
        for poem in jn_poems.JNPoem.filterPoems(jn_poems.getAllPoems(), unlocked=True):
            poem_options.append((poem.display_name, poem))

        poem_options.sort(key = lambda option: option[0])

    call screen scrollable_choice_menu(poem_options, ("Olvidalo", None))

    if isinstance(_return, jn_poems.JNPoem):

        show natsuki at jn_center

        if Natsuki.isEnamored(higher=True):
            n 1unmaj "¿[_return.display_name]?{w=0.5}{nw}"
            extend 3nchsmeme " ¡Okaaay!"
            n 3uchsml "Solo un segundo,{w=0.2} [player]..."

            play audio drawer
            with Fade(out_time=0.5, hold_time=0.5, in_time=0.5, color="#000000")

            n 1unmbg "¡Aquí estamos!{w=0.5}{nw}"
            extend 1nchsml " Ehehe."

            call show_poem (_return)

            n 2tnmsml "¿Todo listo?{w=0.5}{nw}"
            extend 2nlrssl " Solo pondré eso de vuelta."
            show natsuki 4nsrsml

        elif Natsuki.isAffectionate(higher=True):
            n 1unmaj "¿[_return.display_name]?{w=0.2} ¿Ese?{w=0.5}{nw}"
            extend 1fchbg " ¡Entendido!"
            n 3fchsml "Solo dame un segundo aquí..."

            play audio drawer
            with Fade(out_time=0.5, hold_time=0.5, in_time=0.5, color="#000000")

            n 1fchbgl "¡Lo encontré!"

            call show_poem (_return)

            n 2tnmssl "¿Todo listo?{w=0.75}{nw}"
            extend 2flrdvl " Ehehe."
            show natsuki 2fsrdvl
        else:

            n 1unmaj "¿Ese?{w=0.5}{nw}"
            extend 1nnmss " Muy bien."
            n 4nllss "Solo déjame sacarlo..."

            play audio drawer
            with Fade(out_time=0.5, hold_time=0.5, in_time=0.5, color="#000000")

            n 1ullaj "Bueno,{w=0.5}{nw}"
            extend 4nlrbol " aquí tienes."

            call show_poem (_return)

            n 2tnmbol "¿Todo listo?{w=0.5}{nw}"
            extend 2nslssl "Solo pondré eso de vuelta."
            show natsuki 4nslbol

        play audio drawer
        with Fade(out_time=0.5, hold_time=0.5, in_time=0.5, color="#000000")
    else:


        show natsuki at jn_center
        n 1nnmbo "Oh.{w=1}{nw}"

        if Natsuki.isAffectionate(higher=True) and random.randint(0, 10) == 1:
            extend 3nlrpol " Bueno,{w=0.2} está bien entonces.{w=1}{nw}"
            extend 3fsqbll " Aguafiestas.{w=0.75}{nw}"
        else:

            extend 3nlrpol " Bueno,{w=0.2} está bien entonces."

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_chocolate_preference",
            unlocked=True,
            prompt="¿Qué tipo de chocolate prefieres?",
            category=["Comida"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_chocolate_preference:
    if Natsuki.isAffectionate(higher=True):
        if get_topic("talk_chocolate_preference").shown_count > 0:
            n 2tnmaj "¿Oh?{w=0.5}{nw}"
            extend 2tsqbo " ¿Esto de nuevo,{w=0.2} eh?"
            n 4tsrsm "..."
        else:

            n 1unmaj "¡Ooh!{w=0.75}{nw}"
            extend 2tsqbg " ¿Mi tipo de chocolate favorito,{w=0.2} dices?"

        n 1nslss "...¿Por qué,{w=0.5}{nw}"
        extend 4fsqsm " [player]?"
        n 3fcsbglsbl "N-{w=0.2}no estás tratando de {i}endulzarme{/i} o algo,{w=0.2} ¿verdad?{w=0.75}{nw}"
        extend 3fsldvlsbl " Ehehe..."
        n 1fslbolsbl "..."
        n 3fcsbglsbl "B-{w=0.2}bueno,{w=0.2} ¡como sea!"

    elif Natsuki.isNormal(higher=True):
        if get_topic("talk_chocolate_preference").shown_count > 0:
            n 4tnmboeqm "¿Huh?{w=1}{nw}"
            extend 2tslpueqm " ¿No me preguntaste esto ya,{w=0.2} [player]?"
            n 1ullaj "Bueno,{w=0.75}{nw}"
            extend 1unmbo " no diría que he cambiado de opinión..."
        else:

            n 4unmboeqm "¿Eh?{w=0.75}{nw}"
            extend 2tllbo " Mi tipo de chocolate favorito,{w=0.5}{nw}"
            extend 2tnmss " ¿eh?"
            n 2uupaj "Esa es...{w=1}{nw}"
            extend 4flrbo " una bastante difícil en realidad,{w=0.75}{nw}"
            extend 1tnmbo " para ser honesta."
            n 1ullaj "Digo..."

    elif Natsuki.isDistressed(higher=True):
        n 3fcsansbl "Oh,{w=1}{nw}"
        extend 3fsremsbl " {i}por favor{/i}."

        if get_topic("talk_chocolate_preference").shown_count > 0:
            n 2fcsemsbl "¿En serio,{w=0.2} [player]?{w=1}{nw}"
            extend 2fsqemsbl " ¿{i}Esto{/i} otra vez?"
        else:

            n 2fsqslsbl "¿En serio,{w=0.2} [player]?"

        n 1fcssl "..."
        n 3fcsemesi "...Bien.{w=0.75}{nw}"
        extend 3fslbo " Por lo que siquiera te {i}importa{/i}."
        n 1fllem "Chocolate blanco,{w=0.2} probablemente."
        n 4tsqem "...¿Por qué?{w=1}{nw}"
        extend 2fcsem " Es barato,{w=0.5} lleno de azúcares y grasas,{w=0.75}{nw}"
        extend 2fcssr " y siempre podría añadirlo a lo que quisiera."
        n 1fsqfr "¿Qué?{w=1}{nw}"
        extend 1fsqaj " No actúes como si {i}en serio{/i} esperaras algo diferente.{w=0.75}{nw}"
        n 2fsran "Como si {i}yo{/i} fuera la que va a tiendas de dulces {i}lujosas{/i} para escoger lo que se me antojara."
        n 2fsqun "..."
        n 1fslun "Sí.{w=1}{nw}"
        extend 1fcsfr " No como si pensara que {i}tú{/i} lo entenderías."
        n 2fcsbo "Lo que sea."
        n 1flrpu "Los otros están bien también,{w=0.75}{nw}"
        extend 4fsrfr " supongo."
        n 1fllsl "El chocolate con leche es simplemente algo aburrido.{w=1}{nw}"
        extend 2fslan " Y no hya {i}forma{/i} de que pudiera conseguir chocolate amargo con {i}mi{/i} tipo de presupuesto."
        n 1fcsboesi "..."
        n 2fslaj "Así que...{w=1}{nw}"
        extend 2fslsl " sí.{w=0.75}{nw}"
        extend 2fsrbo " Eso lo resume."
        n 1fsqbo "..."
        n 1fnmfr "Ahí.{w=0.3} ¿Feliz ahora?"
        n 2tsqem "¿Porque a menos que mágicamente tengas algo para endulzar {i}esta{/i} experiencia?"
        n 1fcssr "Je."
        n 2fsqan "Creo que hemos terminado aquí,{w=0.2} {i}[player]{/i}."

        return
    else:

        n 1fcsan "Je.{w=0.75}{nw}"
        extend 1fsqanltsb " ¿Mi tipo favorito de chocolate?"

        if get_topic("event_warm_package").shown_count > 0:
            n 2fsqupltsb "¿Tu memoria {i}en serio{/i} apesta tanto como tu personalidad?"
            n 1fcsunltsa "..."
            n 1fsqfrltsb "Permíteme {i}recordártelo{/i},{w=0.2} {i}[player]{/i}."
        else:

            n 2fsqupltsb "¿{i}Realmente{/i} quieres saber,{w=0.2} [player]?"
            n 1fcsunltsa "..."

        n 1fcsupltsa "No cualquier basura barata,{w=0.75}{nw}"
        extend 2fnmanltsc " medio-{w=0.2}expirada{w=0.75}{nw}"
        extend 2fsqwrltsb " basura{w=0.75}{nw}"
        extend 1fnmfultsc " que {i}tú{/i} me darías,{w=1}{nw}"
        extend 1fcsfultsa " eso es seguro."
        n 2fsqanltsb "Imbécil."

        return

    n 1fcstr "{i}Tiene{/i} que ser chocolate blanco.{w=0.75}{nw}"
    extend 3fchbg " ¡Cualquier día de la semana!"
    n 4nslcssbr "{i}Está{/i} practicamente desbordándose de azúcar...{w=0.75}{nw}"
    extend 4nsrdvsbr " y debatiblemente siquiera {i}chocolate{/i}..."

    if get_topic("event_warm_package").shown_count > 0:
        n 4uspajl "¡Pero ese {i}sabor{/i}!{w=0.75}{nw}"
        extend 1uchtsleme " ¡Especialmente en chocolate caliente!"
    else:

        n 1uspajl "¡Pero ese {i}sabor{/i}!"

    n 1kcsssl "Tan cremoso y ligero,{w=1}{nw}"
    extend 3kcstsl " con solo ese toque de vainilla...{w=1}{nw}"
    extend 3fchbgl " ¡Lo amo!"
    n 4unmajesu "¡Oh!{w=0.75}{nw}"
    extend 1fchbg " ¡E incluso es súper conveniente para hornear!"
    n 1ullss "Es bastante barato -{w=0.5}{nw}"
    extend 2nsrsssbl " ya que realmente no tiene mucho cacao {i}real{/i} en absoluto -{w=0.5}{nw}"
    extend 2ulrss " Nunca tengo que preocuparme de qué tan fuerte es,{w=0.75}{nw}"
    extend 2fchsm " ¡además va súper bien con chocolate normal también!"
    n 1fchbl "¡Hablando de multiusos!"
    n 4tsqss "¿Compraste un poco como un premio y no puedes terminar el trabajo?{w=0.75}{nw}"
    extend 1fchsmeme " ¡No problemo!"
    n 1ullss "Solo envuélvelo de nuevo,{w=0.2} guárdalo,{w=0.75}{nw}"
    extend 3fwlbg " ¡y esa es tu próxima cubierta de pastel resuelta!"
    n 3fcsss "Así que tómalo de mí,{w=0.2} [player]:{w=1}{nw}"
    extend 3uchgn " ¡es el mejor amigo de un repostero!"
    n 1fcssm "..."
    n 4unmajesu "...¡Ah!{w=1}{nw}"
    n 4fllbglsbr "E-{w=0.2}eso no quiere decir que los otros sean terribles,{w=0.2} o algo así.{w=0.75}{nw}"
    extend 2unmajsbr " ¡El chocolate es súper subjetivo!{w=1}{nw}"
    extend 2nsrsssbr " Pero..."
    n 1tnmbo "Supongo que simplemente no veo el atractivo {i}tanto{/i}."
    n 4nslss "El chocolate con leche está {i}bien{/i},{w=0.2} pero como que lo ves en todas partes."
    n 2fllpu "En cuanto al chocolate amargo..."
    n 2nsrunsbl "..."
    n 2fcsbglsbr "B-{w=0.2}bueno,{w=1}{nw}"
    extend 4flrsslsbr " ¡totalmente tiene su lugar también!"
    n 1unmaj "A veces,{w=0.2} ¡ese toque de amargura es justo lo que necesitas!{w=0.75}{nw}"
    extend 1ullbo " Además con todos los antioxidantes y generalmente la menor cantidad de azúcar..."
    n 2tnmsssbl "A-{w=0.2}¿al menos para chocolate?{w=1}{nw}"
    extend 2kchbgsbl " ¡Supongo que no se pone mucho más saludable que eso!"
    n 1fcsbg "¡Así que sí!{w=0.75}{nw}"
    extend 4fllbgsbr " {i}Totalmente{/i} tiene su lugar,{w=0.2} como dije..."
    n 2fslposbr "...Simplemente no en {i}mi{/i} boca.{w=0.75}{nw}"
    extend 2fchsmsbr " ¡Es todo lo que digo!"

    if (
        not jn_outfits.getOutfit("jn_chocolate_plaid_collection").unlocked
        and Natsuki.isAffectionate(higher=True)
        and persistent.jn_custom_outfits_unlocked
    ):

        n 2nslss "Hombre...{w=1}{nw}"
        extend 1ncsfs " toda esta charla de dulces está trayendo de vuelta todo tipo de recuerdos."
        n 2tllaj "De hecho..."
        n 4tnmss "Estoy {i}segura{/i} de que tenía algún tipo de lindo vestido con temática de chocolate en algún momento.{w=0.75}{nw}"
        extend 2nchgn " O al menos se sentía de esa forma con todos los colores."
        n 2ksrfssbl "...Y Sayori prácticamente babeando sobre él."
        n 2kchsm "Tal vez debería ir a buscar eso más tarde..."

        $ jn_outfits.getOutfit("jn_chocolate_plaid_collection").unlock()
        $ jn_outfits.getWearable("jn_necklace_tight_golden_necklace").unlock()

    n 1fllajlsbr "¡C-{w=0.2}como sea!{w=0.75}{nw}"
    extend 1fcsajl " Suficiente de mí parloteando de nuevo.{w=0.75}{nw}"
    extend 2tlrsssbl " Cielos."
    n 1unmaj "¿Qué hay de ti,{w=0.2} [player]?{w=0.75}{nw}"
    n 1fbkwreex "...¡Espera!{w=1}{nw}"
    extend 1fcsbg " ¡No me digas!"
    n 4fcssresp "..."


    if Natsuki.isLove(higher=True):
        n 3fcsgs "{i}Tiene{/i} que ser chocolate blanco.{w=0.75}{nw}"
        extend 3fchbl " Completamente obvio.{w=1}{nw}"
        extend 4fcsss " Además..."
        n 4fsldvlsbl "M-{w=0.2}me gusta pensar que {i}conozco{/i} a un dulzura cuando veo a uno."
        n 2fchsmlsbl "Ehehe..."
        n 2fchblfsbl "¡T-{w=0.2}te amo,{w=0.2} [player]~!"

    elif Natsuki.isEnamored(higher=True):
        n 1fcsbg "...{i}Tiene{/i} que ser chocolate blanco.{w=1}{nw}"
        extend 4fcssm " Además..."
        n 2fllssless "¿C-{w=0.2}cómo más sería nuestro tiempo juntos así de dulce?"
        n 2fchsmless "Ehehe..."

    elif Natsuki.isAffectionate(higher=True):
        n 1uupaj "...Probablemente chocolate con leche,{w=0.75}{nw}"
        extend 3tsqsm " diría yo."
        n 3fchgn "...¡Te has vuelto así de blando,{w=0.2} después de todo!"
    else:

        n 1fcspu "Es...{w=1}{nw}"
        extend 2tnmpu " en realidad algo difícil de adivinar,{w=0.75}{nw}"
        extend 2tllsl " para ser honesta."
        n 1tnmss "{i}Diría{/i} chocolate amargo,{w=0.5}{nw}"
        extend 4tsqss " pero..."
        n 3fchgnl "¡Me gusta pensar que no eres {i}tan{/i} amargo!{w=0.75}{nw}"
        extend 3nchgn " Ahaha."

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_learning_languages",
            unlocked=True,
            prompt="Aprendiendo idiomas",
            category=["Sociedad"],
            nat_says=True,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_learning_languages:
    $ already_discussed_learning_languages = get_topic("talk_learning_languages").shown_count > 0
    if already_discussed_learning_languages:
        n 1ncsemesi "..."
        n 1nsrem "Hombre...{w=1}{nw}"
        extend 2fcspo " Aún no puedo creer que arruiné mi alemán {i}así{/i} de mal la última vez.{w=0.75}{nw}"
        extend 2kslan " Cielos."
        n 1tnmaj "Pero como sea,{w=0.2} es como dije antes.{w=0.5}{nw}"
        extend 4kbkwr " ¡Aprender un nuevo idioma es {i}súper{/i} complicado!"
    else:

        n 1nllpu "..."
        n 2fllsm "..."
        n 4fsqsm "..."
        n 1fcsss "Je."
        n 2fcsaj "¡Ahem!"
        n 1fcssm "..."


        n 3uchgn "Moin moin,{w=0.2} [player]!{w=0.75}{nw}"
        extend 1usqsm " Was liegt an?{w=0.5}{nw}"
        extend 1fchss " Ehehe."
        n 3fcsbs "Ich wette du wusstest nicht, dass ich nicht {i}nur{/i} Englisch tue,{w=0.2} ¿eh?"
        n 1tsqbg "Du solltest auch versuchen mehr Sprachen...{w=0.5} f-{w=0.2}fluessig..."
        n 2fsrbglsbl "f-{w=0.2}fliessend...?"
        n 1fsrunlesdsbr "..."
        n 2tsremlesssbr "zu reden...?{w=0.5}{nw}"
        extend 2fcsbglesssbr " Sprachfluss!"
        n 4flrbglsbr "O-oder wie man auch sagt -{w=0.3}{nw}"
        extend 1fcsbglsbl " wer rasst..."
        n 2fllunlesssbl "r-{w=0.2}rastet...!{w=0.5}{nw}"
        extend 2klremfesssbl " Hat Rosen...?{w=0.75}{nw}"
        extend 2kllemfesssbl " Mit Rost!"

        n 1fcsunfesssbr "..."
        n 2fcsanfesssbr "¡Nnnnnn-!"
        n 1fcsemlesssbr "Oh,{w=0.75}{nw}"
        extend 4fbkwrlesssbr " {i}olvídalo{/i}!{w=0.75}{nw}"
        extend 2kslpul " Esto es tan vergonzoso..."
        n 1fslunl "..."

        n 4uskemlesh "...!{w=0.5}{nw}"
        n 2fcswrl "¡N-{w=0.3}no es como si no pudiera hacerlo!{w=0.75}{nw}"
        extend 2flleml " {i}totalmente{/i} puedo hacerlo excelente sola."
        n 1fcseml "Simplemente...{w=0.5}{nw}"
        extend 4fsrpol " estoy siendo desanimada.{w=0.5}{nw}"
        extend 4fsqpol " Teniendo una {i}audiencia{/i},{w=0.2} y eso."
        n 1fnmpu "Pero en serio,{w=0.2} [player].{w=0.75}{nw}"
        extend 3tnmaj " ¿Alguna vez has {i}intentado{/i} aprender otro idioma?"
        n 1fbkwr "¡Es súper difícil!{w=1}{nw}"
        extend 2fslpo " ¡No sé cómo la gente lo hace!"

    n 1tslpu "Como..."
    n 1unmaj "Tuvimos clases de idiomas en la escuela -{w=0.5}{nw}"
    extend 2nslss " obviamente -{w=0.75}{nw}"
    extend 2fnmpu " ¡pero nunca hubo tiempo suficiente para realmente {i}practicar{/i}!"
    n 1fllem "Nos emparejaban e íbamos a practicar pronunciaciones y tal."
    n 4unmem "Pero cuando ninguno de los dos realmente {i}conoce{/i} el idioma,{w=0.5}{nw}"
    extend 2fcswr " ¿cómo se supone que sepas cuando alguien está haciendo algo mal?"
    n 1fllaj "Luego con todos los otros estudios volando alrededor,{w=0.5}{nw}"
    extend 3fsrsr " no es como si tuviéramos tiempo libre para intentarlo fuera de la escuela tampoco."
    n 3tsqpu "Además,{w=0.2} con qué tan complejas todas las reglas son y cuánta repetición necesitas,{w=0.5}{nw}"
    extend 3fcsem " ¡una o dos clases a la semana simplemente no es suficiente!"
    n 1fllpu "Como,{w=0.75}{nw}"
    extend 4fnmem " ¿cómo se supone que alguien recuerde si alguna cosa doméstica aleatoria tiene un nombre masculino o femenino?"
    n 3flrwr "¡¿O cómo pronunciar algún espagueti de palabras aleatorias que parece que alguien se inventó completo?!"
    n 1kcsemesi "Ugh..."
    n 1ucspu "Digo...{w=0.75}{nw}"
    extend 1unmpu " ¡no me malinterpretes!{w=0.5}{nw}"
    extend 3fcssl " ¡No es como si {i}no{/i} me gustara aprender un nuevo idioma!"
    n 3nsrss "Y al {i}menos{/i} pudimos elegir qué idioma queríamos aprender."
    n 3nsqpo "Solo desearía que pudiéramos realmente,{w=0.2} bueno..."
    n 3kslpo "{i}Aprenderlos{/i},{w=0.2} ¿sabes?"
    n 1fcsss "Je.{w=0.5}{nw}"
    extend 4fslsr " No es como si algo de eso hubiera detenido a {i}Monika{/i},{w=0.2} claro."
    n 1nslpu "Aunque...{w=0.75}{nw}"
    n 2fnmsll "Todavía como que siento que me robaron experiencias de esa forma."
    n 1fllss "¡Es fácil olvidar que hay un mundo entero allá afuera cuando solo interactúas con una cierta parte de él que habla un idioma!"

    if get_topic("talk_flying").shown_count > 0:
        n 2tllaj "Creo que mencioné antes que nunca he volado a ningún lado.{w=0.5}{nw}"
        extend 2tnmpu " ¿Pero si lo hiciera?"
        n 1fcsss "Me gustaría al menos intentar aprender un poco del idioma de a dónde voy."
        n 1fnmpu "¡Piénsalo!{w=0.75}{nw}"
        extend 1fcsbg " Si ya estás poniendo todo ese dinero y esfuerzo para arreglar todo..."
        n 3tsqsmesm "¿Qué es un poco extra para mostrar algo de respeto,{w=0.2} cierto?"
    else:

        n 2tsqss "¿Y con cuánto más desbloqueas cuando sabes cómo hablar los idiomas ahí?"
        n 1fsqsr "Llegarías a ser un verdadero tonto para no al {i}menos{/i} pensar en ello.{w=0.5}{nw}"
        extend 4fsqsm " Ehehe."

    n 1ullaj "Pero...{w=0.75}{nw}"
    extend 2nnmbo " soy solo yo,{w=0.2} supongo."
    n 2tnmss "Aunque, ¿qué hay de ti,{w=0.2} [player]?"
    $ menu_opening = "¿Algo nuevo en el departamento de idiomas?" if already_discussed_learning_languages else "¿Conoces otros idiomas?"

    menu:
        n "[menu_opening]"
        "Conozco otro idioma":

            if persistent._jn_player_is_multilingual:
                n 4uskemlesh "¿H-{w=0.3}huh?{w=0.75}{nw}"
                extend 2fnmeml " ¡Pero ya dijiste que conocías otro idioma!"
                n 2fsqsfl "...¡¿Y me estás diciendo que fuiste y aprendiste otro?!"
                n 1fsrbol "Wow,{w=0.2} [player]..."
                n 3tsqss "...Realmente eres un presumido,{w=0.2} ¿eh?{w=0.5}{nw}"
                extend 4fsqsm " Ehehe."
            else:

                n 1tsqcs "¿Oho?{w=0.75}{nw}"
                extend 3fsqbg " Bueno,{w=0.2} ¡mírate!{w=0.5}{nw}"
                extend 3fsqss " Mejor no te pongas muy engreído ahora,{w=0.2} [player]..."
                n 1usqsm "No eres el {i}único{/i} multilingüe aquí,{w=0.2} después de todo.{w=0.5}{nw}"
                extend 4fsqsm " Ehehe."
                $ persistent._jn_player_is_multilingual = True
        "Conozco múltiples otros idiomas":

            if persistent._jn_player_is_multilingual:
                n 1fllem "Oh,{w=0.5}{nw}"
                extend 2fcswr " ¡vamos!{w=0.75}{nw}"
                extend 2fsqem " ¿En serio?"
                n 1fslem "Eres {i}tal{/i} presumido,{w=0.2} [player]."
                n 4fsqsm "...Ehehe."
            else:

                n 1fsqsr "..."
                n 2fsrpo "...Presu-{w=0.2}mido.{w=0.5}{nw}"
                extend 4fsqsm " Ehehe."
                $ persistent._jn_player_is_multilingual = True
        "Estoy tratando de aprender otro idioma":

            if persistent._jn_player_is_multilingual:
                n 1unmaj "¿Oh?{w=0.75}{nw}"
                extend 1flrbg " Bueno,{w=0.2} ¡hey!"
                n 3fsqss "Eso hace a ambos ahora,{w=0.2} ¿eh?{w=0.5}{nw}"
                extend 4fsqsm " Ehehe."
            else:

                n 4fnmbgesu "¡Aha!{w=0.5}{nw}"
                extend 3tsqbg " Así que estás familiarizado con la lucha también,{w=0.2} ¿eh?"
                n 1fsqsm "Ehehe."
                $ persistent._jn_player_is_multilingual = False
        "No conozco otros idiomas":

            if persistent._jn_player_is_multilingual:
                n 1tsqaj "...¿Huh?"
                n 4uskemlesh "¡E-{w=0.2}espera un segundo!{w=0.5}{nw}"
                extend 2fsqem " ¡Ya {i}dijiste{/i} que conocías otro idioma!"
                n 2fslpol "No nací {i}ayer{/i},{w=0.2} idiota..."
            else:

                n 1unmem "...¿Huh?{w=0.5} ¿En serio?{w=0.5}{nw}"
                extend 2knmpo " ¿Ni siquiera un poco?"
                n 1ncspuesi "Hombre..."
                n 1nllpu "Tengo que admitir,{w=0.5}{nw}"
                extend 4nsqbo " eso es algo decepcionante."
                n 1fsqbg "...Nada te detiene de empezar sin embargo,{w=0.2} ¿verdad?{w=0.5}{nw}"
                extend 2fsqsm " Ehehe."
                $ persistent._jn_player_is_multilingual = False

    n 1ullaj "Bueno,{w=0.2} como sea.{w=1}{nw}"
    extend 2tnmss " Creo que ya he hablado demasiado a este punto,{w=0.2} ¿eh?"
    n 2tlrss "Y,{w=0.2} bueno...{w=0.75}{nw}"
    extend 4fsqbg " como dicen en {i}Deutschland{/i}..."
    n 1ncsss "Alles hat ein Ende,{w=0.5}{nw}"
    extend 3uchgnlelg " nur die Wurst hat zwei!"

    return



init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_rage_rooms",
            unlocked=True,
            prompt="Habitaciones de ira",
            category=["Entretenimiento", "Pasatiempos"],
            nat_says=True,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_rage_rooms:
    $ already_discussed_rage_rooms = get_topic("talk_rage_rooms").shown_count > 0

    if already_discussed_rage_rooms:
        n 2fslss "Hombre..."
        n 2ullaj "Sabes,{w=0.5}{nw}"
        extend 2tnmbo " [player]..."
        n 1fcssm "Aún no puedo quitarme de la mente las habitaciones de ira."
        n 1ulraj "Sé que hablamos de ellas antes,{w=0.2} pero..."
        n 3nsrss "Bueno,{w=0.75}{nw}"
        extend 3tnmpu " ¿puedes culparme?"
    else:

        n 1ullaj "Hey,{w=0.2} [player]..."
        n 1ulrbo "Esto es un poco aleatorio,{w=0.5}{nw}"
        extend 4ulraj " pero..."
        n 2tnmpu "¿Alguna vez has estado en una habitación de ira antes?"
        n 2nslsssbr "Nunca he {i}estado{/i} en una yo misma en realidad,{w=0.75}{nw}"
        extend 1ncsaj " pero oh.{w=0.5}{nw}"
        extend 1fcsaj " Mi.{w=0.5}{nw}"
        extend 1fcsaw " Dios.{w=0.5}{nw}"
        extend 2nsqsr " [player]."

    n 1fcspu "Ellas...{w=0.75}{nw}"
    extend 1fcsaj " se ven...{w=0.75}{nw}"
    extend 4fspgsedz " ¡{i}asombrosas{/i}!"
    n 4uwdaj "¡No,{w=0.2} de verdad!{w=0.75}{nw}"
    extend 2fcspo " ¡Hablo en serio!"
    n 1ullss "Básicamente tienes una habitación entera llena de viejas cosas inútiles:{w=0.5}{nw}"
    extend 1ulrbo " muebles no deseados,{w=0.2} decoraciones,{w=0.2} viejo hardware de computadora...{w=0.75}{nw}"
    extend 1nnmbo " así como un montón de herramientas y equipamiento de seguridad."
    n 1nllpu "Ya sabes.{w=0.75}{nw}"
    extend 2ullaj " Gafas,{w=0.2} martillos,{w=0.5}{nw}"
    extend 2nllsm " ese tipo de cosas."
    n 2tsqsm "¿Y entonces...?"
    n 1fcssm "Ehehe."
    n 3fchbg "¡Vamos,{w=0.2} [player]!{w=0.75}{nw}"
    extend 3fsqbg " ¿Para qué {i}más{/i} crees que es todo eso?"
    n 3uchgnelg "...¡Llegas a sacarle absolutamente la {i}MIERDA{/i} a todo!"
    n 1unmbs "¡En serio!{w=0.75}{nw}"
    extend 1fchbs " ¡Simplemente te vuelves loco!"
    n 2tsqbg "...¿Y la mejor parte?{w=1}{nw}"
    extend 1fchbg " ¡No tienes que limpiar después tampoco!{w=0.75}{nw}"
    extend 4fspgs " ¡Incluso puedes llevar gente {i}con{/i}tigo!"
    n 1fcsss "Hombre...{w=0.75}{nw}"
    extend 3fchgn " ¡imagina a {i}Yuri{/i} probando algo como eso!"
    n 3nsrdvsbl "Y Sayori..."
    n 4uwdbosbl "...¡No quedaría habitación {i}sobrando{/i}!"
    n 1ullss "Claro,{w=0.5}{nw}"
    extend 1ullbo " ellas ya te dan un montón de sus propias cosas que puedes destrozar...{w=0.75}"
    n 1fchsm "¡Pero puedes totalmente traer tus propias cosas también!{w=0.75}{nw}"
    extend 3nsrsmsbr " Bueno..."
    n 1nlrbo "Mientras sea todo seguro de romper -{w=0.5}{nw}"
    extend 2nsrsssbl " nada de baterías grandes,{w=0.2} cosas presurizadas,{w=0.2} o algo tonto como eso."
    n 1fsqsm "¿Finalmente tuviste suficiente de esa impresora basura masticando todas tus tareas?"
    n 1fcsbg "¡Nada como un juicio por combate para mostrar quién manda!"
    n 4unmajesu "¡Oh!{w=0.5}{nw}"
    extend 1nnmbo " Pero no me malinterpretes."
    n 3nsrbgsbl "Todavía tienes que pagar sin importar si trajiste tu propia basura,{w=0.75}{nw}"
    extend 3nsrposbl " claro...{w=1}{nw}"
    extend 3kslslsbl " y realmente {i}no{/i} es una forma de lidiar con problemas de ira ni nada de eso."
    n 1fcssm "Pero tengo que decir,{w=0.2} [player]."
    n 4fsqbg "Si eso no suena como una forma {w=0.2}{i}aplasteante{/i}{w=0.2} de aliviar el estrés..."
    n 2uchgn "¡Entonces no sé qué lo es!{w=0.5}{nw}"
    extend 1fchsmeme " Ehehe."

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_take_down_deco",
            unlocked=True,
            prompt="¿Puedes quitar las decoraciones por mí?",
            conditional="len(store.persistent._jn_holiday_deco_list_on_quit) > 0",
            category=["Días festivos"],
            player_says=True,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_take_down_deco:
    n 2tllpu "¿Simplemente no sintiendo las celebraciones hoy,{w=0.75}{nw}"
    extend 2tnmsl " [player]?"

    if len(jn_events.getHolidaysForDate()) == 0:
        n 2nslsssbl "Supongo que {i}han{/i} como que extendido su bienvenida..."
        n 2nslposbl "..."
    else:

        n 1ncsemesi "...{w=1}{nw}"

    n 1ulraj "Sí,{w=0.5}{nw}"
    extend 1nlrbo " puedo hacer eso.{w=0.75}{nw}"
    extend 3nsrpo " Supongo.{w=1}{nw}"
    extend 3fsqca " Pero tú estás limpiando todo eso la próxima vez."
    n 1nllsl "Solo dame un segundo aquí...{w=1}{nw}"
    show natsuki 1ncssl

    show black zorder 4 with Dissolve(0.5)
    $ jnPause(1)
    play audio chair_out
    $ jnPause(3)
    hide deco
    $ persistent._jn_holiday_deco_list_on_quit = []
    play audio clothing_ruffle
    $ jnPause(2)
    play audio drawer
    $ jnPause(3)
    play audio chair_in
    $ jnPause(1)
    show natsuki 1nlrbo at jn_center
    hide black with Dissolve(1.25)

    n 1ulraj "¡Y creo que eso es todo!"

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_thoughts_on_vegetarianism",
            unlocked=True,
            prompt="¿Qué piensas sobre el vegetarianismo?",
            conditional="jn_utils.get_total_gameplay_hours() >= 4",
            category=["Comida", "Sociedad"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_thoughts_on_vegetarianism:
    $ already_discussed_vegetarianism = get_topic("talk_thoughts_on_vegetarianism").shown_count > 0

    if Natsuki.isNormal(higher=True):
        if already_discussed_vegetarianism:
            n 2tnmpu "¿Huh?{w=0.5}{nw}"
            extend 2tnmsl " ¿Vegetarianismo?"
            n 1fcspu "...Espera."
            n 2tllboeqm "¿No hablamos de esto antes?"
            n 2tslbo "..."
        else:

            n 1tnmpu "¿Eh?{w=0.5}{nw}"
            extend 2tnmsleqm " ¿Vegetarianismo?"
            n 1tllaj "Esa...{w=0.75}{nw}"
            extend 1ullss " definitivamente no es una pregunta que esperaba,{w=0.75}{nw}"
            extend 4tnmbo " tengo que decir."
            n 1ulrpu "Pero...{w=0.75}{nw}"
            extend 2tsqss " ¿por qué preguntas,{w=0.2} [player]?"
            n 2fsqsm "¿Buscando cambiar de aires,{w=0.2} eh?{w=0.75}{nw}"
            extend 1fchsm " Ehehe."

        n 1ullss "Bueno,{w=0.2} como sea.{w=0.75}{nw}"
        extend 4tnmbo " ¿Con toda seriedad?"
        n 1ulraj "Nunca he pensado mucho en eso,{w=0.5}{nw}"
        extend 2ulrbo " para ser honesta."
        n 2nsrss "Teníamos opciones vegetarianas y veganas en la escuela,{w=0.75}{nw}"
        extend 2tnmbo " pero nunca sentí un impulso particular para probarlas ni nada."
        n 4nslsssbr "Y no es como si realmente pueda probarlas {i}ahora{/i},{w=0.2} tampoco."
        n 1unmeml "¡P-{w=0.2}pero eso no quiere decir que se vieran {i}mal{/i} ni nada!"
        n 2fsldv "Al menos no para mí."
        n 1fllss "Diablos,{w=0.75}{nw}"
        extend 3fchgn " ¡Monika se tragaba esa cosa como si no hubiera un mañana!"
        n 1ulraj "Aunque...{w=1}{nw}"
        extend 3fcscaedz " ¡Sí creo que es súper admirable cómo la gente puede dejar la carne a un lado por tantas razones!{w=1}{nw}"
        extend 4uwdaj " ¡En serio!"
        n 1ullaj "Digo,{w=0.75}{nw}"
        extend 1nllsl " es una cosa dejar de comer un tipo particular de carne.{w=0.75}{nw}"
        extend 2fcsss " Cualquiera puede hacer eso."
        n 1tnmpu "Pero dejar {i}todo{/i},{w=0.75}{nw}"
        extend 4unmem " o incluso rechazar {i}cualquier{/i} producto animal en absoluto?"
        n 3fcsbg "¡Ahora {i}eso{/i} toma agallas!{w=1.25}{nw}"
        extend 3fsldvsbl " ...Sin juego de palabras."
        n 1ullaj "Claro,{w=0.5}{nw}"
        extend 2tllsl " tal vez a algunas personas simplemente no les gusta el sabor.{w=0.75}{nw}"
        extend 2tnmbo " Totalmente entiendo eso.{w=1}{nw}"
        extend 1fnmaj " Pero hay un montón de razones por las que la gente lo hace -{w=0.5}{nw}"
        extend 1fcsbg " ¡y todas son igual de válidas!"
        n 3ulraj "Preocupaciones ambientales,{w=0.5}{nw}"
        extend 3nslun " bienestar animal...{w=0.75}{nw}"
        extend 3kchbgsbr " ¡incluso solo para ahorrar dinero!"
        n 4tsqsssbr "Loco pensar cómo una sola elección de estilo de vida puede venir de tantos lugares,{w=0.2} ¿eh?"
        n 1unmajesu "Oh -{w=0.5}{nw}"
        extend 2fllbgsbl " no te preocupes,{w=0.2} [player].{w=0.75}{nw}"
        extend 2nslpo " No me voy a poner a sermonear sobre eso ni nada de eso."
        n 1unmca "{i}Es{/i} solo una elección como cualquier otra,{w=0.75}{nw}"
        extend 1nlrss " después de todo.{w=0.75}{nw}"
        extend 2nsrsssbl " Y una personal también."
        n 4fwlbg "...¡Como si eso fuera a detenerme de sugerirlo sin embargo!"
        n 2fsldv "Incluso si {i}yo{/i} no puedo probarlo yo misma ahora mismo..."
        n 1fsqsm "¡No hay excusa para ti!{w=1}{nw}"
        extend 1fcsbg " Lo siento,{w=0.2} [player]."
        n 3uchgn "¡Me temo que no te librarás de esta!"
        n 1fcsbg "¡Así que!"
        n 1ulraj "No sé si ya estás practicando una dieta libre de animales,{w=0.75}{nw}"
        extend 4fsqss " pero si no lo estás..."
        n 1fchbg "¿Por qué no darle una oportunidad,{w=0.2} [player]?"
        n 1ullss "No necesitas ir con todo ni nada -{w=0.5}{nw}"
        extend 3fchsm " ¡podrías cambiar solo una comida al día y ver cómo te sientes!"
        n 4tlrss "Además con todas las recetas allá afuera,{w=0.75}{nw}"
        extend 4tsqbg " ¡el trabajo duro está prácticamente ya hecho para ti!{w=0.75}{nw}"
        extend 3fchsmeme " ¡Pan comido!"
        n 3tnmsm "Y como sea,{w=0.75}{nw}"
        extend 1tllaj " incluso si es solo por un día o dos,{w=0.2} y no funciona:{w=0.5}{nw}"
        extend 4tsqsm " al menos puedes decir que lo {i}intentaste{/i},{w=0.2} ¿verdad?"
        n 4tslsm "Bueno,{w=0.2} en cualquier caso -{w=0.5}{nw}"
        extend 1nslss " me he extendido lo suficiente,{w=0.75}{nw}"
        extend 1fcsss " así que creo que eso es todo lo que tengo que decir sobre ese tema."
        n 1fsqss "Además,{w=0.2} [player]..."
        n 3fsqbg "No querría convertirte en un {i}vegetal{/i} ahora,{w=0.75}{nw}"
        extend 3tsqcs " ¿o sí?"
        n 3nchgnelg "Ehehe."

        if Natsuki.isLove(higher=True):
            n 4fchblleaf "¡Te amo,{w=0.2} [player]~!"

    elif Natsuki.isDistressed(higher=True):
        if already_discussed_vegetarianism:
            n 1fcsemesi "..."
            n 2fslsl "En serio,{w=0.75}{nw}"
            extend 2fsqsl " ¿[player]?"
            n 2nsqsr "¿Esto {i}de nuevo{/i}?"
        else:

            n 1fcsem "...¿En serio,{w=0.2} [player]?{w=0.75}{nw}"
            extend 2fsqsr " ¿{i}Vegetarianismo{/i}?"
            n 2fcssl "..."

        n 1fcssl "..."
        n 1nsrsl "Como sea.{w=1}{nw}"
        extend 2fsrsr " No es como si tuviera mucho que decir al respecto."
        n 1nnmbo "Nunca realmente lo practiqué ni nada de eso,{w=0.75}{nw}"
        extend 1nllsl " pero puedo al menos respetar el esfuerzo que la gente hace."
        n 2fcsaj "Toma verdaderas agallas cortar tantas opciones de tu dieta.{w=0.75}{nw}"
        extend 2flrca " O incluso de tu estilo de vida completamente."
        n 4nlrtr "La gente lo hace por un montón de razones,{w=0.75}{nw}"
        extend 4nsrsl " obviamente."
        n 1nlrpu "Pero...{w=1}{nw}"
        extend 1nnmsl " supongo que es genial cómo una sola elección de estilo de vida puede unir a montones de personas."
        n 1ullsl "El ambiente,{w=0.5}{nw}"
        extend 2nslsf " bienestar animal...{w=0.75}{nw}"
        extend 2ksrbo " incluso solo frutas y vegetales siendo más baratos de comprar al por mayor."
        n 1fcsca "Es todo igual de válido.{w=0.75}{nw}"
        extend 1ncssl " Justo como la elección de empezar a ir libre de animales o no."
        n 2ncsss "...Je.{w=0.75}{nw}"
        extend 2fsqsl " Y hablando de elecciones que la gente hace..."
        n 4fnmem "No hay premios por adivinar quién debería estar haciendo mejores ahora mismo,{w=0.75}{nw}"
        extend 1fsqan " {i}[player]{/i}."
    else:

        if already_discussed_vegetarianism:
            n 1fcsan "Oh,{w=0.75}{nw}"
            extend 2fsqupl " vete a pasear ya,{w=0.2} [player]."
            n 2fsleml "{i}Todavía{/i} no te doy una respuesta.{w=0.75}{nw}"
            extend 1fsqful " ¿Y-{w=0.2}y por qué debería?"
            n 1fcsanltsa "{i}Cualquier cosa{/i} que diga está mal,{w=0.75}{nw}"
            extend 2fcssrltsa " aparentemente."
            n 2fnmfultsc "¿No es así?"
        else:

            n 1fsqeml "...Wow.{w=0.75}{nw}"
            extend 2fnmanltsc " ¿Y por qué debería siquiera {i}molestarme{/i} en responder,{w=0.2} [player]?"
            n 2fllunltsc "¿Conociéndote?"
            n 1fcsfultsa "Cualquier respuesta que dé va a ser la {i}incorrecta{/i} de todos modos,{w=0.75}{nw}"
            extend 2fsqfultsb " ¿no es así?"
            n 2fcsupltsa "Imbécil."

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_staying_motivated",
            unlocked=True,
            prompt="Manteniéndose motivado",
            conditional="jn_utils.get_total_gameplay_hours() >= 4",
            category=["Vida"],
            affinity_range=(jn_affinity.NORMAL, None),
            nat_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_staying_motivated:
    n 1kcsemesi "...{w=1.25}{nw}"
    n 2ksrem "Hombre..."
    n 2fsrsl "..."
    n 4flrfl "Sabes,{w=0.2} [player].{w=0.75}{nw}"
    extend 4fsqfl " ¿Si hay una cosa que {i}realmente{/i} no puedo soportar?"
    n 1fllem "Es cuando por cualquier razón,{w=0.2} simplemente no puedo motivarme sobre nada.{w=1}{nw}"
    extend 1fcsgs " ¡Es lo peor!"
    n 4flrfl "Como...{w=0.75}{nw}"
    extend 2fsrsl " cuando nada parece valer el esfuerzo,{w=0.75}{nw}"
    extend 2ksqsl " o sientes que solo estás posponiendo algo.{w=0.75}{nw}"
    extend 4knmajsbr " ¡Incluso si realmente quieres hacerlo!"
    n 3fnman "¿Y entonces?{w=0.5}{nw}"
    extend 3fllfl " ¿Si {i}no{/i} sales de eso de alguna forma?"
    n 1fcsan "¡Terminas sintiéndote toda horrible por no hacer algo!{w=0.75}{nw}"
    extend 1fbkwr " ¡{i}Apesta{/i}!"
    n 2fcsem "Ugh.{w=1.25}{nw}"
    extend 2fslem " En siente como que simplemente no puedes ganar a veces."
    n 4unmfllsbl "...¡E-{w=0.2}eso no quiere decir que me sienta así a menudo ni nada!{w=0.75}{nw}"
    extend 3fcsemlsbl " ¡N-{w=0.2}no hay forma!{w=0.75}{nw}"
    extend 3fcsbgsbr " {i}Siempre{/i} tengo las cosas bajo control."
    n 1fcsss "Je."
    n 4fsqss "...¿Y sabes por qué,{w=0.2} [player]?"
    n 4fsqcs "Sí.{w=0.75}{nw}"
    extend 2fcsbg " Apuesto a que sí."
    n 2fchgn "¡Porque sé justo como decirle a ese tipo de humor que se largue!"

    if get_topic("talk_time_management").shown_count > 0:
        n 1ullaj "Digo,{w=0.75}{nw}"
        extend 2tllbo " creo que mencioné el timeboxing antes.{w=0.75}{nw}"
        extend 2nslss " Tener al menos {i}algún{/i} tipo de estructura para seguir puede ayudar."
        n 1tnmaj "¿Pero personalmente?{w=0.75}{nw}"
    else:

        n 1tlraj "¿Personalmente?{w=0.75}{nw}"

    extend 1unmaj " Encuentro que la mayoría del problema es solo entrar en el humor correcto -{w=0.5}{nw}"
    extend 4ulraj " y no hay escasez de formas de llegar allí."
    n 3fchgn "¡Como la música!"
    n 3fcsbg "¡Nada vence a mis probadas y verdaderas listas de música para sacarme de la rutina!{w=0.75}{nw}"
    extend 3fcssmeme " Una buena melodía o dos {i}siempre{/i} me animan."
    n 4fnmaj "¡Pero necesitas hacer lo que funcione para {i}ti{/i},{w=0.2} [player]!"

    if persistent.jn_player_tea_coffee_preference in ["tea", "coffee"]:
        n 1fsqss "Beber un poco de [persistent.jn_player_tea_coffee_preference],{w=1}{nw}"
    else:

        n 1ullbo "Conseguir algo de cafeína en tu sistema,{w=0.75}{nw}"

    extend 2ulraj " abrir las ventanas para algo de aire fresco,{w=0.75}{nw}"
    extend 2fcsbg " levantarte de tu trasero -{w=1}{nw}"
    extend 2fnmfl " ¡lo que sea que sea!"
    n 4fcsaj "Es todo sobre conseguir que ese ímpetu vaya...{w=0.75}{nw}"
    extend 4fcsca " ¡y luego mantenerlo!"
    n 2nsqsr "En serio.{w=0.5}{nw}"
    extend 2fsrem " La peor cosa que puedes hacer es ponerte todo encendido y solo dejar lo que sea que estés haciendo de inmediato.{w=0.75}{nw}"
    extend 2fnmgs " ¡Tienes que comprometerte!"
    n 1fsrca "Y no dejes distraerte -{w=0.5}{nw}"
    extend 4fcscaesm " una cosa a la vez.{w=0.75}{nw}"
    extend 4fcssm " ¡Y termina lo que empieces!"

    n 1fsqfl "Pero lo más importante,{w=0.2} [player]?"
    n 1fcsfl "Solo...{w=0.75}{nw}"
    extend 2nsrpo " no seas totalmente tonto sobre ello.{w=1}{nw}"
    extend 2fnmbo " Forzarte a cosas,{w=0.2} quiero decir."
    n 4fcstr "Volver con una mentalidad fresca es igual de válido que tratar de empujar pasado el bloqueo."
    n 4flrem "Como sí,{w=0.75}{nw}"
    extend 3fsrsl " no es broma.{w=1}{nw}"
    extend 3nsqca " Apesta sentir que estás tirando el tiempo."
    n 4tllfl "Pero no es como si nunca fueras a intentar de nuevo,{w=0.75}{nw}"
    extend 4tnmbo " ¡o tener otro momento para hacer cosas!"
    n 2fcsaj "Volver más tarde solo es un desperdicio de tiempo si te {i}convences{/i} a ti mismo de que lo es -{w=1}{nw}"
    extend 2fsqca " o te convences de que nunca vas a siquiera empezar algo."

    n 1nllaj "Y hey.{w=1}{nw}"
    extend 4fsqss " ¿Sabes qué {i}nunca{/i} es una pérdida de tiempo,{w=0.2} [player]?"

    if Natsuki.isLove(higher=True):
        n 3fchgnl "¡Pasar más tiempo con tu servidora!"
        n 3fcsbgl "A-{w=0.2}ahora eso es algo que {i}sé{/i} que tú de todas las personas encuentras motivante.{w=0.75}{nw}"
        extend 1fsqsml " Ehehe."
        n 4fchbgl "¡Te amo también,{w=0.2} [player]~!"

    elif Natsuki.isAffectionate(higher=True):
        n 3fcssmledzsbl "¡Pasar más tiempo con tu servidora!"
        n 3fcsbglsbl "A-{w=0.2}ahora {i}eso es{/i} algo que cualquiera debería encontrar motivante!{w=1}{nw}"
        extend 4fsrsmlsbl " Ehehe."
    else:

        n 3fchbgedz "¡Obtener más consejos pro de tu servidora!"
        n 3fcsbg "¡De nada,{w=0.2} [player]~!{w=1}{nw}"
        extend 3fchsm " Ahaha."

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_daily_jokes_unlock",
            unlocked=True,
            conditional="not persistent._jn_daily_jokes_unlocked",
            affinity_range=(jn_affinity.HAPPY, None),
            nat_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_daily_jokes_unlock:
    n 2nllsl "..."
    n 2fllsl "..."
    n 2fcsflesi "..."
    n 2nlrfl "Sabes,{w=0.2} [player].{w=0.75}{nw}"
    extend 1nnmsl " Solo pensé en algo.{w=0.75}{nw}"
    extend 4fslfl " Algo que realmente está empezando a molestarme hasta la saciedad."
    n 2unmbo "Pasas por aquí lo suficiente,{w=0.2} ¿verdad?{w=0.75}{nw}"
    extend 2nlraj " Para visitar,{w=0.2} digo."
    n 4unmemeshsbl "¡N-{w=0.2}no que no lo aprecie,{w=0.2} ni nada de eso!{w=0.75}{nw}"

    if Natsuki.isEnamored(higher=True):
        extend 4nslsllsbl " Deberías saber que lo hago a estas alturas.{w=1}{nw}"

    elif Natsuki.isAffectionate(higher=True):
        extend 2fcsajlsbl " ¡T-{w=0.2}totalmente lo hago!{w=1}{nw}"
    else:

        extend 4fcsemsbl " ¡P-{w=0.2}por supuesto que lo hago!"
        n 2fcspo "Incluso si {i}sí{/i} como que me lo debes.{w=1}{nw}"

    extend 1nlrsl " Pero..."
    n 1fcsaj "Es solo que..."
    n 4fslun "..."
    n 4fcsansbl "¡Nnnnn...!"
    n 1fbkwrsbr "¡Es solo que se vuelve tan {w=0.3}{i}aburrido{/i}!{w=1}{nw}"
    extend 1fcswr " ¡Como si nada {i}nunca{/i} cambiara por aquí!{w=1}{nw}"
    extend 2flrgs " Es siempre lo mismo,{w=0.75}{nw}"
    extend 2fcsgs " ¡y estoy harta de eso!"
    n 1fslsl "Ugh..."
    n 4fcsemesi "..."
    n 2fcswr "¡Lo que necesitamos es variedad!"
    n 2fcsgs "¡Algo diferente!{w=0.75}{nw}"
    extend 4fcspo " Y nada diferente pasó nunca por solo sentarse a {i}esperarlo{/i}."
    n 3fllfl "TIENE que haber algo como eso por aquí en algún lugar..."
    n 3fslbo "..."
    n 4nllaj "...De hecho.{w=0.75}{nw}"
    extend 2unmfl " ¿Sabes qué?{w=1}{nw}"
    extend 2fcsca " Solo dame un par de minutos."
    n 4flrpu "Tiene que haber algo en el clóset que me perdí antes."

    show natsuki 1fcsbo
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(0.5)
    play audio chair_out
    $ jnPause(4)

    n "Bien...{w=1}{nw}"
    extend " qué tenemos..."
    n "..."
    n "¡Oh,{w=0.2} por-!"
    n "¡¿Desde cuándo se volvió este sitio el {i}basurero{/i} oficial de la escuela?!{w=1}{nw}"
    extend " ¡La mitad de esta cosa no era ni siquiera {i}nuestra{/i}!"

    play audio stationary_rustle_a
    $ jnPause(2.5)
    play audio gift_slide
    $ jnPause(3)

    n "Cielos...{w=1}{nw}"
    extend " ¿qué es esto?{w=0.75}{nw}"
    extend " ¿Una biblioteca?"
    n "¿Cuánto más de esta cosa hay...?"

    play audio gift_slide
    $ jnPause(3)

    n "...¿Huh?{w=1.25}{nw}"
    extend " Qué es..."
    n "..."
    n "Espera...{w=1}{nw}"
    extend " ¡¿e-{w=0.2}es esa mi tarea?!{w=0.75} QUIÉN-{w=0.5}{nw}"
    play audio gift_close
    n "¡Ack-!"
    n "..."
    n "Nnnnng...{w=1.5}{nw}"
    extend " m-{w=0.5}mi cabeza..."
    n "¡¿Q-{w=0.2}quién demonios solo {b}balancea{/b} libros de esa forma?!{w=0.75}{nw}"
    extend " ¡En {i}serio{/i} voy a...!"
    n "..."
    n "..."
    n "...Espera un segundo.{w=1.5}{nw}"
    extend " Oh.{w=0.2} Por.{w=0.2} Dios."
    n "Esto...{w=1.25}{nw}"
    extend " es...{w=1.25}{nw}"
    extend " ¡{b}PERFECTO{/b}!"
    n "..."
    n "...!"

    $ jnPause(2)

    show natsuki 1fcssmeme
    play audio chair_in
    $ jnPause(1.5)
    hide black with Dissolve(0.5)
    $ jnPause(0.5)

    n 4fchbg "¡[player]!{w=0.5} ¡[player]!"
    n 4uchgneme "¿Adivina qué enconteeee~?{w=0.75}{nw}"
    extend 4fsqsmeme " Ehehe."
    n 4fcsbs "Es...{w=1.5}{nw}"

    show natsuki 1uchgn
    show joke_book zorder JN_PROP_ZORDER
    play audio page_turn
    $ jnPause(3)

    extend 1uchgnedz " ¡nuestro viejo libro de chistes del salón!{w=0.75}{nw}"
    extend 1fchbgedz " ¡Duh!"
    n 1fcsbg "¡Y justo cuando estaba empezando a preguntarme si este lugar tenía {i}algo{/i} de literatura!"
    n 1fsrbgsbl "...Bueno...{w=0.75}{nw}"
    extend 1fsrposbl " cualquiera que {i}no sea{/i} solo mi propio material,{w=0.2} como sea."
    n 1fsqsm "..."
    n 1tsqbosbl "..."
    n 1fnmflsbl "¿Qué?{w=0.75}{nw}"
    extend 1fcsposbl " No comiences dándome eso,{w=0.2} [player].{w=1}{nw}"
    extend 1fcsaj " Además."
    n 1tsqbg "¿{i}Tú{/i} tenías algo mejor?"
    n 1tsqcs "..."
    n 1fcscsesm "..."
    n 1fcsbg "¡Sip!{w=0.75}{nw}"
    extend 1fcssm " Eso es sobre lo que esperaba.{w=1}{nw}"
    extend 1fsqsm " Ehehe."
    n 1fcsss "Hombre...{w=1}{nw}"
    extend 1fchbg " ¡No puedo esperar para empezar a soltar algunos de estos!{w=0.75}{nw}"
    extend 1uchgn " ¡Esto va a ser genial,{w=0.2} simplemente lo sé!"
    n 1nchsmeme "..."
    n 1unmaj "Oh -{w=0.5}{nw}"
    extend 1nllaj " Probablemente debería mencionar,{w=0.2} [player]."
    n 1nslca "No quiero terminar quemando esta cosa demasiado rápido.{w=0.75}{nw}"
    extend 1nsqslsbr " O terminaríamos justo de vuelta donde estábamos.{w=1.25}{nw}"
    extend 1ulraj " Así que..."
    n 1fcsbg "Solo voy a elegir algo diario para torturarte con ello.{w=0.75}{nw}"
    extend 1fchbg " No hay razón para exagerar."
    n 1fsqss "¿Suena como un plan,{w=0.2} [player]?{w=0.75}{nw}"
    extend 1fcsss " Claro que sí."
    n 1fcsgs "¡Así que!{w=0.5}{nw}"
    extend 1fcsbg " Mejor empieza a esperarlo..."
    n 1fchgn "¡Porque yo {i}definitivamente{/i} lo hago!{w=1}{nw}"
    extend 1nchgn " Ehehe."

    n 1fllsm "..."
    n 1fllbg "De hecho...{w=1}{nw}"
    extend 1fsqbg " ¿sabes qué,{w=0.2} [player]?{w=0.75}{nw}"
    extend 1fcsbg " ¿Por qué esperar?"
    n 1fsqsm "Sabes lo que dicen,{w=0.2} después de todo.{w=1}{nw}"
    extend 1fchgn " ¡No hay tiempo como el presente!"

    $ persistent._jn_daily_jokes_unlocked = True
    call talk_daily_joke (from_unlock=True)

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_daily_joke",
            unlocked=True,
            prompt="Chiste diario",
            conditional="persistent._jn_daily_jokes_unlocked and persistent._jn_daily_jokes_enabled and not persistent._jn_daily_joke_given",
            affinity_range=(jn_affinity.HAPPY, None),
            nat_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_daily_joke(from_unlock=False):
    if not from_unlock:
        $ dialogue_choice = random.randint(1, 6)
        if dialogue_choice == 1:
            n 1nchgn "¡Okaaay!{w=1}{nw}"
            extend 3fsqbg " Creo que ambos sabemos de qué es hora ahora,{w=0.2} ¿eh?{w=1.25}{nw}"
            extend 3fsqsm " Ehehe."

        elif dialogue_choice == 2:
            n 4fcsbg "¡Bien!{w=1}{nw}"
            extend 2tlrss " Creo que ya es hora,{w=0.2} [player].{w=1.25}{nw}"
            extend 2tsqsm " ¿No crees?"

        elif dialogue_choice == 3:
            n 2fcsaj "¡Correcto!{w=1}{nw}"
            extend 2fcsbg " Creo que ahora es tan buen momento como cualquier otro."
            n 4tlrbo "Ahora dónde dejé ese libro..."

        elif dialogue_choice == 4:
            n 4tllbo "Hmmm..."
            n 4tnmaj "¿Sabes qué,{w=0.2} [player]?{w=1}{nw}"
            extend 3fsqbg " Creo que es cerca de esa hora otra vez."
            n 3fcssm "Ehehe."

        elif dialogue_choice == 5:
            n 2ulraj "Sabes,{w=0.2} [player]...{w=1}{nw}"
            extend 2flrcs " Creo que ya es la hora.{w=1.25}{nw}"
            extend 4fsqcs " ¿Tú no?"

        elif dialogue_choice == 6:
            n 1fcsbg "¡Muy bien!{w=1}{nw}"
            extend 4fwrbg " ¡Creo que ya es hora para el viejo libro de chistes!{w=0.75}{nw}"
            extend 4fcssm " Ehehe."

        show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
        show joke_book zorder JN_PROP_ZORDER
        $ Natsuki.setIsReadingToRight(True)
        show natsuki reading
        hide black with Dissolve(0.5)
        $ jnPause(0.5)

    $ daily_jokes = jn_jokes.getUnseenJokes()

    if not daily_jokes:
        $ jn_jokes.resetJokes()
        n 1fcsemesi "..."
        n 1fsrpo "Hombre...{w=1}{nw}"
        extend 1tnmbo " realmente {i}estamos{/i} pasando a través de estas cosas,{w=0.2} ¿eh?{w=1.25}{nw}"
        extend 1fcsflsbl " ¡Me voy a quedar sin chistes completamente a este paso!"
        n 1nsrslsbr "..."
        n 1nsrajsbr "A ti...{w=1.25}{nw}"
        extend 1flrsssbr " ¿no te importa si solo empiezo a elegirlos al azar,{w=0.2} verdad?"
        n 1fcsgslsbr "¡N-{w=0.2}no me malinterpretes!"
        extend 1fllflsbr " ¡Todavía voy a al menos {i}intentar{/i} mantener las cosas frescas!{w=1}{nw}"
        extend 1fcsposbr " O-{w=0.2}obviamente."
        n 1nsqpo "Solo no me des ninguna mirada graciosa si elijo uno que ya has escuchado.{w=1.25}{nw}"
        extend 1fsqpo " ¿Capiche?"

        if Natsuki.isLove(higher=True):
            n 1fsqsm "Ehehe.{w=1}{nw}"
            $ chosen_tease = jn_utils.getRandomTease()
            extend 1fchbll " ¡Te amo también,{w=0.2} [chosen_tease]!"

        elif Natsuki.isAffectionate(higher=True):
            n 1fsqsm "Ehehe.{w=1}{nw}"
            extend 1uchgnl " ¡Apreciado,{w=0.2} [player]!"

        $ daily_jokes = jn_jokes.getUnseenJokes()

    n 1fcsss "Ahora,{w=0.75}{nw}"
    extend 1fsqsm " veamos..."

    $ Natsuki.setIsReadingToRight(True)
    show natsuki reading
    $ jnPause(3)
    play audio page_turn
    $ jnPause(2)

    $ daily_joke = random.choice(daily_jokes)
    if daily_joke.joke_category == jn_jokes.JNJokeCategories.corny:
        $ dialogue_choice = random.randint(1, 4)
        if dialogue_choice == 1:
            n 1nsrflsbl "Oh,{w=0.2} cielos."

        elif dialogue_choice == 2:
            n 1ncsemesi "..."

        elif dialogue_choice == 3:
            n 1nslposbl "..."

        elif dialogue_choice == 4:
            n 1nsrem "...¿{i}En serio{/i}?"
            n 1ncsemesi "..."

    elif daily_joke.joke_category == jn_jokes.JNJokeCategories.bad:
        $ dialogue_choice = random.randint(1, 3)
        if dialogue_choice == 1:
            n 1fcsemesi "..."

        elif dialogue_choice == 2:
            n 1fupem "Oh,{w=0.5} por-{w=1.25}{nw}"
            n 1fcssl "..."

        elif dialogue_choice == 3:
            n 1fsrem "Ugh..."

    elif daily_joke.joke_category == jn_jokes.JNJokeCategories.confusing:
        $ dialogue_choice = random.randint(1, 3)
        if dialogue_choice == 1:
            n 1cdwpu "...Huh."

        elif dialogue_choice == 2:
            n 1tdrsl "..."
            n 1tdlpu "O-{w=0.2}kay..."

        elif dialogue_choice == 3:
            n 1tdwca "..."
            n 1tdwaj "Uh...{w=1}{nw}"
            extend 1tdwbo " huh."
    else:

        $ dialogue_choice = random.randint(1, 6)
        if dialogue_choice == 1:
            n 1fcsss "¡Ah!{w=0.75}{nw}"
            extend 1fchgn " ¡Este servirá!"

        elif dialogue_choice == 2:
            n 1unmbs "¡Oh!{w=0.5} ¡Oh!{w=0.75}{nw}"
            extend 1fcsbs " ¿Qué tal este?"

        elif dialogue_choice == 3:
            n 1fcsbg "¡Ajá!{w=0.75}{nw}"
            extend 1fsqsm " ¡Aquí vamos!"

        elif dialogue_choice == 4:
            n 1fspgs "Hmm...{w=0.75}{nw}"
            extend 1fnmbg " ¿qué tal este,{w=0.2} [player]?"

        elif dialogue_choice == 5:
            n 1nchgn "¡Muy bien!{w=0.75}{nw}"
            extend 1fcsbg " ¡Probemos {i}este{/i} para ver qué tal!"

        elif dialogue_choice == 6:
            n 1unmbg "¡Oh!{w=0.75}{nw}"
            extend 1fchgn " ¡Tengo uno!{w=0.5} ¡Tengo uno!"

        n 1fcsaj "¡A-{w=0.2}hem!"
        n 1fcssm "..."

    call expression daily_joke.label

    $ daily_joke.setSeen(True)
    $ persistent._jn_daily_joke_given = True
    $ Natsuki.calculatedAffinityGain(bypass=True)
    $ dialogue_choice = random.randint(1, 3)

    if daily_joke.joke_category == jn_jokes.JNJokeCategories.funny:
        if dialogue_choice == 1:
            n 1uchgn "¿Ves?{w=1}{nw}"
            extend 1fchbg " ¡Te {i}dije{/i} que este libro tenía cosas buenas!"
            n 1fwlbg "¡De nada,{w=0.2} [player]!"
            extend 1fchsmeme " Ehehe."

        elif dialogue_choice == 2:
            n 1fllbg "Hombre..."
            n 1fchgn "Estoy {w=0.2}{i}tan{/i}{w=0.2} marcando ese.{w=1}{nw}"
            extend 1fchsmeme " Ehehe."
            n 1uchgn "¡Aprecio que sintonices,{w=0.2} [player]!"
        else:

            n 1fchdvesm "¡Pfffft-!"
            n 1fchbg "Okay,{w=0.2} okay.{w=0.75}{nw}"
            extend 1flrbg " Tienes que admitir.{w=1}{nw}"
            extend 1fcsbg " Ese {w=0.2}{i}fue{/i}{w=0.2} bastante bueno."
            n 1fchbg "¡Apuesto a que tendrás otro mañana,{w=0.2} [player]!"

        show natsuki 1fchsm

    elif daily_joke.joke_category == jn_jokes.JNJokeCategories.corny:
        if dialogue_choice == 1:
            n 1fsrem "...Cielos."
            n 1fsrca "..."
            n 1fcsbgsbl "B-{w=0.2}bueno,{w=0.5}{nw}"
            extend 1fcstrsbl " ¡nunca dije que serían {w=0.2}{i}buenos{/i}{w=0.2} chistes!"
            n 1fchgn "¡Lo siento,{w=0.2} [player]~!"

        elif dialogue_choice == 2:
            n 1nsqsr "..."
            n 1nslaj "Estoy...{w=1.25}{nw}"
            extend 1nllss " empezando a darme cuenta de {i}por qué{/i} nunca vimos este libro muy seguido."
            n 1ullss "Bueno -{w=0.3}{nw}"
            extend 1fwlbg " ¡Mejor suerte la próxima vez,{w=0.2} [player]!"
            n 1fchsm "Ahaha."
        else:

            n 1nlrfl "...Wow.{w=1.25}{nw}"
            extend 1fsqpo " De hecho estoy empezando a pensar que el libro en sí es el chiste a este punto."
            n 1nslpo "..."
            n 1nllaj "Bueno,{w=0.5}{nw}"
            extend 1fcsfl " todavía no voy a retractarme de lo que dije.{w=1}{nw}"
            extend 1fchgn " Lo siento [player]."
            n 1fsqbg "¡Pero eso es todo lo que obtendrás por hoy!"

        show natsuki 1fchsm

    elif daily_joke.joke_category == jn_jokes.JNJokeCategories.bad:
        if dialogue_choice == 1:
            n 1fcsfl "...Okay,{w=1.25}{nw}"
            extend 1fbkwr " ¿quién demonios aprobó {i}eso{/i}?{w=0.75}{nw}"
            extend 1fcsgs " ¡Cielos!"
            n 1fslpo "No puedo creer que alguien {i}realmente{/i} pagara dinero por esto.{w=1.25}{nw}"
            extend 1fcsaj " Como sea."
            n 1fsrfl "El siguiente mejor que sea bueno.{w=1}{nw}"
            extend 1fcspoesi " Eso es todo lo que {i}yo{/i} tengo que decir."

        elif dialogue_choice == 2:
            n 1fcsemesi "..."
            n 1fsqwr "¿En serio?{w=1.25}{nw}"
            extend 1fllfl " ¿Es {i}un{/i} buen chiste mucho pedir?{w=1}{nw}"
            extend 1fcsfl " Vamos {w=0.2}{i}ya{/i}."
            n 1flrfl "He terminado con esta cosa."
            n 1fsrem "{i}'Galardonado'{/i},{w=1}{nw}"
            extend 1fcsfl " mi {i}trasero{/i}."
        else:

            n 1fcssl "..."
            n 1fcsan "¡Uuuuuu-!"
            n 1fbkwr "¡¿Por qué tantos de estos solo {w=0.2}{i}apestan{/i}{w=0.2}?!{w=1.25}{nw}"
            extend 1fcswrl " ¡En serio!"
            n 1fcsgssbr "¡El único chiste aquí es cuánto les pagaron a estos escritores!"
            n 1fsrslesi "..."
            n 1fsqtr "¿Sabes qué?{w=1}{nw}"
            extend 1fcsca " Creo que eso es más que suficiente por hoy."

        show natsuki 1fcspo

    elif daily_joke.joke_category == jn_jokes.JNJokeCategories.confusing:
        if dialogue_choice == 1:
            n 1cdwslsbl "..."
            n 1cnmslsbl "..."
            n 1cdrslsbl "..."
            n 1cdrflsbr "...Sí.{w=0.75}{nw}"
            extend 1csrcasbr " No mucho que decir sobre {i}eso{/i},{w=0.2} [player]."

        elif dialogue_choice == 2:
            n 1tdwbo "..."
            n 1tdwfl "Yo...{w=1}{nw}"
            extend 1cslslsbr " no lo entiendo.{w=0.75}{nw}"
            extend 1cnmemsbr " ¿Se {i}suponía{/i} siquiera que fuera gracioso o qué?"
            n 1clrajsbr "'Chistes para todos',{w=0.5}{nw}"
            extend 1csrbosbr " mi trasero."
        else:

            n 1csrfl "...Sí."
            n 1tlrfl "Yo...{w=1}{nw}"
            extend 1csrsssbl " creo que hemos terminado con esto por hoy,{w=0.5}{nw}"
            extend 1cslcasbl " [player]."

        show natsuki 1nsrbo
    else:

        if dialogue_choice == 1:
            n 1fcsbg "¡Gracias por escuchar~!{w=0.75}{nw}"
            extend 1fchsm " Ehehe."

        elif dialogue_choice == 2:
            if Natsuki.isLove(higher=True):
                n 1fwlsml "¡Te amo también,{w=0.2} [player]!{w=0.75}{nw}"
                extend 1fchsml " Ehehe."
            else:

                n 1fchgn "¡De nada,{w=0.2} [player]!"
        else:

            n 1fsqbg "¿Misma hora mañana,{w=0.2} [player]?{w=0.75}{nw}"
            extend 1nchgn " Ehehe."

        show natsuki 1fchsm

    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(1.5)
    play audio drawer
    hide joke_book
    show natsuki 1fchsmeme
    $ jnPause(1.3)
    hide black with Dissolve(0.5)
    $ jnPause(1)

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_daily_jokes_start",
            unlocked=True,
            prompt="¿Puedes empezar a contarme chistes diarios?",
            category=["Bromas"],
            conditional="persistent._jn_daily_jokes_unlocked and not persistent._jn_daily_jokes_enabled",
            affinity_range=(jn_affinity.HAPPY, None),
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_daily_jokes_start:
    n 2usqss "¿Oho?{w=1}{nw}"
    extend 4nlrbg " ¿Qué es esto ahora,{w=0.75}{nw}"
    extend 4tsqbg " tan de repente?"
    n 2fcsbg "¡Parece que realmente {w=0.2}{i}no puedes{/i}{w=0.2} tener suficiente de mi increíble entrega de chistes después de todo!"
    n 2fsqsmeme "Ehehe."
    n 1fcsss "Bueno en ese caso,{w=1}{nw}"
    extend 4fnmss " será mejor que te prepares,{w=0.2} [player]."
    n 3fchgn "Porque voy a elegir todos los {i}extra{/i} cursis ahora.{w=1}{nw}"
    extend 3nchgn " ¡Solo para tiiiii~!"

    if Natsuki.isLove(higher=True):
        n 3fchbll "¡Te amo,{w=0.2} [player]!"

    $ persistent._jn_daily_jokes_enabled = True

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_daily_jokes_stop",
            unlocked=True,
            prompt="¿Puedes dejar de contarme chistes diarios?",
            category=["Bromas"],
            conditional="persistent._jn_daily_jokes_unlocked and persistent._jn_daily_jokes_enabled",
            affinity_range=(jn_affinity.HAPPY, None),
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_daily_jokes_stop:
    n 1unmem "¿H-{w=0.3}huh?{w=1}{nw}"
    extend 4fcseml " Espera,{w=0.5}{nw}"
    extend 4fnmeml " ¿qué?"
    n 1fcswr "¡¿Y-{w=0.2}y qué se supone que significa {i}eso{/i},{w=0.2} [player]?!"
    extend 3fnmfl " ¿Huh?"
    n 3fnmgs "¿Tienes algún tipo de problema con el libro?"
    n 4fsqwr "¿Crees que mi entrega simplemente apesta?{w=1}{nw}"
    extend 4fbkwr " ¡¿Es eso?!"
    n 2fcspo "..."
    n 2fsqcs "..."
    n 2fchdvesm "¡Pfffft-!{w=1}{nw}"
    extend 1fchbs " ¡Relájate,{w=0.2} [player]!{w=0.75}{nw}"
    extend 4fchgn " ¡Relájate!{w=0.75}{nw}"
    extend 3klrbg " Hombre..."
    n 3fnmbg "Tú {i}realmente{/i} tienes que ver la expresión en tu cara a veces.{w=1}{nw}"
    extend 3uchgn " ¡No tiene precio!"
    n 4ullaj "Nah,{w=0.2} está bien.{w=1}{nw}"
    extend 4nllbo " Supongo."
    n 1nsrpo "No es como si fueran los {i}mejores{/i} chistes de todos modos.{w=1}{nw}"
    extend 1nlrfl " Ya sabes.{w=1}{nw}"
    extend 2nsrsslsbr " No siendo {i}míos{/i} y todo,{w=0.2} p-{w=0.2}por supuesto."
    n 4nlraj "Así que...{w=1}{nw}"
    extend 4tnmca " solo déjame saber cuando te aburras o algo,{w=0.2} supongo."
    extend 4fcstr " Además."
    n 4fchgn "...¡No es como si alguna vez fuera a dejar pasar una oportunidad para hacerte retorcer!{w=1}{nw}"
    extend 4fcssm " Ahaha."

    if Natsuki.isLove(higher=True):
        n 3fchtsl "¡Te amo también,{w=0.2} [player]~!"

    $ persistent._jn_daily_jokes_enabled = False

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_daily_jokes_seen_before_start",
            unlocked=True,
            prompt="¿Qué chistes me has contado antes?",
            category=["Bromas"],
            conditional="persistent._jn_daily_jokes_unlocked and jn_jokes.getShownBeforeJokes() is not None",
            affinity_range=(jn_affinity.HAPPY, None),
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_daily_jokes_seen_before_start:
    if persistent._jn_daily_jokes_enabled:
        n 4ccsss "¿Oh?{w=0.75}{nw}"
        extend 4ccsbg " ¿Qué es esto ahora,{w=0.2} tan de repente?{w=0.75}{nw}"
        extend 3fsqbg " {i}Alguien{/i} simplemente no puede tener suficiente del libro de chistes,{w=0.2} ¿eh?"
        n 3fcssm "Ehehe."
        n 4ullaj "Bueno...{w=1}{nw}"
        extend 5cllss " No tomé notas exactamente ni nada de los que te he contado...\n{w=0.75}{nw}"
        extend 2fcssssbr " ¡pero estoy bastante segura de que puedo averiguarlo!"
        n 4unmaj "Solo dame un segundo aquí..."
    else:

        n 1csqss "¿Oh?{w=0.75}{nw}"
        extend 4fnmss " ¿Estoy escuchando esto bien?"
        n 4fsqbg "¿{i}Ahora{/i} de repente quieres escuchar todo sobre los chistes?{w=0.75}{nw}"
        extend 3fcsbg " ¿Los que prácticamente me {i}rogaste{/i} que dejara de contarte?"
        n 3tsqss "...¿{i}Esos{/i} chistes?"
        n 4fsqsm "..."
        n 4fcssm "Ehehe."
        n 2fcsbs "No digas más,{w=0.2} no digas más.{w=0.75}{nw}"
        extend 2fchgn " ¡[n_name] te tiene cubierto!"
        n 4ccsss "Solo dame un segundo aquí..."

    show natsuki 4fcssmeme
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(0.5)
    play audio drawer
    $ Natsuki.setDeskItem(jn_desk_items.getDeskItem("jn_joke_book_held"))
    show natsuki 1fchsmeme
    $ jnPause(2.25)
    hide black with Dissolve(0.5)
    $ jnPause(0.5)

    if random.choice([True, False]):
        n 1fchbgeme "¡Bien!{w=0.75}{nw}"
        extend 1fcsbg " ¡Háblame,{w=0.2} [player]!{w=0.75}{nw}"
        extend 1tnmss " ¿Qué querías escuchar otra vez?"
    else:

        n 1fchbgeme "¡Okaaay!{w=0.75}{nw}"
        extend 1fchgn " ¡Aquí vamos,{w=0.2} [player]!{w=0.75}{nw}"
        extend 1tsqsm " ¿Cuál querías escuchar?"

    call talk_daily_jokes_seen_before_loop

    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(0.5)
    play audio drawer
    $ Natsuki.clearDeskItem(jn_desk_items.JNDeskSlots.centre)
    show natsuki 1nchsmeme
    $ jnPause(2.25)
    hide black with Dissolve(0.5)
    $ jnPause(0.5)

    return

label talk_daily_jokes_seen_before_loop:
    python:
        joke_options = []
        for joke in jn_jokes.getShownBeforeJokes():
            joke_options.append((joke.display_name, joke))

        joke_options.sort(key = lambda option: option[0])

    show natsuki option_wait_holding at jn_left
    call screen scrollable_choice_menu(
        joke_options,
        ("Olvídalo", None),
        400,
        "mod_assets/icons/joke_book.png")
    show natsuki at jn_center
    $ joke_choice = _return

    if isinstance(joke_choice, jn_jokes.JNJoke):
        $ dialogue_choice = random.randint(1, 3)
        if joke_choice.joke_category == jn_jokes.JNJokeCategories.funny:
            if dialogue_choice == 1:
                n 1unmaj "¡Ooh!{w=0.75}{nw}"
                extend 1unmbg " ¡Sí!{w=0.5}{nw}"
                extend 1fchbg " ¡Amo ese!"

            elif dialogue_choice == 2:
                n 1tsqss "[joke_choice.display_name],{w=0.2} ¿eh?"
                n 1fchsm "Ehehe.{w=0.75}{nw}"
                extend 1fchbg " ¡Lo tienes,{w=0.2} [player]!"
            else:

                n 1uspbg "¡Oh!{w=0.2} ¡Oh!{w=0.5}{nw}"
                extend 1uchgn " ¡Amo ese!"

            show natsuki 1udwsm

        elif joke_choice.joke_category == jn_jokes.JNJokeCategories.corny:
            if dialogue_choice == 1:
                n 1csqfl "...¿En serio?{w=0.75}{nw}"
                extend 1fllfl " ¡Pero ni siquiera era {i}tan{/i} bueno,{w=0.2} [player]!"
                n 1ccsemesi "..."

            elif dialogue_choice == 2:
                n 1csrem "Hombre...{w=1}{nw}"
                extend 1tnmem " ¿estás {i}seguro{/i} de que quieres escuchar ese de nuevo?{w=0.75}{nw}"
                extend 1nslsl " Bien."
            else:

                n 1nsqflsbr "...¿Ese de {i}nuevo{/i}?{w=0.75}{nw}"
                extend 1cslemsbr " Cielos..."

            show natsuki 1ndwbo

        elif joke_choice.joke_category == jn_jokes.JNJokeCategories.bad:
            if dialogue_choice == 1:
                n 1fcsan "Oh,{w=0.2} por-{w=0.5}{nw}"
                n 1ccsemesi "..."
                n 1csrtr "Solo {i}tenías{/i} que elegir ese,{w=0.5}{nw}"
                extend 1csqca " ¿eh?"
                n 1cslaj "...Bien.{w=0.75}{nw}"
                extend 1ccsaj " Como sea."

            elif dialogue_choice == 2:
                n 1ccsemesi "..."
                n 1clrfl "¿En serio,{w=0.2} [player]?{w=0.75}{nw}"
                extend 1csqfl " ¿{i}Ese{/i}?"
                n 1nslposbr "...Bien."
            else:

                n 1fupfl "Ugh...{w=1}{nw}"
                extend 1cnmfl " ¿en serio?"
                n 1clraj "{i}No puedes{/i} hablar en serio,{w=0.2} [player].{w=0.75}{nw}"
                extend 1csqemsbr " ¿[joke_choice.display_name]?"
                n 1ccsslesisbr "..."

            show natsuki 1cdwca

        elif joke_choice.joke_category == jn_jokes.JNJokeCategories.confusing:
            if dialogue_choice == 1:
                n 1cdwpu "...¿[joke_choice.display_name],{w=0.2} [player]?{w=0.75}{nw}"
                extend 1tsqpu " ¿Estás seguro?"
                n 1tslsl "..."
                n 1tllbo "Bueno...{w=1}{nw}"
                extend 1tdlsl " si tú lo dices,{w=0.2} supongo."

            elif dialogue_choice == 2:
                n 1tnmpu "...¿En serio?{w=0.75}{nw}"
                extend 1tsqpu " ¿[joke_choice.display_name]?"
                n 1tsrbo "...Huh.{w=0.75}{nw}"
                extend 1tlraj " Si insistes.{w=0.75}{nw}"
                extend 1ccsflsbl " Solo no digas que no te lo advertí."
            else:

                n 1ccsflsbr "...Espera.{w=0.75}{nw}"
                extend 1ccsflsbr " ¿[joke_choice.display_name]?{w=0.75}{nw}"
                extend 1tsqslsbr " ¿Seguro?"
                n 1ccssssbl "¿Qué?{w=0.75}{nw}"
                extend 1csqsssbl " ¿Realmente {i}entiendes{/i} ese chiste o algo?"
                n 1ccsajsbl "...Como sea."

            show natsuki 1cdwca
        else:

            if dialogue_choice == 1:
                n 1unmaj "¿[joke_choice.display_name]?{w=0.75}{nw}"
                extend 1fchbg " ¡Seguro!"

            elif dialogue_choice == 2:
                n 1tnmss "¿[joke_choice.display_name]?{w=0.75}{nw}"
                extend 1fcssm " ¡Lo tienes!"
            else:

                n 1udwaj "¿[joke_choice.display_name]?{w=0.75}{nw}"
                extend 1unmbo " ¿Ese?"
                n 1nchbg "¡OKay!{w=0.75}{nw}"
                extend 1fcsbg " ¡Aquí vamos!"

            show natsuki 1cdwsm

        play audio page_turn

        if random.choice([True, False]):
            $ jnPause(1.25)
            play audio page_turn

        $ jnPause(1.25)

        n 1fcsaj "¡A-{w=0.2}hem!"
        n 1fcsbo "..."

        call expression joke_choice.label

        $ dialogue_choice = random.randint(1, 3)
        if joke_choice.joke_category == jn_jokes.JNJokeCategories.funny:
            if dialogue_choice == 1:
                n 1flrss "Hombre...{w=1}{nw}"
                extend 1fchgn " ¡Juro que ese nunca pasa de moda!{w=0.75}{nw}"
                extend 1nchgnl " Ahaha."

            elif dialogue_choice == 2:
                n 1fcssm "Ehehe.{w=0.75}{nw}"
                extend 1fchbg " ¡Sip!"
                n 1fchbsl "¡Ahora eso es lo que yo llamo aprobado por [n_name]!"
            else:

                n 1fcssmeme "Ehehe.{w=0.75}{nw}"
                extend 1ulrss " Bueno,{w=0.2} ¿qué puedo decir?"
                n 1fwlbgl "¡Tienes que amarlo,{w=0.2} [player]!"

            n 1ullss "Como sea..."
            show natsuki 1tnmss

        elif joke_choice.joke_category == jn_jokes.JNJokeCategories.corny:
            if dialogue_choice == 1:
                n 1nsrfl "...Sí."
                n 1fcsaj "Tengo que decir.{w=0.75}{nw}"
                extend 1cllbo " No me quejaría si {i}ese{/i} nunca apareciera de nuevo.{w=0.75}{nw}"
                extend 1ccsbosbr "\nSolo digo."

            elif dialogue_choice == 2:
                n 1ccsflesi "..."
                n 1csraj "En serio no puedo creer que alguien {i}pagara{/i} por esto.{w=0.75}{nw}"
                extend 1fcsfl " Ugh."
                n 1cllsl "Como sea."
            else:

                n 1csrfl "Yo...{w=1}{nw}"
                extend 1ccsfl " creo que ese debió haberse {i}quedado{/i} en el libro,{w=0.5}{nw}"
                extend 1csqcasbl " [player]."
                n 1csrcasbl "..."

            n 1nlraj "Así que..."
            show natsuki 1tnmbo

        elif joke_choice.joke_category == jn_jokes.JNJokeCategories.bad:
            if dialogue_choice == 1:
                n 1ccsemesi "..."
                n 1clrfl "Muy bien.{w=0.75}{nw}"
                extend 1clrca " Ese está lidiado.{w=0.75}{nw}"
                extend 1csrca " {i}Otra vez{/i}."

            elif dialogue_choice == 2:
                n 1ccsflesi "..."
                n 1cllfl "Sí.{w=0.75}{nw}"
                extend 1cllsl " Ese envejeció casi tan bien como esperaba.{w=1}{nw}"
                extend 1cslpo " {i}Como basura{/i}."
            else:

                n 1ccssssbl "Heh.{w=0.75}{nw}"
                extend 1ccstr " Supongo que al menos {i}algunas{/i} cosas no cambian.{w=0.75}{nw}"
                extend 1csrbo " {i}Como ese chiste todavía apestando{/i}."

            n 1ccsajsbl "Bueno,{w=0.2} como sea.{w=0.75}{nw}"
            extend 1nllaj " Así que..."
            show natsuki 1tnmsl

        elif joke_choice.joke_category == jn_jokes.JNJokeCategories.confusing:
            if dialogue_choice == 1:
                n 1cslfl "...Sí.{w=0.75}{nw}"
                extend 1cslaj " Tiene tanto sentido para mí como lo hizo antes."
                n 1csrsl "{i}No mucho{/i}."

            elif dialogue_choice == 2:
                n 1csrsl "..."
                n 1ccsajsbl "Bueno,{w=0.5}{nw}"
                extend 1cllflsbl " tengo que admitir.{w=0.75}{nw}"
                extend 1cdwflsbl " Todavía no tengo idea de para quién se supone que es {i}ese{/i} chiste."
                n 1csrbosbl "..."
            else:

                n 1ccsaj "Uh huh.{w=0.75}{nw}"
                extend 1ccsbg " ¡Sip!"
                n 1cllflsbr "...Todavía no tengo idea de qué es todo el alboroto con{w=0.75}{nw}"
                extend 1cslflsbr " {i}ese{/i}."
                n 1cslbosbr "..."

            n 1ccsajsbr "B-{w=0.2}bueno,{w=0.2} como sea."
            show natsuki 1tnmca
        else:

            if dialogue_choice == 1:
                n 1fcssmeme "Ehehe.{w=0.75}{nw}"
                extend 1fchbg " ¡Ahí lo tienes,{w=0.2} [player]!"

            elif dialogue_choice == 2:
                n 1fnmbg "...¡Y ahí lo tienes,{w=0.2} [player]!{w=0.75}{nw}"
                extend 1fcssmesm " ¡Mejor aprécialo!"
            else:

                n 1fwrsm "...¡Y eso es todo lo que ella escribió!{w=0.75}{nw}"
                extend 1fchsm " Ehehe."

            n 1ulraj "Así que..."
            show natsuki 1unmbo

        menu:
            n "¿Querías elegir otro [player],{w=0.2} o...?"
            "¡Seguro!":

                if joke_choice.joke_category == jn_jokes.JNJokeCategories.corny or joke_choice.joke_category == jn_jokes.JNJokeCategories.bad:
                    n 1nlrsl "...Muy bien.{w=0.75}{nw}"
                    extend 1csrsssbl " Solo trata de elegir uno bueno esta vez."

                elif joke_choice.joke_category == jn_jokes.JNJokeCategories.confusing:
                    n 1unmbo "'Kay.{w=0.75}{nw}"
                    extend 1tsqbosbl " Solo elige uno normal esta vez."
                else:

                    n 1nchbg "¡Entendido!{w=0.75}{nw}"
                    extend 1tnmss " ¿Qué más querías escuchar de nuevo?"

                jump talk_daily_jokes_seen_before_loop
            "Eso es todo por ahora":

                if joke_choice.joke_category == jn_jokes.JNJokeCategories.funny:
                    n 1fcsss "¿Oh?{w=0.75}{nw}"
                    extend 1fsqss " ¿Qué pasa,{w=0.2} [player]?{w=0.75}{nw}"
                    extend 1fnmsm " ¿Tuviste suficiente {i}ya{/i}?"
                    n 1fcssm "Ehehe."
                    n 1fcsbg "Bien,{w=0.2} bien.{w=0.75}{nw}"
                    extend 1flrsm " Lo guardaré..."
                    n 1fsqcs "...Ahora que hemos tenido suficiente{w=0.5}{nw}"
                    extend 1fnmss " {i}diversión{/i}{w=0.5}{nw}"
                    extend 1fsqbg " y todo."
                    n 1nchgn "Ahaha.{w=0.75}{nw}"

                    if Natsuki.isLove(higher=True):
                        extend 1fchbll " ¡Te amo también,{w=0.2} [player]~!"
                    else:

                        extend 1fcsbs " ¡Sin arrepentimientos,{w=0.2} [player]!"

                    show natsuki 1fchsmeme

                elif joke_choice.joke_category == jn_jokes.JNJokeCategories.corny or joke_choice.joke_category == jn_jokes.JNJokeCategories.confusing:
                    n 1ncsss "Heh.{w=0.75}{nw}"
                    extend 1ulrfl " Bueno...{w=1}{nw}"
                    extend 1nslsssbl " no puedo decir que te culpe,{w=0.2} [player]."
                    n 1nllsssbr "Solo voy a...{w=0.75}{nw}"
                    extend 1nslbosbr " guardar esto."

                    show natsuki 1nlrbosbl

                elif joke_choice.joke_category == jn_jokes.JNJokeCategories.bad:
                    n 1nslfl "...Sí.{w=0.75}{nw}"
                    extend 1ccsfl " De hecho,{w=0.2} ¿sabes qué?{w=0.75}{nw}"
                    extend 1cnmaj " Buena llamada."
                    n 1ccsposbr "He tenido suficiente de esto de todos modos."

                    show natsuki 1nsrposbr
                else:

                    n 1unmaj "¿Casi terminamos aquí,{w=0.2} [player]?{w=0.75}{nw}"
                    extend 1nchsm " ¡No hay problema!"
                    n 1clrss "Solo vamos a...{w=1}{nw}"
                    extend 1csqss " {i}cerrar el libro{/i}{w=0.5}{nw}"
                    extend 1csqbg " en esto."

                    if Natsuki.isLove(higher=True):
                        n 1fchgn "Ehehe.{w=0.75}{nw}"
                        extend 1fchblleme " ¡Te amo también,{w=0.2} [player]~!"
                    else:

                        n 1fchgnelg "¡De nada,{w=0.2} [player]!"

                    show natsuki 1fchsmeme
    else:

        n 1tlraj "Bueno...{w=1}{nw}"
        extend 1tnmbo " si tú lo dices,{w=0.2} [player]."
        n 1tllss "Solo voy a...{w=1}{nw}"
        extend 1cslss " poner esta cosa de vuelta."

        show natsuki 1nslbo

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_fitting_clothing",
            unlocked=True,
            prompt="Problemas con la ropa",
            category=["Moda"],
            conditional="persistent.jn_custom_outfits_unlocked",
            affinity_range=(jn_affinity.AFFECTIONATE, None),
            nat_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_fitting_clothing:
    n 2cllbo "..."
    n 2cllfl "Sabes,{w=0.2} [player]..."
    n 2tnmbo "No recuerdo siempre haberme quejado sobre mi altura tanto.{w=0.75}{nw}"
    extend 4nsrss "\nNo {i}realmente{/i}."
    n 4ulraj "Digo...{w=1}{nw}"
    extend 3clrsl " siempre me pareció inútil ponerse toda alterada sobre eso.{w=0.75}{nw}"
    extend 3nsrposbr " No es como si alguna vez fuera a ser alta {i}eventualmente{/i}."
    n 4csrca "...Especialmente no ahora."
    n 1ulraj "Pero...{w=1}{nw}"
    extend 1unmaj " supongo que solo me di cuenta de ello que es como mis dientes,{w=0.75}{nw}"
    extend 2nnmbo " o mi cabello o lo que sea."
    n 2fcstr "Solo tienes que aprovecharlo al máximo.{w=1}{nw}"
    extend 4fcsgsl " ¿Y-{w=0.2}y por qué no debería?{w=0.75}{nw}"
    extend 3fcsbgl " ¡Estoy totalmente luciendo lo que tengo!"

    n 1csqsl "Pero{w=0.3} Oh.{w=0.75} Por.{w=0.75} Dios,{w=0.75}{nw}"
    extend 2csrem " [player]."
    n 2fsqem "Comprar ropa.{w=1}{nw}"
    extend 1fcsan " Lo juro.{w=1}{nw}"
    extend 4fbkwr " ¡Es como mi propio infierno especial!"
    n 4fcswrl "¡¿Siquiera has {i}considerado{/i} cómo es conseguir ropa nueva cuando eres así de pequeña?!"
    n 2fllfll "En serio -{w=0.5}{nw}"
    extend 2fbkwrl " ¡es lo peor!{w=1}{nw}"
    extend 2fcsgs " ¡Y ni siquiera importa a dónde vayas!"
    n 4ftlfl "¿Mediano?{w=0.5}{nw}"
    extend 4ftrfl " ¿Pequeño?{w=0.5}{nw}"
    extend 2fsqem " ¿{i}Extra{/i} Pequeño?{w=0.75}{nw}"
    extend 2fcsgs " ¡Como si importara!"
    n 1fslem "Esas no son tallas -{w=0.5}{nw}"
    extend 4fcsan " ¡solo estoy eligiendo qué tanto de {b}chiste{/b} es el ajuste!"
    n 1flrfl "Sí,{w=0.2} claro.{w=0.75}{nw}"
    extend 4flrca " {i}Sé{/i} que oversize es una cosa.{w=1}{nw}"
    extend 2fsrtr " Obviamente."
    n 2flrgs "¡Pero v-{w=0.3}{nw}"
    extend 2fcsgs "{b}vamos{/b}!"
    n 4ksqfl "¿Es {i}realmente{/i} mucho querer mangas que {i}no{/i} cuelguen de mis brazos también?"
    n 1fllfl "Digo,{w=0.2} la mitad del tiempo que caminaba a revisar la ropa de adultos,{w=0.75}{nw}"
    extend 1fnmem " ¡tendría que caminar directo de vuelta afuera otra vez!"
    n 2fsrsl "...Y solo hay tantas veces que puedes intentar la sección de niños antes de que la gente empiece a darte miradas estúpidas."

    n 2fcsemesi "Ugh..."
    n 1cslbo "Es simplemente vergonzoso.{w=1}{nw}"
    extend 4fslsl " Y usualmente una {i}completa{/i} pérdida de tiempo también."
    n 4cllfl "Entiendo que algunos lugares hacen una...{w=0.75}{nw}"
    extend 1cslflsbr " línea{w=0.75}{nw}"
    extend 1cslcasbr " {i}petite{/i},{w=0.75}{nw}"
    extend 2fcswrsbr " ¡pero todo es todavía {i}igual{/i} de caro que las cosas normales!"
    n 2fcsem "Cielos..."
    n 4fllem "Ni siquiera usan tanto material.{w=1}{nw}"
    extend 4ftlem " Deberían al menos incluir un descuento o algo."
    n 2fsrfl " ...{i}Idiotas{/i}."
    n 2nsrpo "..."
    n 2ncstr "Bueno,{w=0.2} como sea.{w=0.75}{nw}"
    extend 1fnmca " Las tiendas pueden estar cortas de opciones.{w=0.75}{nw}"
    extend 1fsrca " Y {i}cortesía{/i}."
    n 3fcsaj "Pero puedo asegurarte:{w=0.5}{nw}"
    extend 3fcsbg " ¡mi imaginación {i}nunca{/i} se queda corta!"

    $ pastel_goth_getup = jn_outfits.getOutfit("jn_pastel_goth_getup")
    if not pastel_goth_getup.unlocked:
        python:
            import copy

            pastel_goth_getup.unlock()
            topic_outfit = copy.copy(pastel_goth_getup)
            topic_outfit.hairstyle = jn_outfits.getOutfit(Natsuki.getOutfitName()).hairstyle

        n 3fllpu "..."
        n 3fllss "...De hecho.{w=1}{nw}"
        extend 4fsqss " ¿Sabes qué?"
        n 2fcsbg "Olvida solo divagar sobre eso.{w=0.75}{nw}"
        extend 2fcssm " Deberías saber que soy mucho mejor que eso por ahora."
        n 4fchgn "...¡Así que voy a {i}probarlo{/i}!"
        n 3fcsbgsbl "S-{w=0.2}será mejor que te quedes quieto,{w=0.2} [player]..."
        n 3fchgn "¡Porque voy a mostrarte cómo se ve la artesanía {i}real{/i}!{w=0.75}{nw}"
        extend 3nchgn " Ehehe."
        show natsuki 1fcssmeme

        show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
        $ jnPause(0.5)
        play audio chair_out
        $ jnPause(3)

        n "Bien...{w=1}{nw}"
        extend " ahora dónde..."
        n "¡Ajá!"

        play audio drawer
        $ jnPause(3)
        play audio clothing_ruffle
        $ jnPause(1)

        if Natsuki.isLove(higher=True):
            n "¡N-{w=0.2}no mires!{w=0.75} Ehehe..."

        elif Natsuki.isEnamored(higher=True):
            n "¡N-{w=0.2}no mires!"
        else:

            n "¡H-{w=0.2}hey!{w=0.75} ¡Será mejor que no estés mirando!"

        $ jnPause(1)
        play audio zipper
        $ Natsuki.setOutfit(outfit=topic_outfit, persist=False)

        show natsuki 2fsrdvlsbl
        $ jnPause(2)
        n "Y..."
        play audio chair_in
        $ jnPause(0.25)
        hide black with Dissolve(1.5)
        $ jnPause(1.5)

        n 2fchbglsbl "¡Ta-da!"
        n 2csqsm "¿Puedes adivinar de dónde vino {i}esto{/i},{w=0.2} [player]?{w=0.75}{nw}"
        extend 1fcssm " Ehehe."
        n 4fslss "Por mucho que me quejé sobre recurrir a la sección de niños..."
    else:

        n 4ullaj "Estoy bastante segura de que ya presumí mi obra antes,{w=0.75}{nw}"
        extend 1fcsbg " así que te ahorraré el show de moda,{w=0.2} [player]."
        n 3fsqsm "...Esta vez."
        n 3tnmss "Aunque como dije antes -{w=0.5}{nw}"
        extend 4fslss " por mucho que me quejé sobre recurrir a la sección de niños..."

    n 3fcsbg "¡No hay nada que un poco de buen conocimiento a la antigua,{w=0.2} una aguja,{w=0.75}{nw}"
    extend 3fchgn " y un montón de mis parches no puedan arreglar!{w=1}{nw}"
    extend 3nchgn " Ahaha."

    n 4clrss "Bueno,{w=0.2} como sea.{w=0.75}{nw}"
    extend 2csrsmsbl " Creo que ya he hablado suficiente.{w=1}{nw}"
    extend 2fcsajsbl " Por bien que se sintiera sacar todo eso de mi pecho."
    n 1fcsss "Heh.{w=0.75}{nw}"
    extend 4cslbg " Además,{w=0.2} ¿toda esta plática sobre cosas nunca siendo de la talla correcta?"
    n 4fnmss "Supongo que podrías decir que seguir adelante es solo...{w=1}{nw}"
    extend 3fsqbg " {i}apropiado{/i}{w=1}{nw}"
    extend 3fchgn ",{w=0.2} ¿verdad?"

    if Natsuki.isLove(higher=True):
        n 3fchsm "Ehehe.{w=0.5}{nw}"
        extend 3fchbll " ¡Te amo también,{w=0.2} [player]!"
    else:

        n 3fchsm "Ehehe.{w=0.5}{nw}"
        extend 3uchgn " ¡Sin arrepentimientos,{w=0.2} [player]!"

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_favorite_subject",
            unlocked=True,
            prompt="¿Cuál es tu materia favorita?",
            category=["Educación"],
            conditional="jn_utils.get_total_gameplay_hours() >= 2",
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_favorite_subject:
    $ already_discussed_topic = get_topic("talk_favorite_subject").shown_count > 0

    if Natsuki.isNormal(higher=True):
        if already_discussed_topic:
            n 2ccsbo "...Espera.{w=0.75}{nw}"
            extend 2tnmpu " ¿No pasamos por esto ya,{w=0.2} [player]?{w=1}{nw}"
            extend 2clrbo " Huh."
            n 1clraj "Bueno,{w=0.2} como sea.{w=0.75}{nw}"
            extend 4tllaj " No es como si mucho hubiera cambiado.{w=1}{nw}"
            extend 2cslem " ¡{i}Todavía{/i} no puedo con matemáticas!"
        else:

            n 2cslem "No {i}matemáticas{/i},{w=0.5}{nw}"
            extend 2fsrfl " te diré eso."
            n 1nsrsl "..."
            n 1cllslsbr "..."
            n 4cnmflsbr "...¿Qué?{w=0.75}{nw}"
            extend 4fllgs " ¡Hablo en serio!{w=0.75}{nw}"
            extend 2fbkwr " ¡Simplemente no puedo soportarlas!"

        n 2fcsgs "Digo,{w=0.2} entiendo totalmente todas las cosas normales.{w=0.75}{nw}"
        extend 4flrfl " Suma,{w=0.2} resta,{w=0.2} fracciones.{w=0.5}{nw}"
        extend 1fcsca " Eso es juego de niños.{w=0.75}{nw}"
        extend 2clrca " Realmente no me importa {i}eso{/i}."
        n 1fcsfl "Es solo que..."
        n 4fsrun "..."
        n 4fcswr "¡Es cuando obtienes todas esas reglas {i}estúpidas{/i} que tienes que recordar!{w=0.75}{nw}"
        extend 2fbkwr " ¡Simplemente hay demasiadas de ellas!"
        n 2fllwr "Como...{w=1}{nw}"
        extend 2fcsgs " ¿cómo se supone que {i}yo{/i} recuerde tres sabores diferentes de balbuceo para calcular alguna parte aleatoria de un triángulo?"
        n 2flran "¿Qué voy a hacer siquiera {i}con{/i} eso?{w=0.75}{nw}"
        extend 1fsrwr " ¡¿Medir la rebanada de pizza perfecta?!{w=0.75}{nw}"
        extend 2fcsem " Vamos."
        n 4fcsan "Y ni siquiera me hagas {i}empezar{/i} en cálculo...{w=1}{nw}"
        extend 2fslsl " o {i}álgebra{/i}."
        n 2fsqem "Y yo {i}realmente{/i} odiaba tener que pasar mis noches estudiando eso como loca antes de{w=0.25}{nw}"
        extend 2fcsan " cada{w=0.3} maldito{w=0.3}{nw}"
        extend 2fsran " examen."
        n 4fcsan "Es..."
        n 1csrsl "..."
        n 1ccsflsbr "...Simplemente no es como funciona mi cerebro.{w=0.75}{nw}"
        extend 4cslbolsbr " Para nada."
        n 4fcsgslsbr "P-{w=0.2}pero eso no es decir que nadie ayudaría ni nada como eso!{w=0.75}{nw}"
        extend 2fllflsbr " Monika siempre seguía tratando de ofrecer cuando tenía el tiempo.{w=0.75}{nw}"
        extend 2cllbo " Pero..."
        n 1kllbo "..."

        if Natsuki.isAffectionate(higher=True):
            n 2csrbolsbr "...Es vergonzoso.{w=0.75}{nw}"
            extend 2knmbolsbr " ¿Sabes?{w=0.75}{nw}"
            extend 4fcsfl " Y por mucho que no soporte la materia..."
            n 1cslbol "...No es como si {i}no{/i} quisiera ser buena en ella también."

            if Natsuki.isEnamored(higher=True):
                n 1cslcal "I-{w=0.2}incluso si es solo para poder {i}decir{/i} que puedo hacerlo."
                n 4cslunl "..."
            else:

                n 1fcstrlsbr "Justo como todo lo demás."
                n 4cllsllsbr "..."

            n 2ccsfllsbr "C-{w=0.2}como sea!{w=0.75}{nw}"
            extend 4fcspo " Nos estamos desviando aquí."
            n 4tllpu "Materia favorita,{w=0.5}{nw}"
            extend 3tnmss " ¿eh?"
            n 3csqsm "Ehehe.{w=0.75}{nw}"
            extend 4fsqbg " ¿Realmente necesitas preguntar?{w=0.75}{nw}"

            if already_discussed_topic:
                extend 2fcsbg " ¿No habías adivinado {i}ya{/i},{w=0.2} [player]?"
            else:

                extend 2fcsbg " ¿En serio no recuerdas,{w=0.2} [player]?"
        else:

            n 1ccsfllsbl "...Olvídalo.{w=0.75}{nw}"
            extend 2csrcalsbl " No importa."
            n 2fcsajlsbl "Y-{w=0.2}y además.{w=0.75}{nw}"
            extend 2fcspo " Esto ya se estaba desviando demasiado."
            n 4unmaj "Materia favorita,{w=0.5}{nw}"
            extend 4tnmbo " ¿eh?"
            n 2ccsss "Je.{w=1}{nw}"

            if already_discussed_topic:
                extend 2fcsbg " ¿Realmente no recuerdas,{w=0.2} [player]?"
            else:

                extend 2fcsbg " Como si la respuesta ya no te hubiera prácticamente golpeado en la cara."

        n 4uchgn "...Literatura,{w=0.75}{nw}"
        extend 3fchgn " ¡duh!"
        n 3fsqsm "No creíste en serio que solo saqué mi poesía de la nada o algo,{w=0.5}{nw}"
        extend 3fsqbg " ¿verdad?{w=0.75}{nw}"
        extend 3fchgn " ¡Nop!"
        n 4fllss "Digo,{w=0.75}{nw}"
        extend 1fcsss " {i}Soy{/i} una natural..."
        n 2fcstr "...Pero solo te estás engañando a ti mismo si piensas que puedes salirte con la tuya sin poner esfuerzo actual también."
        n 2tllaj "De verdad aunque -{w=0.5}{nw}"
        extend 1tnmfl " ¿cómo podría a alguien desagradarle algo con tanta variedad?{w=0.75}{nw}"
        extend 4fspgs " ¡La literatura es {b}asombrosa{/b}!"
        n 4fcsbg "Historias épicas...{w=0.75}{nw}"
        extend 4unmfl " experiencias que cambian la vida...{w=0.75}{nw}"
        extend 4clrss " cualquier cosa y todo lo que pudieras {i}posiblemente{/i} imaginar..."
        n 2tsqfl "...¿Y todo lo que tengo que hacer es pasar las páginas?{w=0.75}{nw}"
        extend 4fchgn " ¡Apúntame!"
        n 2flrss "Probablemente te he llamado eso un montón antes ya,{w=0.2} [player]."
        n 2fsqsm "...Pero solo un {i}verdadero{/i} tonto {i}pasaría{/i} de una oferta así de buena.{w=0.75}{nw}"
        extend 2fcssm " Ehehe."
        n 4ulraj "Bueno,{w=0.2} como sea.{w=0.75}{nw}"
        extend 2tlrbo " Creo que he seguido sobre eso suficiente tiempo.{w=0.75}{nw}"
        extend 2tsqfl " ¿Quién quiere pasar todo el día hablando sobre cursos y temas de todas las cosas?"

        if Natsuki.isLove(higher=True):
            n 4ccsbgl "Además,{w=0.2} [player]."
            n 3fcsbgl "No reconoces un tema mucho más interesante..."
            n 3fsqssl "...¿Cuando ya está sentado justo en frente de ti?{w=0.75}{nw}"
            extend 3fsldvlsbr " Ehehe."
            $ chosen_tease = jn_utils.getRandomTease()
            n 1fchbgfsbr "¡T-{w=0.2}te amo también,{w=0.2} [chosen_tease]!"

        elif Natsuki.isEnamored(higher=True):
            n 4fcsssl "Además..."
            n 3fcsbglsbr "N-{w=0.2}no tienes algo {i}mucho{/i} más interesante en frente de ti de lo que deberías estar aprendiendo en su lugar?{w=0.75}{nw}"
            extend 1fslsslsbr " Ehehe..."
        else:

            n 4csqbg "De hecho..."
            n 4fcsss "Supongo que podrías decir que ya era hora de que...{w=0.75}{nw}"
            extend 3fsqbg " {i}cambiáramos el tema{/i}{w=0.75}{nw}"
            extend 3fchgn ",{w=0.2} ¿verdad?"
            n 1nchgn "Ehehe."

    elif Natsuki.isDistressed(higher=True):
        if already_discussed_topic:
            n 4fcsan "...¿En serio?{w=0.75}{nw}"
            extend 4fsqan " ¿Me estás diciendo que ni siquiera estabas {i}escuchando{/i} la primera vez?"
            n 1fcsfr "..."
            n 2fcsem "...Como sea.{w=0.75}{nw}"
            extend 2fslem " No me importa."
            n 2fslsl "Todavía no soporto las matemáticas."
        else:

            n 2fcssl "..."
            n 2fslsl "...Supongo que al menos puedo decirte lo que {i}no{/i} me gusta.{w=1}{nw}"
            extend 2fcsfl " Matemáticas."

        n 4fsqfl "...Y no,{w=0.2} no porque sea simplemente inútil en ellas o algo estúpido como eso.{w=1}{nw}"
        extend 4fsrem " {i}A pesar{/i} de lo que probablemente pienses."
        n 1fcsem "Es solo que...{w=1}{nw}"
        extend 2fcsfl " es demasiado complicado."
        extend 2fllan " ¡Es ridículo!"
        n 2fcsan " ¿Cómo se supone que {i}alguien{/i} recuerde tantas tonterías aleatorias?{w=0.75}{nw}"
        extend 1flrem " Especialmente alrededor de exámenes."
        n 2fupfl "Porque nada me hace {i}amar{/i} una materia más que tener que vivir para ella{w=0.5}{nw}"
        extend 4fcsan " cada{w=0.3} maldita{w=0.3} vez{w=0.3}{nw}"
        extend 4fslan " que un examen aparece."
        n 1fcssl "..."
        n 4fcsfl "Yo...{w=0.75}{nw}"
        extend 2fsran " entiendo...{w=0.75}{nw}"
        extend 2fsrsr " que pude haber solo pedido ayuda.{w=1}{nw}"
        extend 2fsqem " De mis {w=0.2}{i}amigos{/i}{w=0.3}, como sea."
        n 1clrsl "Pero ese no es el punto."
        n 2csrsl "A veces solo quieres hacer cosas por ti misma.{w=1}{nw}"
        extend 2fsrfr " No {i}necesitar{/i} depender de alguien más constantemente.{w=1.25}{nw}"
        extend 2fnmfl " ¿Y sabes qué?"
        n 1fllfl "¿Por qué no?{w=0.75}{nw}"
        extend 1fslan " Además..."
        n 4fslem "No es como si siempre fuera a haber {i}alguien{/i} en quien puedas confiar."
        n 2fllem "...¿Verdad,{w=0.75}{nw}"
        extend 2fsqem " {i}[player]{/i}?"
    else:

        if already_discussed_topic:
            n 2fslan "Tú {i}seriamente{/i} piensas que vas a obtener una respuesta diferente..."
            n 2fsqan "...¿Si solo preguntas {i}otra vez{/i}?{w=0.75}{nw}"
            extend 2fnmup " ¿Acaso {b}parece{/b} que nací ayer?"
            n 4fnman "...¿Y por qué exactamente debería decirte a {i}ti{/i},{w=0.2} de todos modos?"
        else:

            n 2fsqan "...¿En serio?{w=0.75}{nw}"
            extend 2fsqfl " ¿Mi materia favorita?"
            n 4fnman "...¿Y por qué exactamente debería decirte a {i}ti{/i}?"

        n 4fsqfutsb "¿Para que puedas empezar a sermonearme sobre ello?"
        n 2fcssltsa "Heh.{w=1}{nw}"
        extend 2fcsemtsa " Sí.{w=1}{nw}"
        extend 2fsqantsb " {i}No gracias{/i}."
        n 4fsqupltsb "Ahora {i}sal de mi vista{/i}."

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_can_you_draw",
            unlocked=True,
            prompt="¿Sabes dibujar?",
            category=["Arte"],
            conditional="jn_utils.get_total_gameplay_hours() >= 6",
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_can_you_draw:
    $ already_discussed_topic = get_topic("talk_can_you_draw").shown_count > 0

    if Natsuki.isNormal(higher=True):
        if already_discussed_topic:
            n 2ccsbo "Espera...{w=1}{nw}"
            extend 2tnmpu " ¿dibujar?{w=0.75}{nw}"
            extend 2fsrpu " Juraría que hablamos de esto antes,{w=0.2} [player]...{w=1}{nw}"
            extend 4ncsbo " huh."
            n 4nllaj "Bueno,{w=0.2} como sea."
            n 4fslpo "Todavía estoy medio molesta sobre cómo mi escuela manejó las clases de arte."
            n 2nnmaj "Como sí,{w=0.2} las tuvimos...{w=1}{nw}"
            extend 2fsrbo " pero no fueron exactamente súper a fondo ni nada.{w=0.75}{nw}"
        else:

            n 4tnmaj "¿Huh?{w=0.75}{nw}"
            extend 4cllbo " ¿Si sé dibujar?{w=0.75}{nw}"
            extend 1tslpu " Como...{w=0.3} retratos,{w=0.2} paisajes,{w=0.5}{nw}"
            extend 2tnmaj " ¿ese tipo de cosas?"
            n 2ccsss "Je.{w=0.75}{nw}"
            extend 2cslaj " ¡Ojalá!{w=0.75}{nw}"
            extend 2fsqbo " Y créeme -{w=0.5}{nw}"
            extend 4fcsss " sabrías sobre ello si tuviera {i}esa{/i} clase de talento."
            n 1nnmaj "Digo,{w=0.2} ¿siquiera has {i}visto{/i} la clase de cosas que la gente publica en línea ahora?"
            n 4uspgs "¡Es una locura!{w=0.75}{nw}"
            extend 3nlrss " ¡No tengo idea de cómo lo hacen!"
            n 1csrbo "...O siquiera por dónde empiezan,{w=0.2} para el caso."
            n 2nnmaj "Tuvimos clase de arte durante la escuela,{w=0.5}{nw}"
            extend 2fslpo " obviamente.{w=0.75}{nw}"
            extend 2cnmaj " Pero realmente no fue súper a fondo ni nada.{w=0.75}{nw}"

        extend 2fcsaj " Como...{w=0.3} para nada."
        n 4clrpu "De hecho.{w=0.75}{nw}"
        extend 1csrbo " entre más lo pienso..."
        n 2fcswr "¡Apenas y {i}calificó{/i} como clase de arte del todo!{w=0.75}{nw}"
        extend 2fllgs " ¡Se sintió como que apenas sacamos el lienzo!"
        n 2fcsan "Lo juro -{w=0.5}{nw}"
        extend 1csraj " demasiadas lecciones fueron solo un ejercicio de pasar páginas más que {i}pintar{/i}."
        n 4ctrpu "Entiendo que el arte tiene mucha historia detrás.{w=0.75}{nw}"
        extend 4csrfl " Y por supuesto hay toneladas de estilos allá afuera que aprender.{w=0.75}{nw}"
        extend 4fcssl " Lo entiendo."
        n 1flrgs "Pero va{w=0.5}{nw}"
        extend 2fcsgs " {b}mos{/b}!{w=1}{nw}"
        extend 2fslup " Cuál es siquiera el punto en estudiar tanto sobre todos esos artistas y estilos diferentes..."
        n 4fsqem "...¿Si apenas tuvimos el tiempo de cubrir cualquiera de lo básico?{w=0.75}{nw}"
        extend 4fcsup " ¡Mucho menos intentar cualquiera de las cosas que estudiamos!"
        n 2cslem "Y-{w=0.2}y además!{w=0.75}{nw}"
        extend 2fslem " Todos esos artistas ya tuvieron su turno.{w=0.75}{nw}"
        extend 4fcsgs " ¡Yo quiero crear cosas geniales también!"
        n 1fcsemesi "Ugh..."
        n 2csrflsbl "Creerías que la única vez que quieren incentivar la creatividad sería cuando le darían un descanso a los libros de texto."
        n 2ccssl "..."
        n 2clrpu "Supongo que no habría sido tan malo si pudiera haber practicado fuera de la escuela.{w=0.5}{nw}"
        extend 2tlrbo " Como en casa o lo que sea.{w=0.75}{nw}"
        extend 4unmpu " ¡O tal vez incluso el club de arte!"
        n 1nslss "Je."
        n 4nslslsbr "No hay premios por adivinar por qué ninguna de esas iba a funcionar."
        n 4ccsajsbr "Poniendo todo eso de lado.{w=0.75}{nw}"
        extend 1unmaj " ¿Honestamente?"
        n 3csrpul "No es que no quisiera ser capaz de dibujar cosas geniales.{w=0.75}{nw}"
        extend 3tnmaj " ¿Estás bromeando?{w=0.75}{nw}"
        extend 4fchgn " ¡Eso sería asombroso!"

        if Natsuki.isAffectionate(higher=True):
            n 2csrpusbl "Es solo que..."
            n 2ksrbol "..."
            n 2fcspul "Es...{w=1}{nw}"
            extend 1cslpu " intimidante.{w=1}{nw}"
            extend 2ksqsl " Tratar de enseñarte a ti misma algo como eso."
            n 2cllaj "Está bien si siempre has estado dibujando,{w=0.2} o tienes algún tipo de maestro."
            n 2cnmbol "...¿Pero qué tal si no {i}tienes{/i} esa clase de dirección en ningún lado?"

            if Natsuki.isEnamored(higher=True):
                n 2ccsajl "La gente siempre dice que solo se reduce a práctica,{w=0.75}{nw}"
                extend 2fsrsllsbl " o buscar algún curso aleatorio en línea o lo que sea.{w=0.75}{nw}"
                extend 2fnmflsbl " Y-{w=0.2}y no estoy diciendo que estén mal!"
                n 2fcsposbr "Eso es solo ser ignorante."
                n 2fcsajsbr "Todos tienen su propio enfoque,{w=0.2} obviamente.{w=1}{nw}"
                extend 2cslslsbr " Pero..."
                n 2kslbolsbr "...Supongo que yo nunca encontré el mío.{w=1.25}{nw}"
                extend 4ccsssl " No {i}aún{/i},{w=0.2} como sea."
                n 2ulrpu "Aunque...{w=1}{nw}"
                extend 4unmbo " ¿qué hay de ti,{w=0.2} [player]?"
            else:

                n 2ncspuesi "..."
                n 2csrbo "No lo sé."
                n 2ksrbosbr "..."
                n 4fcsajlsbl "C-{w=0.2}como sea!{w=0.75}{nw}"
                extend 2ccsca " Estoy un poco aburrida de escucharme a mí misma ahora.{w=0.75}{nw}"
                extend 2tnmbo " Así que qué hay de ti,{w=0.2} [player]?"
        else:

            n 2clrca "Pero...{w=1}{nw}"
            extend 2ksrpu " eso es..."
            n 1fcsbo "..."
            n 1fcscalsbr "O-{w=0.2}olvídalo."
            extend 1cllsll " Supongo que ni siquiera importa ahora de todas formas."
            n 4fcsajsbl "Además.{w=0.2} Creo que ya terminé de escucharme hablar por ahora."
            n 4nlraj "Así que...{w=0.75}{nw}"
            extend 4unmbo " ¿qué hay de ti,{w=0.2} [player]?"

        if jn_activity.ACTIVITY_MANAGER.hasPlayerDoneActivity(jn_activity.JNActivities.artwork):
            n 4fwdaw "...¡Espera!{w=0.75}{nw}"
            extend 3fcsbg " ¡No me digas!{w=0.75}{nw}"
            extend 3fcsbs " Tengo una muy buena corazonada para este tipo de cosas{w=0.5}{nw}"
            extend 3fsqss " si lo digo yo misma."
            n 3fcssm "Ehehe."
            n 4fcsbg "¡Sip!"
            n 4fsqsmeme "Tienes 'artista' escrito por todo tú."
            n 3fsqsssbr "Razón de más para estar agradecido de que siempre tienes {i}tal{/i} gran sujeto a la mano,{w=0.5}{nw}"
            extend 3fcsbgsbr " ¿tengo razón?"
        else:

            show n 4tnmbo
            menu:
                n "¿Dibujas mucho,{w=0.2} o...?"
                "¡Sí, dibujo seguido!":

                    n 4fsqcs "¿Oh?{w=0.75}{nw}"
                    extend 3fsqss " Te consideras un artista,{w=0.2} ¿eh?"
                    n 3fcssm "Ehehe."
                    n 3fllss "Bueno,{w=0.5}{nw}"
                    extend 3fsqcs " será mejor que te consideres afortunado,{w=0.2} [player].{w=0.75}{nw}"
                    extend 3fcsbgsbr " ¡No todos los días un sujeto tan {i}asombroso{/i} simplemente se planta justo enfrente de ti!"
                "No, usualmente no dibujo":

                    n 3tnmsl "¿En serio?{w=0.75}{nw}"
                    extend 3cslca " Aww..."
                    n 3ullaj "Lo admitiré,{w=0.2} estoy un poco decepcionada.{w=1}{nw}"
                    extend 4tllbo " Aunque lo entiendo.{w=0.75}{nw}"
                    extend 2cslsssbr " No es como si {i}yo{/i} fuera alguien para juzgar por eso."
                    extend 4fsqsm " Aún."
                "Ya no dibujo":

                    n 3kslpu "Aww..."
                    n 3tslbo "..."
                    n 3ccsfl "...Espera.{w=0.2} ¿'Ya no'?{w=0.75}{nw}"
                    extend 3csqem " ¿Qué quieres decir con,{w=0.2} {i}'ya no'{/i}?{w=0.5}{nw}"
                    extend 3fcsgs " ¡Tienes que volver a ello,{w=0.2} [player]!"
                    n 3tnmaj "¿Por qué no?{w=0.75}{nw}"
                    extend 3fcsbgsbr " ¡{i}Especialmente{/i} cuando has sido bendecido con {i}tal{/i} buen sujeto para empezar!{w=0.75}{nw}"
                    extend 3fcssmsbr " Ehehe."

        n 1ullaj "Bueno como sea.{w=0.75}{nw}"
        extend 2ccsaj " ¿Sabes qué?{w=0.75}{nw}"
        extend 2fcsbg " ¿Quién dice que no podría aprender a dibujar en algún punto?"
        n 2utraj "Tiene que haber algunos suministros de arte que pueda robar de algún lugar por aquí."
        n 2nsrsssbl "No es como que el club de arte vaya a necesitarlos ahora.{w=0.75}{nw}"
        extend 1tsqss " ¿Y quién sabe,{w=0.2} [player]?"
        n 3fcscsesm "¡Apuesto a que hay un Picasso en mí aún!"
        n 3fnmbg "¡Solo tengo que{w=0.5}{nw}"
        extend 3fsqbg " {i}facili-tar{/i}{w=0.5}{nw}"
        extend 3fchgn " las cosas primero!{w=0.75}{nw}"
        extend 3nchgn " Ehehe."

        if Natsuki.isLove(higher=True):
            n 3fchbll "¡Te amo también,{w=0.2} [player]~!"

    elif Natsuki.isDistressed(higher=True):
        if already_discussed_topic:
            n 2fcsemesi "..."
            n 4fcsfl "No,{w=0.2} [player].{w=1}{nw}"
            extend 4fsqan " Como {i}ya{/i} te dije.{w=0.75}{nw}"
            extend 4fslsl " No puedo."
            n 1fnmsf "¿Qué esperabas?{w=0.75}{nw}"
            extend 1flrem " Ya dije cómo mis clases de arte apestaron,{w=0.5}{nw}"
            extend 2fsqsl " si siquiera estabas prestando atención."
        else:

            n 2fsqsl "No,{w=0.2} [player].{w=0.75}{nw}"
            extend 2fsrem " No puedo.{w=0.75}{nw}"
            extend 2fcssf " Si eso realmente te importa."
            n 2fllem "Y no porque nunca quisiera aprender o algo así tampoco."
            n 2fsqfl "Creerías que la clase de arte de todos los lugares sería el mejor lugar para tratar y aprenderlo."

        n 2fsrpu "Apenas y sacamos los suministros de arte -{w=0.75}{nw}"
        extend 2ftrem " ¡pasamos mucho más tiempo aprendiendo sobre cómo {i}otra gente{/i} trabajó que actualmente aprendiendo nosotros mismos!"
        n 1fnmsl "Fue solo una decepción completa."
        n 1fcsbo "..."
        n 2fsqsl "Mira.{w=0.2} No soy tonta.{w=1}{nw}"
        extend 2fcsfl " Entiendo que tienes que aprender sobre por qué la gente hace arte,{w=0.75}{nw}"
        extend 2cslbo " o todos los estilos diferentes y cómo funcionan."
        n 2fcsfl "Pero va{w=0.5}{nw}"
        extend 2fcsgs " {b}mos{/b}!{w=0.75}{nw}"
        extend 2fslsf " No es como si la parte práctica fuera menos importante."
        n 2cslpu "Ni siquiera me importaría tanto si al menos hubiéramos cubierto todo lo básico {i}antes{/i} de desempolvar todos los libros de texto estúpidos.{w=0.75}{nw}"
        extend 2fcssl " No todos nosotros tenemos el tiempo para un club de arte."
        n 2fsrem "...O el lujo de practicar en casa."
        n 2csrss "Je.{w=0.75}{nw}"
        extend 2fcssf " Diría que no hay mucho deteniéndome de tratar de aprender ahora.{w=0.75}{nw}"
        extend 2cslsf " No es como si el tiempo libre fuera un problema ya."
        n 2fnmsl "¿Pero honestamente?"
        n 2fsqem "{i}Algo{/i} me dice que no voy a estar de humor para eso por un buen rato."
        n 2fslan "Me pregunto por qué..."
        extend 2fsqem " {i}[player]{/i}."
    else:

        if already_discussed_topic:
            n 2fslan "...¿En serio?{w=1}{nw}"
            extend 2fsqan " ¿Qué soy,{w=0.2} un disco rayado?"
            n 2fsquptsb "La única cosa que estoy dibujando justo ahora es un fin a esta conversación {i}estúpida{/i}."
            n 4fsqanltsb "Idiota."
        else:

            n 2fcssstsa "...Je.{w=1}{nw}"
            extend 2fslfltsb " ¿Si sé dibujar?{w=1.25}{nw}"
            extend 2fsqantsb " ¿En serio?"
            n 2fcssftsa "..."
            n 2fcsfltsa "...De hecho.{w=0.75}{nw}"
            extend 2fsqfutsb " ¿Sabes qué?"
            n 2fcsemtsa "Sí.{w=0.2} Soy buena dibujando{w=0.75}{nw}"
            extend 2fsqantsb " conclusiones."
            n 4fnmfultsf "...Y tengo muchas dibujadas sobre los tipos como {b}tú{/b}."

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_enable_no_topics_reminder",
            unlocked=True,
            prompt="¿Puedes recordarme la próxima vez que te quedes sin temas?",
            category=["Natsuki", "Recordatorios"],
            conditional="not persistent._jn_natsuki_out_of_topics_remind",
            player_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_enable_no_topics_reminder:
    $ already_discussed_topic = get_topic("talk_enable_no_topics_reminder").shown_count > 0

    n 1tnmpueqm "¿Huh?{w=0.75}{nw}"
    extend 4tnmbo " ¿Temas?{w=0.75}{nw}"
    extend 2tsrfl " ¿Qué quieres...?"
    n 2ttrsl "..."

    if already_discussed_topic:
        n 4fnmwrleexsbr "...H-{w=0.2}hey!{w=0.75}{nw}"
        extend 4fsqwrl " ¡Ahora espera un segundo aquí,{w=0.2} [player]!{w=0.75}{nw}"
        extend 4fcsgs " ¡Sé {i}exactamente{/i} de qué se trata todo esto!"
        n 2fllfl "Incluso dijiste antes que querías que {i}dejara{/i} de recordarte..."
        n 2fnmgs "¡Y ahora me estás molestando con recordarte{w=0.3}{nw}"
        extend 4fcsgs " {i}otra vez{/i}!{w=1}{nw}"
        extend 2fsrfl " Cielos..."
        n 2cslpu "¿Realmente tengo que recordarte cómo tomar una {i}decisión{/i} también ahora [player],{w=0.5}{nw}"
        extend 2csqpu " o qué?"
        n 2fsqpo "..."
        n 2fsqcs "..."
        n 2fcssm "Ehehe.{w=0.75}{nw}"
        extend 4nlrss " Nah,{w=0.5}{nw}"
        extend 1csrss " está bien.{w=0.75}{nw}"
        extend 1csrbo " {i}Supongo{/i}."
        n 4ccsaj "Solo...{w=1}{nw}"
        extend 2csqca " no hagas ningún tipo de hábito de ello.{w=0.75}{nw}"
        extend 2cslcasbr " Odio sonar como un disco rayado."

        if Natsuki.isEnamored(higher=True):
            n 2fcsbglsbr "I-{w=0.2}incluso si disfrutas escucharme seguir sobre ello {i}tanto{/i}.{w=0.75}{nw}"
            extend 2fsqsmlsbr " Ehehe."

            if Natsuki.isLove(higher=True):
                n 4fchbglsbl "Te amo,{w=0.2} [player]~!"

        elif Natsuki.isAffectionate(higher=True):
            n 2fcsajlsbr "I-{w=0.2}incluso si {i}disfrutas{/i} escucharme seguir sobre ello tanto.{w=0.75}{nw}"
            extend 2ccsbolsbl " ¿Entendido?"
        else:

            n 2fcsaj "Y-{w=0.2}y estoy segura de que tú también lo harías.{w=0.75}{nw}"
            extend 2fcspo " ¿Capiche?"
    else:

        if Natsuki.isEnamored(higher=True):
            n 2unmajesu "¡Oh!{w=0.75}{nw}"
            extend 4nllsssbr " Sí,{w=0.2} recuerdo."
            $ chosen_tease = jn_utils.getRandomTease()
            n 3fchsm "¡Seguro,{w=0.2} [chosen_tease]!{w=0.75}{nw}"
            extend 3fsqss " Será mejor que no te atrape haciendo ninguna queja,{w=0.2} [player]."
            n 4fcsbg "Después de todo..."
            n 3uchgnl "¡{i}Tú{/i} lo pediste!{w=0.75}{nw}"
            extend 3fchsmleme " Ehehe."

        elif Natsuki.isAffectionate(higher=True):
            n 4unmajesu "¡Oh!{w=0.75}{nw}"
            extend 4nslsssbr " Cierto,{w=0.5} eso."
            n 2fchbg "¡Seguro!{w=0.75}{nw}"
            extend 2fsqbg " Solo recuerda,{w=0.2} [player]..."
            n 2nchgn "¡Tú lo pediste!"
        else:

            n 2unmfleex "¡Oh!{w=0.75}{nw}"
            extend 2cllsssbr " Je.{w=0.75}{nw}"
            extend 4cslsssbr " Cierto."
            n 2ullaj "Digo...{w=1}{nw}"
            extend 2tnmbo " seguro,{w=0.2} supongo."
            n 2ccspo "S-{w=0.2}solo no te pongas todo ansioso cuando tenga que decirte qué pasa de nuevo,{w=0.2} ¿entendido?"


    $ persistent._jn_natsuki_out_of_topics_remind = True
    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_windup_playing_things_out_loud",
            unlocked=True,
            prompt="Poner cosas a todo volumen",
            category=["Cierres"],
            conditional="jn_utils.get_total_gameplay_hours() >= 4",
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_windup_playing_things_out_loud:
    $ already_discussed_topic = get_topic("talk_windup_playing_things_out_loud").shown_count > 0
    if already_discussed_topic:
        n 7csrca "..."
        n 3fcsflesi "..."
        n 3cllfl "Sabes,{w=0.2} [player]..."
        n 7tnmsl "Estoy muy segura de que ya pasé por todo esto antes.{w=0.75}{nw}"
        extend 7clrflsbl " Y ni siquiera sé por qué todavía me molesta tanto."
        n 4fsrem "Pero {i}aún{/i} no puedo soportar cuando algunas personas sienten la necesidad de simplemente explotar lo que {i}ellos{/i} quieren escuchar en voz alta frente a todos los demás."
        n 2fsrca "..."
        n 2fnmfll "¿Qué?{w=0.75}{nw}"
        extend 2csqfll " ¿Me veo como que estoy inventando todo esto o algo?{w=0.75}{nw}"
        extend 4fcsgsl " ¡Es lo {i}peor{/i}!"
    else:

        n 7cslsl "..."
        n 3fslan "¡Tch!"
        n 3fsrbo "..."
        n 3ccsss "Je."
        n 4cllfl "Oye,{w=0.2} [player]...{w=1}{nw}"
        extend 2cnmaj " ¿quieres saber qué me molesta?"
        n 2fnmfl "Y me refiero a{w=0.5}{nw}"
        extend 4fsqem " lo que {i}realmente{/i}{w=0.5}{nw}"
        extend 4fsran " ¿me pone de nervios?"
        n 2fcsemesi "..."
        n 2fllaj "Cuando estás tomando algún tipo de transporte público,{w=0.2} o solo estás pasando el rato en algún lugar.{w=0.75}{nw}"
        extend 2fllfl " Ese tipo de cosas."
        n 4fcsanean "...Y entonces algún completo idiota siente la necesidad de sacar su teléfono solo para explotar lo que {i}ellos{/i} sienten ganas de escuchar."
        n 4fsrsl "..."
        n 2fnmwrl "H-{w=0.2}hey!{w=0.75}{nw}"
        extend 2fcspol " ¡Estoy hablando en serio aquí,{w=0.2} [player]!{w=0.75}{nw}"
        extend 4fbkwrl " ¡Es lo {i}peor{/i}!"

    n 3flrem "Digo,{w=0.2} vamos.{w=0.75}{nw}"
    extend 3fupwr " ¿Por dónde siquiera {i}empiezo{/i}?"
    n 6fcsgs "Primero que nada,{w=0.5}{nw}"
    extend 3fllan " básicamente puedes garantizar que lo que sea que es,{w=0.75}{nw}"
    extend 3fslan " {i}nunca{/i} va a sonar bien."
    n 4fbkwr "¡Nada {i}nunca{/i} lo hace cuando lo estás explotando de bocinas de teléfono basura o audífonos rotos!"
    n 4fcsan "Puntos extra también si es algún niño jugando en algo que sus padres les dieron solo para callarlos."
    n 1nsqem "Y{w=0.3} Oh.{w=0.75}{nw}"
    extend 2csqfl " Por.{w=0.75}{nw}"
    extend 2fsqem " Dios,{w=0.5}{nw}"
    extend 4fsrfu " [player]."
    n 4fcsup "{i}El eco{/i}."
    n 3fsqgs "¿Siquiera sabes cuánto peor se pone cuando estás atrapado dentro del tren,{w=0.5}{nw}"
    extend 3fcsgs " o literalmente cualquier otra cosa?"
    n 3fcsan "Hablando de un dolor de oído.{w=0.75}{nw}"
    extend 7fllem " ¡Especialmente si solo querías relajarte antes de que el día empiece!"
    n 4fsrem "{i}Y{/i} puedes olvidarte de tratar de mantener cualquier tipo de conversación también con todo ese ruido de fondo."
    n 2fcssl "Je.{w=0.75}{nw}"
    extend 2fsqfr " Entonces sabes cuál es la peor parte,{w=0.2} [player]?"
    n 4fllem "Si siquiera intentas llamarles la atención,{w=0.5}{nw}"
    extend 4csqem " simplemente sabes que harán una escena masiva sobre ello también,{w=0.5}{nw}"
    extend 4fslfu " ¡o hacerlo sonar como si tú solo estuvieras enloqueciendo!"
    n 6ftlgs "'¡Pero no {i}tienes{/i} que escucharlo!'{w=0.5}{nw}"
    extend 3ftrwr " '¡Tú puedes poner lo que quieras también!'\n{w=0.75}{nw}"
    extend 3fsran "Como si eso hiciera todo simplemente bien,{w=0.5}{nw}"
    extend 3fsqan " ¿verdad?"
    n 1fcsem "Dame un descanso."
    n 2flran "Como ¿qué tan desconsiderado puedes ser?{w=0.75}{nw}"
    extend 2fcsan " ¡¿En serio?!"
    n 4fslem "A-{w=0.2}además,{w=0.5}{nw}"
    extend 4fcsgs " no es como si pudieras simplemente elegir {i}no{/i} escuchar lo que sea que decidan agraciar tus oídos con."
    n 2fsrsll "...Y no todos nosotros podemos pagar todas las cosas elegantes de cancelación de ruido tampoco."
    n 1ccsemesi "Ugh..."
    n 2fllsl "Idiotas.{w=0.75}{nw}"
    extend 2fslbol " Me hace querer arrancar ese estúpido teléfono o lo que sea de sus manos y tirarlo por la ventana."

    if get_topic("talk_using_headphones_carefully").shown_count > 0:
        n 1ccsfll "Y sé que dije antes que encerrarte del mundo con audífonos era una mala idea."
        $ descriptor = "{i}tratando{/i} de ser" if Natsuki.isAffectionate(higher=True) else "siendo medio"
        n 5csrsl "Pero al menos sigues [descriptor] considerado.{w=0.75}{nw}"
        extend 5cnmbol " ¿Sabes?"

        if Natsuki.isAffectionate(higher=True):
            n 1ccsfll "Yo solo..."
            n 4csrsll "..."

    n 4ccsfllesi "..."
    n 2cslajl "...Mira.{w=0.75}{nw}"
    extend 2ccsbo " No soy tonta.{w=0.75}{nw}"
    extend 1clrfl " Entiendo que si estás en un espacio público entonces tienes que acomodar a otros que quieren usarlo también."
    n 3fslem "¡Pero eso no le da a cualquier viejo idiota el derecho de usarlo como {i}ellos{/i} quieran a expensas de todos los demás!"
    n 3fsrsl "...Mucho menos actuar tan con derecho sobre toda la cosa estúpida.{w=0.75}{nw}"
    extend 3fsrfl " Cielos."
    n 3fnmca "..."
    n 4ccsflsbl "...Sí,{w=0.2} sí.{w=0.75}{nw}"
    extend 1cllcasbl " Lo sé.{w=0.75}{nw}"

    if already_discussed_topic:
        extend 2cllflsbr " No voy a dejar que me moleste tanto.{w=0.75}{nw}"
        extend 2cslflsbr " De nuevo."
    else:

        extend 2ccstrlsbr " No voy a dejar que me moleste {i}tanto{/i}."

    if Natsuki.isEnamored(higher=True):
        n 2fcsssl "...I-{w=0.2}incluso si sé que simplemente no puedes tener suficiente del sonido de mi voz."

    elif Natsuki.isAffectionate(higher=True):
        n 2csrpol "...Incluso si apuesto que solo disfrutas escuchar mis quejas estúpidas por ahora."

    n 2ulraj "Así que...{w=1}{nw}"
    extend 2cnmca " Solo voy a decir esto."
    n 1tllfl "Realmente no me importa lo que escuches o cómo lo escuches en tus propias cuatro paredes,{w=0.2} [player]."

    if Natsuki.isEnamored(higher=True):
        n 5csrssl "And I {i}seriously{/i} doubt you of all people would do something like that.{w=0.75}{nw}"
        $ descriptor = "eres" if Natsuki.isLove(higher=True) else "eres"
        extend 5csqssl " Incluso si [descriptor] un gran tonto a veces."

    elif Natsuki.isAffectionate(higher=True):
        n 4csrsslsbr "Y medio dudo que seas la clase de persona que hace ese tipo de cosas de todos modos."
    else:

        n 2tlraj "Y medio dudo que seas {i}tan{/i} idiota de todos modos."

    n 2clrfl "Pero...{w=1}{nw}"
    extend 2csgfl " si escucho sobre ti explotando algún tipo de transmisión de [player] allá afuera enfrente de todos cuando {w=0.3}{i}literalmente{/i}{w=0.5}{nw}"
    extend 2csqfl " ¿nadie preguntó?"
    n 4fcsbs "...¡Entonces puedes apostar tu trasero que voy a darle a {i}tus{/i} oídos algo extra especial para escuchar!{w=0.75}{nw}"
    extend 4fsqsmeme " Ehehe."

    if Natsuki.isLove(higher=True):
        n 2fchbgl "¡Te amo,{w=0.2} [player]~!"

    elif Natsuki.isAffectionate(higher=True):
        n 2fchgnl "¡De nada,{w=0.2} [player]!"
    else:

        n 2nchgn "¡Espero que hayas aprendido algo,{w=0.2} [player]!"

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_work_experience",
            unlocked=True,
            prompt="¿Alguna vez tuviste alguna experiencia laboral?",
            category=["Sociedad"],
            conditional="jn_utils.get_total_gameplay_days() >= 2",
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_work_experience:
    $ already_discussed_work_experience = get_topic("talk_work_experience").shown_count > 0
    if Natsuki.isNormal(higher=True):
        if already_discussed_work_experience:
            n 7csrfl "Espera...{w=1}{nw}"
            extend 7tnmfl " ¿experiencia laboral?{w=0.75}{nw}"
            extend 3ccsajsbr " E-{w=0.2}espera un segundo."
            n 7tnmbosbr "¿No me preguntaste sobre eso ya,{w=0.2} [player]?{w=0.75}{nw}"
            extend 7tllsl " Huh."
            n 4tllaj "Bueno,{w=0.5}{nw}"
            extend 4ullaj " lo que sea.{w=0.75}{nw}"
            extend 2cnmfl " Supongo que no me importa compartir mi...{w=1}{nw}"
            extend 2csrfl " {i}experiencia{/i}{w=0.5}{nw}"
            extend 2csrsl " de nuevo."
            n 1ccsem "Si siquiera puedes llamarlo así,{w=0.2} c-{w=0.2}como sea."
            n 3cllfl "Como estaba diciendo antes,{w=0.2} nunca pudimos elegir apropiadamente nuestras prácticas ni nada de eso."
        else:

            n 3tlrbo "Experiencia laboral,{w=0.5}{nw}"
            extend 3tnmbo " ¿huh?"
            n 4ccsflsbl "...Espera.{w=0.75}{nw}"
            extend 4nsqflsbl " No me digas.{w=0.75}{nw}"
            extend 2csqem " ¿Te refieres a algún tipo de práctica mientras estaba en la escuela?{w=0.75}{nw}"
            extend 2tsqfl " ¿O como una pasantía?"
            n 1cnmsl "¿{i}Ese{/i} tipo de experiencia laboral?"
            n 2fcsslesi "..."
            n 2ccsfl "Je.{w=0.75}{nw}"
            extend 2cllfl " Sí.{w=0.75}{nw}"
            extend 4cslfr " Todo el proceso fue una {i}experiencia{/i} de acuerdo."
            n 7nllaj "Entonces.{w=0.75}{nw}"
            extend 7ullfl " No sé cómo funciona para ti,{w=0.2} [player].{w=0.75}{nw}"
            extend 3tnmsl " ¿Pero en mi escuela al menos?{w=0.75}{nw}"
            extend 3clrem " Ni siquiera pudimos {i}elegir{/i} apropiadamente nuestras prácticas."

        n 1fnmem "En serio -{w=0.5}{nw}"
        extend 4fllgs " ¡fue una total lotería!{w=0.75}{nw}"
        extend 2fslan " ¡Nada más que pura suerte!"

        if already_discussed_work_experience:
            n 2ccsslsbr "Y no,{w=0.2} como dije -{w=0.5}{nw}"
        else:

            n 2ccsemsbr "Y no,{w=0.2} [player],{w=0.2} antes de que preguntes -{w=0.5}{nw}"

        extend 1csqemsbr " no tuvimos opción en si {i}queríamos{/i} hacerlo tampoco."
        n 4clraj "Todos teníamos este formulario en línea que teníamos que llenar en la sala de computadoras,{w=0.5}{nw}"
        extend 4fsqfl " pero no era como que pudiéramos solo escribir un lugar que ya tuviéramos en mente.\n{w=0.75}{nw}"
        extend 2fupem "Por {i}supuesto{/i} que no."
        n 2fcsgs "¡Nop!{w=0.75}{nw}"
        extend 2fllem " Era solo un montón de opciones prellenadas entre las que teníamos que elegir.{w=0.75}{nw}"
        extend 4fslan " ¡Ni siquiera eran buenas!"
        n 2flrem "Había un par de lugares de oficina,{w=0.2} seguro."
        n 2fnman "¡Pero la mayoría de ellos eran solo trabajar en alguna tienda random!{w=0.75}{nw}"
        extend 4fcswr " ¡El punto entero de esos es que ni siquiera {i}necesitas{/i} experiencia para hacerlos!"
        n 2fsrem "...Y teníamos que elegir {i}tres{/i} de ellos también.{w=0.5} {i}En orden de preferencia{/i}."
        n 1fcssl "Je.{w=0.75}{nw}"
        extend 4fsqfl " ¿La peor parte,{w=0.2} [player]?{w=0.75}{nw}"

        if already_discussed_work_experience:
            extend 4fslsl " {i}Todavía{/i} me molesta hablar de ello una segunda vez."
        else:

            extend 4fllfl " Ni siquiera vas a {i}creer{/i} esto."

        n 4fnmgs "¡Tuvimos que escribir una carta de presentación completa para todos ellos también!{w=0.75}{nw}"
        extend 2fsran " ¡Había un conteo de palabras y todo!"
        n 2ccsemesi "..."
        n 2fcsbosbr "Lo entiendo.{w=0.75}{nw}"
        extend 7cllflsbl " Se suponía que nos daría práctica sobre cómo aplicar para cosas en el futuro."
        n 3fcsgs "¡Pero {i}en serio{/i}!"
        n 2fslan "¿Sabes cuánto dolor es sonar convincente para algo que ni siquiera te {i}importa{/i}?"
        n 2fcswr "¡Ni siquiera sabíamos sobre la mitad de los lugares que podíamos elegir hasta que aparecieron en la lista!"
        n 1fsran "No es como que los lugares a los que estábamos aplicando no {i}sabían{/i} que teníamos que hacerlo tampoco -{w=0.5}{nw}"
        extend 3fcsan " ¡todo es un acto total de todas formas!"
        n 3fllem "Así que entonces estábamos atrapados tratando de investigar desesperadamente todos estos lugares,{w=0.5}{nw}"
        extend 3fnmem " qué hacían siquiera,{w=0.5}{nw}"
        extend 4flran " cómo realmente {i}llegar{/i} ahí..."
        n 1fsqan "...¡Mientras tratábamos de hacer creer que éramos {i}asombrosos{/i} para el trabajo y vencer a todos los demás en entregarlo!"
        n 2fslsl "Entonces con todos aplicando para todos los buenos,{w=0.5}{nw}"
        extend 2fslem " los maestros solo enviarían tu última opción en su lugar.{w=0.75}{nw}"
        extend 4fnmbo " O tirarte con algún lugar que nadie quería para nada."

        $ already_discussed_interviews = get_topic("talk_how_to_interview_properly").shown_count > 0
        if already_discussed_interviews:
            n 1csrsl "Hablando de una completa pérdida de tiempo."
            n 2clrflsbl "Ya mencioné antes que nunca tuve el tiempo para un trabajo de medio tiempo o nada como eso fuera de la escuela."
            n 4csqslsbl "...¿Así que por qué creyeron que tendríamos un par de semanas para desperdiciar en algo como {i}eso{/i}?"
            n 2fcsfl "{i}Especialmente{/i} cuando ni siquiera es trabajo pagado."
        else:

            n 2fcsfl "Ugh..."
            n 6tsqfl "¿Y con las tareas constantes más todas las lecciones regulares también?{w=0.75}{nw}"
            extend 4fllfl " ¡Ni siquiera tenía tiempo para un trabajo {i}pagado{/i}!{w=0.75}{nw}"
            extend 2fcsaj " Mucho menos solo entregando todo mi esfuerzo {i}gratis{/i}."

        n 2csrfl "Sí,{w=0.2} sí.{w=0.75}{nw}"
        extend 2clrfl " Pasamos tiempo en un lugar de trabajo real para que sepamos qué esperar después,{w=0.5}{nw}"
        extend 1clrbo " o construir algunas conexiones."
        n 2ccsflsbr "Es solo que..."
        n 5cslbosbr "..."

        if Natsuki.isAffectionate(higher=True):
            n 4fcsemsbr "¡E-{w=0.2}es solo tan {i}molesto{/i}!{w=0.75}{nw}"
            extend 4knmemsbr " ¿Sabes?{w=0.75}{nw}"
            extend 2csrfllsbl " Con tanto pasando al mismo tiempo,{w=0.2} quiero decir."
            n 1csrsllsbl "..."
            n 4ccspulsbl "No...{w=1}{nw}"
            extend 4fcspul " me...{w=1}{nw}"
            extend 2flrbol " importa ayudar a un lugar."
            n 5csrpul "Si es sobre algo que realmente me {i}importa{/i}."
            n 5cnmeml "...¿Pero por qué tiene que sufrir {i}mi{/i} futuro por ello?"
            n 2cslsll "No es como que no pudiera simplemente conseguir un trabajo en uno de esos lugares cuando realmente necesitara el trabajo.{w=0.75}{nw}"
            extend 2knmbol " ¿Verdad?"

            if Natsuki.isEnamored(higher=True):
                n 1ccsss "Je.{w=0.75}{nw}"
                extend 1csrpu " Además."
                n 1clrsll "Ya se me dijo que mi futuro solo iba a ser apilar estantes."
                n 2kslsll "...La última cosa que necesitaba era una vista previa."
                n 2kslbol "..."
                n 4ccsemlsbr "C-{w=0.2}como sea!"
            else:

                n 2kslbol "..."
                n 4ccscasbr "C-{w=0.2}como sea."

            n 5cslbo "Como si todo el tiempo gastado buscando y llenando cosas en realidad hubiera terminado significando mucho."
            n 4unmgs "¡No es que no lo {i}intentara{/i} ni nada de eso!{w=0.75}{nw}"
            extend 2fcsgssbr " ¡P-{w=0.2}por supuesto que lo hice!{w=0.75}{nw}"
            extend 2fllslsbr " Solo mi suerte que todos sintieron ganas de elegir los únicos lugares que {i}yo{/i} podía soportar."
            n 5flrflsbr "Y no era como que pudiera siquiera ir a muchos otros lugares tampoco."
            n 5clrslsbr "No con mi...{w=1}{nw}"
            extend 1ksrslsbr " situación."
            n 1nlraj "Así que..."
            n 2nslbo "Acordaron dejarme pasar algún tiempo en la biblioteca de la escuela en su lugar.\n{w=0.75}{nw}"
            extend 2cslss "Al menos pude estudiar cuando no estaba ocupado."
            n 2kslsllsbr "...Y siempre llegué a casa a tiempo.{w=1}{nw}"
            extend 5cslbol " Supongo que pude apreciar eso."

            $ office_outfit = jn_outfits.getOutfit("jn_office_outfit")
            if Natsuki.isEnamored(higher=True) and persistent.jn_custom_outfits_unlocked and not office_outfit.unlocked:
                n 7cllbo "..."
                n 7cllfl "...De hecho.{w=0.75}{nw}"
                extend 7tllbo " Ahora que lo pienso..."
                n 3tnmfl "Estoy muy segura de que todavía tengo el atuendo que armé para mi práctica en algún lugar también.{w=0.75}{nw}"
                extend 3nlrfl " Huh."
                n 4tlrsl "..."
                n 4tsrss "De hecho.{w=0.75}{nw}"
                extend 7cnmss " ¿Sabes qué?{w=0.75}{nw}"
                extend 6ccsss " Solo dame un minuto aquí."
                n 3fcsbslsbl "¡Alguien tiene que mostrarte cómo se ve un profesional {i}real{/i},{w=0.2} d-{w=0.2}después de todo!"

                show natsuki 4fcssmlsbl
                show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
                $ jnPause(1)
                play audio chair_out

                $ jnPause(3)
                play audio drawer
                $ jnPause(1.5)
                play audio clothing_ruffle
                $ jnPause(1.5)
                n "¡Oye!{w=0.5} ¡N-{w=0.2}nada de espiar!"
                $ jnPause(1)
                play audio zipper
                $ jnPause(3)
                $ office_outfit.unlock()
                $ Natsuki.setOutfit(outfit=office_outfit, persist=False)

                play audio chair_in
                $ jnPause(3)
                show natsuki 5csrdvlsbr at jn_center
                hide black with Dissolve(1.25)

                n 5csqbolsbr "..."
                n 5ccssslsbr "B-{w=0.2}bueno?{w=0.75}{nw}"
                extend 4cnmajlsbr " ¡No mientas,{w=0.2} [player]!{w=0.75}{nw}"
                extend 4cllbglsbr " Después de todo."
                n 3fcsbglsbl "No necesito ser una bibliotecaria apropiada para leerte a {i}ti{/i} como un libro.{w=0.75}{nw}"

                if Natsuki.isLove(higher=True) and get_topic("talk_school_uniform").shown_count > 0:
                    extend 4fslbglsbl " Además..."
                    n 6fsgsmlsbl "¿N-{w=0.2}no te {i}gustaba{/i} una chica en uniforme,{w=0.2} [player]?{w=0.75}{nw}"

                extend 3fsqsmlsbl " Ehehe."
                n 5fcsbgsbl "Obviamente no {i}tenía{/i} que vestirme para ello ni nada de eso.{w=0.75}{nw}"
                extend 2flrbg " Pero vamos."
                n 2fchgn "¿Quién {i}no{/i} dejaría pasar un descanso del uniforme escolar,{w=0.2} verdad?"
            else:

                n 1ccsfllesi "..."
        else:

            n 4ccsflsbr "O-{w=0.2}olvídalo.{w=0.75}{nw}"
            extend 2ccsposbr " Obviamente mi práctica estuvo bien.{w=0.75}{nw}"
            extend 2csrbosbr " Aunque no es como si nada de eso importara ahora de todas formas."

        if persistent._jn_player_had_work_placement is None:
            n 1ulraj "Pero...{w=1}{nw}"
            extend 4clrflsbl " He continuado demasiado ya.{w=0.75}{nw}"
            extend 5csrbosbl " De nuevo.{w=0.75}{nw}"
            extend 2tlraj " Así que..."
            n 7tnmaj "¿Qué hay de ti,{w=0.2} [player]?"

            show natsuki option_wait_curious
            menu:
                n "¿Alguna vez tuviste algún tipo de práctica laboral,{w=0.2} o...?"
                "Sí, he tenido una práctica laboral":

                    $ persistent._jn_player_had_work_placement = True
                    n 4fnmbg "¡Ajá!{w=0.75}{nw}"
                    extend 3fcsbg " ¡Lo sabía!{w=0.75}{nw}"
                    extend 6fsqsm " Solo no podías salirte de ello,{w=0.2} ¿eh?"
                    n 7tllss "Bueno...{w=0.3} Realmente no puedo decir que estoy sorprendida.{w=0.75}{nw}"
                    extend 7ccssmesm " No es como si {i}tú{/i} pudieras salirte de eso si yo no pude."
                "No, no he tenido una práctica laboral":

                    $ persistent._jn_player_had_work_placement = False
                    n 3nsrsl "...Hmph.{w=0.75}{nw}"
                    extend 3fcspo " Suertudo."
                    n 7clraj "Aunque tengo que preguntar,{w=0.2} [player]."
                    n 7tnmfl "¿Es eso porque simplemente nunca fuiste a algún lugar que hiciera eso?"
                    n 6fcsbg "...¿O estás solo sentado esperando por tu turno?"
                    n 3fsqsm "..."
                    n 3fcssm "Ehehe.{w=0.75}{nw}"
                    extend 4csgbg " ¿Te llamé la atención?"
                "Tengo una práctica laboral ahora":

                    $ persistent._jn_player_had_work_placement = True
                    n 3ccsss "¿Oh?{w=0.75}{nw}"
                    extend 7ccsbg " ¿Y supongo que estás trabajando duro entonces,{w=0.2} [player]?"
                    n 7csqsm "...Je."
                    n 6fsqbg "¿O durando en el trabajo?"
                    n 3fsqsm "..."
                    n 3fcssmeme "Ehehe."

            n 4ulrss "Bueno,{w=0.2} como sea."
        else:

            n 1nlraj "Pero...{w=1}{nw}"
            extend 5clrpu " He continuado por demasiado tiempo ya.{w=0.75}{nw}"
            extend 5csrbosbl " Realmente tengo que dejar de hacer eso."

        if Natsuki.isEnamored(higher=True):
            n 3clrfl "Todavía no diría que realmente califico mi práctica laboral."
            n 7tlrbo "Pero...{w=1}{nw}"
            extend 7tnmca " ¿estar aquí contigo,{w=0.2} [player]?"
            n 4ccsssl "Je."
            n 4cllsslsbr "...Sí,{w=0.5}{nw}"
            extend 5ccssmlsbr " diría que esa es una {i}experiencia{/i} por la que puedo estar muy feliz."
            n 5clrbglsbr "I-{w=0.2}incluso si {i}eres{/i} un montón de trabajo a veces.{w=0.75}{nw}"
            extend 2fchsmfsbr " Ehehe."

            if Natsuki.isLove(higher=True):
                $ chosen_tease = jn_utils.getRandomTease()
                n 5fchblfeaf "¡T-{w=0.2}te amo también,{w=0.2} [chosen_tease]!"

        elif Natsuki.isAffectionate():
            n 3clrfl "Todavía no diría que califico mi experiencia honestamente."
            n 7tlrbo "Pero...{w=1}{nw}"
            extend 7tnmfl " estar atrapada aquí contigo,{w=0.2} [player]?"
            n 5tllbolsbr "..."
            n 5tllsslsbr "Bueno...{w=1}{nw}"
            extend 6ccsbglsbl " ¡S-{w=0.2}supongo que podría pensar en una peor práctica!"
            n 3ccssmlsbl "Ehehe."

        elif Natsuki.isHappy():
            n 5clrfl "No diría exactamente que califico mi experiencia,{w=0.2} para ser honesta."
            n 7clrpu "Pero...{w=1}{nw}"
            extend 7tnmpu " ¿solo sentarse por aquí hablando contigo?{w=0.75}{nw}"
            extend 7ullbo " Bueno..."
            n 2fchgn "¡Supongo que puedo pensar en un montón de peores prácticas!{w=0.75}{nw}"
            extend 2nchgn " Jajaja."
        else:

            n 7ulraj "No diría exactamente que califico mi experiencia,{w=0.2} para ser honesta."
            n 7tlrfl "Pero...{w=1}{nw}"
            extend 7tnmfl " ¿solo sentarse por aquí contigo?"
            n 4tllaj "Bueno...{w=1}{nw}"
            extend 4nchgn " ¡Supongo que podría irme peor!"
            n 2csrajsbl "S-{w=0.2}solo no lo hagas todo incómodo,{w=0.2} [player].{w=0.75}{nw}"
            extend 5cslposbl " ¿Capiche?"

    elif Natsuki.isDistressed(higher=True):
        if already_discussed_work_experience:
            n 1ccsemesi "..."
            n 2cslem "En serio,{w=0.75}{nw}"
            extend 2csqem " ¿[player]?{w=0.75}{nw}"
            extend 4fsqfl " ¿Esto {i}otra vez{/i}?{w=0.75}{nw}"
            extend 4fnmfl " ¿Siquiera estabas {i}escuchando{/i} la primera vez o qué?"
            n 1fcsfr "..."
            n 1flrfl "...Bien.{w=0.75}{nw}"
            extend 2fcsfl " Además."
            n 4fllsl "No voy a discriminar contra los{w=0.5}{nw}"
            extend 4fsqsl " {i}duros de oído{/i}."
            n 1fcsfl "Entonces.{w=0.75}{nw}"
            extend 1flrbo " Como estaba diciendo antes..."
        else:

            n 4nsqfl "...¿Qué?{w=0.75}{nw}"
            extend 4tsqsl " ¿Experiencia laboral?"
            n 4nslfl "Oh."
            n 2fcsfl "Je.{w=0.75}{nw}"
            extend 2flrfl " Sí.{w=0.75}{nw}"
            extend 2fsrpu " Tuve una {i}experiencia{/i} de acuerdo.{w=0.75}{nw}"
            extend 4csqsl " Si eso realmente importa."

        n 1nllaj "Mi escuela hizo prácticas,{w=0.75}{nw}"
        extend 1nllsl " pero no fue algún tipo de gran evento si eso es lo que estabas pensando."
        n 2fslfr "Aunque algún {i}aviso{/i} real hubiera sido lindo."
        n 2fcsaj "Nop -{w=0.5}{nw}"
        extend 4flrem " todos fuimos barajados a la sala de computadoras un día,{w=0.5}{nw}"
        extend 4fnmfl " y nos dijeron que iniciáramos sesión en algún sitio web especial de prácticas."
        n 3cslfl "Entonces tuvimos que elegir algunas opciones de una lista de lugares que estaban aceptando estudiantes para hacer prácticas laborales."
        n 3ctlfl "Había un par de lugares decentes,{w=0.2} seguro.{w=0.75}{nw}"
        extend 3fcsan " ¡Pero {i}todos{/i} fueron por esos!{w=0.75}{nw}"
        extend 3fsran " Y luego simplemente serías enviado a algún basurero que a nadie le importaba en su lugar si no eras el favorito del maestro."
        n 1fcsem "...Y no,{w=0.2} [player].{w=0.75}{nw}"
        extend 2nsqsl " No tuvimos la opción de pasar.{w=0.75}{nw}"
        extend 2cllsl " {i}Todos{/i} tuvimos que hacerlo."
        n 4fllem "No fue solo elegir cosas de una lista tampoco -{w=0.5}{nw}"
        extend 4fsqfl " cartas de presentación y entrevistas también.{w=0.75}{nw}"
        extend 4fsrfl " Todo el proceso estúpido."
        n 1flrsl "Ni siquiera sé a quién creían que engañaban."
        extend 2fsrsl " No era como si esos lugares {i}no{/i} fueran a aceptar a quien sea que la escuela les enviara."
        n 2fllfl "Y luego todo eso alrededor de nuestros estudios regulares solo para frotarlo en la cara.\n{w=0.75}{nw}"
        extend 4fslem "Como si {i}mágicamente{/i} encontráramos el tiempo alrededor de todas las tareas y exámenes o algo."
        n 4fcsemesi "..."
        n 2fcssl "Lo entiendo,{w=0.2} ¿okay?{w=0.75}{nw}"
        extend 1fsrem " No soy tonta.{w=0.75}{nw}"
        extend 2ccsem " {i}Obviamente{/i} las habilidades de vida y conexiones importan."
        n 4fcsfl "Pero va{w=0.5}{nw}"
        extend 4fcsgs " {b}mos{/b}!{w=0.75}{nw}"
        extend 3flrsl " Como si me estuviera perdiendo de experiencia de vida {i}súper importante{/i} apilando{w=0.5}{nw}"
        extend 3fsran " estantes,{w=0.5}{nw}"
        extend 3fllem " o jugando al cajero por dos semanas."
        n 1fcsem "Ugh..."
        n 2flrsl "No me habría importado tanto si no tuviera todo lo demás para mantener encima.{w=0.75}{nw}"
        extend 2fsrsl " O si el trabajo fuera realmente {i}pagado{/i}.{w=0.75}{nw}"
        extend 2fsrem " Qué pérdida de tiempo."
        n 1fcsfl "No es como si nada de eso importara ahora sin embargo,{w=0.2} supongo."
        n 4fsqfl "Después de todo."

        if Natsuki.isUpset(higher=True):
            n 4fslsl "Estar aquí justo ahora ya se siente como trabajo suficiente para mí,{w=0.5}{nw}"
            extend 4fsqfr " {i}[player]{/i}."
        else:

            n 4fcsan "Lidiar {i}contigo{/i} justo ahora se siente como trabajo suficiente para mí,{w=0.5}{nw}"
            extend 4fsqan " {i}[player]{/i}."
    else:

        if already_discussed_work_experience:
            n 1fcsfltsa "Je.{w=1}{nw}"
            extend 1fsqantsb " ¿Qué parezco?{w=1.25}{nw}"
            extend 4fnmuptsc " ¿Tu {i}caja de resonancia{/i} personal?"
            n 4fcsantsa "Como ya {i}te dije{/i} -{w=0.75}{nw}"
            extend 4fcswrtsa " apestó,{w=0.2} ¿okay?!{w=1}{nw}"
            extend 2fsqwrtsb " ¿Es eso lo que querías escuchar?!"
            n 2fslantsb "Nunca quise hacer ninguna,{w=0.2} y fui obligada a de todas formas."
            n 4fsqfultsb "Mucho como esta conversación.{w=1}{nw}"
            extend 4fcsanltsa " Terminé de hablar de esto,{w=0.2} {i}[player]{/i}."
        else:

            n 1fsqfltsb "...¿En serio?{w=1}{nw}"
            extend 4fnmantsc " ¿Y desde cuándo te importó cualquiera de mis experiencias,{w=0.75}{nw}"
            extend 4fsqantsc " {i}[player]{/i}?"
            n 4fcsuntsa "..."
            n 2fcsemtsa "¿Sabes qué?{w=1}{nw}"
            extend 2fcsantsa " No me importa.{w=1}{nw}"
            extend 1fnmantsc " ¿Quieres una respuesta tan mal?{w=1.25}"
            extend 2fsquptsb " {b}Bien{/b}."
            n 2flrantsc "Fue basura.{w=1}{nw}"
            extend 4fnmfutsc " ¿Okay?!{w=1.25}{nw}"
            extend 4fcsfutsa " El proceso {i}entero{/i}."
            n 1fslantsb "Desde aplicar a todas las opciones estúpidas,{w=0.75}{nw}"
            extend 1fslfrtsb " hasta escribir cartas sin sentido.{w=1}{nw}"
            extend 2fsqantsb " Todo eso."
            n 2fcsunltsa "Je.{w=1}{nw}"
            extend 4fcsgtltsa " ¿Y aún así de alguna manera?"
            n 4fsqgtltsb "Todavía preferiría eso a estar atrapada aquí con los gustos de{w=0.5}{nw}"
            extend 1fsqwrltse " ¡{b}TI{/b}!"

        if Natsuki.isRuined():
            $ chosen_insult = jn_utils.getRandomInsult()
            n 2fcsfultse "{i}[chosen_insult].{/i}"

    return


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_play_blackjack",
            unlocked=True,
            prompt="¿Quieres jugar Blackjack?",
            conditional="persistent._jn_blackjack_unlocked",
            category=["Juegos"],
            player_says=True,
            affinity_range=(jn_affinity.AFFECTIONATE, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_play_blackjack:
    if Natsuki.isLove(higher=True):
        $ chosen_tease = jn_utils.getRandomTease()
        n 2ccsbgl "¡Duh!{w=0.75}{nw}"
        extend 4fchgnl " ¡Por supuesto que quiero jugar contigo,{w=0.2} [chosen_tease]!{w=0.75}{nw}"
        extend 4fchsml " Ehehe."

    elif Natsuki.isEnamored(higher=True):
        n 2ccssml "Blackjack otra vez,{w=0.2} ¿eh?"
        n 2fsqsml "Ehehe.{w=0.75}{nw}"
        extend 4fnmbgl " ¡Puedes apostar que sí,{w=0.2} [player]!"
    else:

        n 2unmss "¿Quieres jugar blackjack otra vez?{w=0.75}{nw}"
        extend 2fchbg " ¡Seguro,{w=0.2} [player]!"

    if Natsuki.getDeskItemReferenceName(jn_desk_items.JNDeskSlots.right) == "jn_card_pack":
        n 7csqbg "Qué bueno que no guardé las cartas aún,{w=0.2} ¿eh?"
    else:

        $ dialogue_choice = random.randint(1, 5)
        if dialogue_choice == 1:
            n 4nchgn "¡Hora de sacar las cartas!"

        elif dialogue_choice == 2:
            n 4fcssmeme "Solo tengo que prepararme muy rápido..."

        elif dialogue_choice == 3:
            n 4fcsss "Solo dame un segundo aquí..."

        elif dialogue_choice == 4:
            n 4fchbg "¡Tomaré las cartas!"
        else:

            n 4fdwsm "Déjame prepararme aquí..."

        show natsuki 4fcssmeme
        show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
        $ jnPause(1.5)
        play audio drawer
        $ jnPause(1)
        $ Natsuki.setDeskItem(jn_desk_items.getDeskItem("jn_card_pack"))
        show natsuki 4fchsm
        hide black with Dissolve(1)

    $ get_topic("talk_play_blackjack").shown_count += 1
    jump blackjack_intro


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_remind_blackjack_rules",
            unlocked=True,
            prompt="¿Puedes repasar las reglas del Blackjack de nuevo?",
            conditional="persistent._jn_blackjack_unlocked and persistent._jn_blackjack_explanation_given",
            category=["Juegos"],
            player_says=True,
            affinity_range=(jn_affinity.AFFECTIONATE, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_remind_blackjack_rules:
    if Natsuki.isLove(higher=True):
        n 2tllss "Necesitas un pequeño recordatorio,{w=0.5}{nw}"
        extend 2tnmbo " ¿eh [player]?"
        n 7tlrsl "..."
        n 7tlraj "Bueno...{w=1}{nw}"
        extend 7tlrss " Supongo que no puedo estar muy sorprendida,{w=0.75}{nw}"
        extend 7tsqss " conociéndote."
        n 6ccssslsbr "E-{w=0.2}es muy difícil prestar atención con una cara tan linda,{w=0.2} ¿verdad?{w=0.75}{nw}"
        extend 3csldvlsbr " Ehehe."
        n 4ccsbglsbr "...C-{w=0.2}como sea."

    elif Natsuki.isEnamored(higher=True):
        n 1ccsbg "¿Oh?"
        n 1flrbg "Alguien necesita un recordatorio ya,{w=0.5}{nw}"
        extend 1fsqss " ¿eh?"
        n 1fsqsm "..."
        n 1fchsm "Jajaja.{w=0.75}{nw}"
        extend 1nlrbg " Nah,{w=0.2} está bien.{w=0.75}{nw}"
        extend 1unmbo " No me importa repasarlo de nuevo."
        n 1fsqbg "...Siempre y cuando mantengas tus oídos atentos {i}esta{/i} vez,{w=0.2} al menos.{w=0.75}{nw}"
        extend 1fsqsm " Ehehe."
    else:

        n 1ccsss "Je.{w=0.75}{nw}"
        extend 1nsqsl " Wow,{w=0.2} [player]."
        n 4nsgfl "¿En serio olvidaste{w=0.5}{nw}"
        extend 4csqfl " ya?"
        n 2csqbo "..."
        n 2fcssm "Ehehe."
        n 1tlrss "Nah,{w=0.5}{nw}"
        extend 3clrss " Está bien."
        n 7ccsbg "No puedo esperar que {i}todos{/i} tengan una memoria tan buena como la mía,{w=0.5}{nw}"
        extend 7fcssmesm " después de todo."

    $ get_topic("talk_remind_blackjack_rules").shown_count += 1
    jump blackjack_explanation


init python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_windup_shaving",
            unlocked=True,
            prompt="Afeitarse",
            category=["Cierres", "Moda"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_windup_shaving:
    $ already_discussed_shaving = get_topic("talk_windup_shaving").shown_count > 0
    if already_discussed_shaving:
        n 2ccsemesi "..."
        n 2cllfl "Sé que no es exactamente algo en lo que tengo que pensar tanto aquí.\n{w=0.75}{nw}"
        extend 4ccsajlsbr " Y-{w=0.2}y sé que probablemente estés harto de escuchar sobre ello por ahora."
        n 3csrfl "Pero todavía no puedo superar cuánto dolor es mantenerse al día con el afeitado siempre."
        n 3fsqbo "..."
        n 4cnmwrl "¡H-{w=0.2}hey!{w=0.75}{nw}"
        extend 2fcstrlsbr " ¡No me des esa mirada,{w=0.2} [player]!"
        n 2fcspo "¡Deberías saber perfectamente bien de lo que estoy hablando!{w=0.75}{nw}"
        extend 4fsrem " Especialmente después de la última vez.{w=0.75}{nw}"
        extend 4fcsan " ¡Es lo {i}peor{/i}!"
        n 6fcsgs "Primero que nada,{w=0.5}{nw}"
    else:

        n 7cslpu "..."
        n 7fcsan "¡Tch!"
        n 3fsrsl "..."
        n 3fcsem "...Ugh."
        n 4fsrfl "Hombre.{w=0.75}{nw}"
        extend 4flrfl " Totalmente olvidé cuánto eso me ponía de nervios."
        n 2csqem "...¿Sabes lo que {i}siempre{/i} odié,{w=0.2} [player]?{w=0.75}{nw}"
        extend 4fslan " ¿Algo que {i}nunca{/i} falló en ponerme de nervios?"
        n 1fslsl "..."
        n 2fsqpu "...Afeitarse."
        n 2fsqfr "..."
        n 2fsqfl "...Sí.{w=0.75}{nw}"
        extend 2fsgem " Sabes exactamente de lo que estoy hablando.{w=0.75}{nw}"
        extend 2fcsgs " Prácticamente puedo verlo en tu cara."
        n 4fllwr "En serio,{w=0.2} [player] -{w=0.5}{nw}"
        extend 4fsqan " ¡es en serio lo peor!{w=0.75}{nw}"
        extend 4fbkwr " ¡No puedo soportarlo!"
        n 3fcswr "¡Es como si cada parte de todo ello estuviera prácticamente {i}diseñada{/i} para molestarte!"
        n 3fcsemesi "..."
        n 4fsgwr "Mejor que estés sentado cómodamente,{w=0.2} [player].{w=0.75}{nw}"
        extend 2fslan " Porque tengo una lista real para soltarme en esta."
        n 6fcsgs "Primero que nada,{w=0.5}{nw}"

    extend 3fupwr " démosle un {i}enorme{/i} aplauso al dolor en el trasero favorito de todos:{w=0.75}{nw}"
    extend 3fsran " ¡el cuerpo humano!"
    n 1fcsgs "No sé tú,{w=0.2} [player].{w=0.75}{nw}"
    extend 2tnmem " ¿Pero dependiendo de qué tan rápido crece tu cabello?{w=0.75}{nw}"
    extend 2csqem " Vas a estar mirando desde días hasta horas entre afeitadas."
    n 2fupgs "¡Por supuesto!"
    n 2fcsgs "Porque nadie{w=0.5}{nw}"
    extend 2fsqem " {i}nunca{/i}{w=0.5}{nw}"
    extend 2fllem " tuvo nada mejor que hacer en la mañana que perder un montón de tiempo obsesionándose sobre qué tan {i}sedosas{/i} son sus características."
    n 4fsqfl "¿Verdad?"
    n 3flran "Y ni siquiera me hagas empezar en qué tan contra-intuitivo es todo ello tampoco."
    n 7fsqem "¿Ir muy lento?{w=0.75}{nw}"
    extend 7fnmem " ¿Ir muy rápido?{w=0.75}{nw}"
    extend 3fsqem " ¿Solo {i}mirar{/i} a tu rasuradora de la manera incorrecta?"
    n 4ftlwr "¡Sorpresa!{w=0.75}{nw}"
    extend 4fcswr " Espero que te hayas abastecido de curitas.{w=0.75}{nw}"
    extend 2csqup " Porque sabes lo que vas a estar haciendo por los siguientes diez minutos."
    n 2ccswr "Digo,{w=0.2} en serio -{w=0.5}{nw}"
    extend 2fsqwr " Ni siquiera es como si tuvieras que preocuparte por eso para el cabello en tu cabeza."
    n 4flran "¿Por qué {i}tiene{/i} que ser tan diferente para el cabello en cualquier otro lugar?"
    n 4fcsan "Dame un descanso."

    n 1fnmfl "Oh -{w=0.5}{nw}"
    extend 3fsqwr " ¿y mencioné cuánto tienes que pagar por el privilegio?"
    n 3fbkwr "¡Ni siquiera importa lo que uses!"
    n 7fllem "¿Esas rasuradoras con las partes reemplazables en el final?{w=0.75}{nw}"
    extend 3fcswr " ¡Espero que disfrutes exprimir tanto de cada una como puedas para ahorrar en los repuestos!"
    n 6csqem "¿Yendo por desechables?{w=0.75}{nw}"
    extend 3flrem " Sí,{w=0.2} porque yo{w=0.2}{nw}"
    extend 4fsrem " {i}totalmente{/i}{w=0.2}{nw}"
    extend 4fsqan " disfruto vaciar la basura justo como vacían mi cuenta de banco."
    n 2fslem "...Para nada."
    n 2fnmgs "¡Incluso las estúpidas eléctricas elegantes no ayudan!{w=0.75}{nw}"
    extend 4fbkwr " ¡Son incluso {i}más{/i} caras que todo lo demás!"
    n 4fcsan "Y todos sabemos cuánta diversión es tener {i}otra{/i} cosa que se queda sin batería."
    n 6ftrem "'¡Nuestra afeitada más cercana nunca!'.{w=0.75}{nw}"
    extend 3fsrem " Sí,{w=0.2} claro.{w=0.75}{nw}"
    extend 3fsran " Más como afeitando todos tus ahorros."
    n 3fcsemesi "..."

    n 3fcssl "Je.{w=0.75}{nw}"
    extend 7fsqfl " ¿Y cualquier cosa que hagas?{w=0.75}{nw}"
    extend 7fslun " {i}Nunca{/i} se siente como que obtendrás el tipo de afeitada que querías en primer lugar."
    n 1fcsfl "Sí,{w=0.2} sí.{w=0.75}{nw}"
    extend 4fcsgs " Di lo que quieras,{w=0.2} [player].{w=0.75}{nw}"
    extend 2csrfl " Lo he escuchado todo antes."
    n 2ftlgs "'¡Solo tienes que dejar que tu piel se remoje,{w=0.2} Natsuki!.'{w=0.75}{nw}"
    extend 6ftrwr " '¡Es fácil!{w=0.2} ¡Solo sigue el grano!.'{w=0.75}{nw}"
    extend 3flrem " '¡No olvides enjabonarte cada vez!.'{w=0.75}{nw}"
    extend 4fcsan " ¡Como si pensaran que no he {i}intentado{/i} eso ya!"
    n 2fllem "Como...{w=1}{nw}"
    extend 2fslan " ¡Va{w=0.5}{nw}{i}mos{/i}!{w=0.75}{nw}"
    extend 2fsqwr " ¿Se supone que esto sea una rutina matutina?{w=1}{nw}"
    extend 1fbkwrean " ¿O algún tipo de ritual de culto?"
    n 1fslsl "Al menos un ritual no deja tus piernas luciendo como una zona de guerra tampoco."
    n 2fcsem "Ugh..."

    if already_discussed_shaving:
        n 2clrsllsbl "..."
        n 2ccsajlsbl "...M-{w=0.2}mira.{w=0.75}{nw}"
        extend 4cllfl " No voy a ir con todo y trabajarme sobre todo esto.{w=0.75}{nw}"
        extend 4cslfl " De nuevo."

        if Natsuki.isEnamored(higher=True):
            n 7ccsssl "I-{w=0.2}incluso si no puedes tener suficiente del sonido de mi voz."
        else:

            n 3ccsca "No es como que solo quejarse sobre algo haya logrado algo de todas formas."
    else:

        n 2csrpu "Creerías que algo con lo que prácticamente todos han tenido que lidiar por tanto tiempo realmente estaría {i}resuelto{/i} por ahora,{w=0.5}{nw}"
        extend 2csqsl " ¿verdad?"
        n 1ccsflesi "..."
        n 1cslsl "..."
        n 3ccstr "Muy bien,{w=0.2} mira.{w=0.75}{nw}"
        extend 3cllfl " Ya he seguido sobre esto suficiente tiempo.{w=0.75}{nw}"
        extend 7cslfl " Y realmente no quiero {i}afeitarse{/i} de todas las cosas viviendo gratis en mi cabeza de nuevo."

    n 3clraj "Así que...{w=1}{nw}"
    extend 3ccsaj " Solo voy a decir esto."

    $ chosen_descriptor = "bebé" if Natsuki.isLove(higher=True) else player
    if already_discussed_shaving:
        n 4ulrfl "Como dije antes.{w=0.75}{nw}"
        extend 4tnmsl " Realmente no me importa ni nada si te afeitas o no,{w=0.2} [chosen_descriptor].{w=0.75}{nw}"
    else:

        n 4ccspu "No me importa particularmente ni nada si te afeitas o no,{w=0.2} [chosen_descriptor].{w=0.75}{nw}"

    extend 7ccsfll " E-{w=0.2}esa es tu decisión,{w=0.2} obviamente."
    n 7cllajl "No voy a pensar menos de alguien que no quiera pasar por todo de...{w=1}{nw}"
    extend 3csleml " Eso."
    n 3cslsl "..."
    n 3cllaj "Pero...{w=1}{nw}"
    extend 7tnmpu " ¿Si {i}tú{/i} de alguna manera tienes algún tipo de rutina matutina mágica que {i}realmente{/i} funciona para ti?"
    n 1ccsss "...Je."
    n 2fcsbgsbr "Entonces espero que sepas justo con quién tienes que compartirla primero,{w=0.2} por si acaso."
    n 2fchbgsbr "¡E-{w=0.2}eso es todo lo que digo!"

    if Natsuki.isLove(higher=True):
        n 2ccsbgl "Y además,{w=0.2} [player].{w=0.75}{nw}"
        extend 4csqsml " ¿N-{w=0.2}no es eso justo lo que hacen las parejas?"
        n 3fcssml "Ehehe."
        n 3fchblleaf "¡T-{w=0.2}te amo también,{w=0.2} [player]!"

    elif Natsuki.isEnamored(higher=True):
        n 2fcsbgl "Y-{w=0.2}y además,{w=0.2} [player].{w=0.75}{nw}"
        extend 6fcssmlesm " Sabes lo que dicen."
        n 3fsqssl "Compartir es cuidar,{w=0.2} ¿verdad?"
        n 4fcssml "Ehehe."
        $ chosen_tease = jn_utils.getRandomTeaseName()
        n 3fchgnl "¡Muchas gracias,{w=0.2} gran [chosen_tease]!"

    elif Natsuki.isAffectionate(higher=True):
        n 2fcsss "Y además,{w=0.2} [player].{w=0.75}{nw}"
        extend 7fsqss " ¿Si no lo haces?{w=1}{nw}"
        extend 7tlraj " Bueno..."
        n 3fcsbg "Solo digamos que te mostraré una afeitada {i}realmente{/i} cercana en su lugar."
        n 3fsqsm "Ehehe."
        n 3fchgn "¡Apreciado,{w=0.2} [player]!"
    else:

        n 2fsqsm "Ehehe."
        n 7fchgn "¡M-{w=0.2}muchas gracias,{w=0.2} [player]!~"

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
