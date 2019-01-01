
function makeFader(track, name, id, media_prefix) {
            var player = new Tone.Player(media_prefix + track);
            //player.loop = true;
            var soloCtrl = new Tone.Solo();
            var panVol = new Tone.PanVol();
            player.chain(panVol, soloCtrl, Tone.Master);
            all_synced.push(player);
            all_ids.push(id);
            all_players.push({
                "player": player,
                "id": id,
                "panVol": panVol,
                "solo": soloCtrl
            });
            var container = $("<div>", {
                "class": "Group"
            }).appendTo('#Sliders');

            $("<div>", {
                "class": "Title",
                "text": name
            }).appendTo(container);

            $("<div>", {
                "align": "center",
                "id": "StartStopInputs" + id
            }).appendTo(container);

            var CurrentStartStopInputs = $("#StartStopInputs" + id);

            $("<span>", {
                "text": "Start:"
            }).appendTo(CurrentStartStopInputs);

            ($("<input>", {
                "type": "number",
                "id": "timingStart" + id,
                "min": "0",
                "max": "600",
                "value": "0",
                "step": "0.01",
            })).appendTo(CurrentStartStopInputs);

            //$("<br><br>").appendTo(CurrentStartStopInputs);

            $("<span>", {
                "text": " Stop:"
            }).appendTo(CurrentStartStopInputs);

            ($("<input>", {
                "type": "number",
                "id": "timingStop" + id,
                "min": "0",
                "max": "600",
                //"value": "0",
                "step": "0.01",
            })).appendTo(CurrentStartStopInputs);
            $("<br><br>").appendTo(CurrentStartStopInputs);

            Interface.Slider({
                param: "volume",
                name: "volume",
                parent: container,
                tone: panVol,
                axis: "y",
                exp: 0.5,
                max: 6,
                min: -60,
            });

            Interface.Slider({
                param: "pan",
                name: "pan",
                parent: container,
                tone: panVol,
                min: -1,
                max: 1,
            });

            var btnDiv = $("<div>", {
                "class": "row offset-md-1",
            }).appendTo(container);

            Interface.Button({
                parent: btnDiv,
                type: "toggle",
                text: "solo",
                activeText: "solo",
                class: "col-md-5",
                start: function () {
                    soloCtrl.solo = true;
                },
                end: function () {
                    soloCtrl.solo = false;
                },
            });

            $("<div>", {
                "class": "col-md-1  ",
            }).appendTo(btnDiv);

            Interface.Button({
                parent: btnDiv,
                type: "toggle",
                text: "mute",
                class: "col-md-5",
                activeText: "mute",
                start: function () {
                    player.mute = true;
                },
                end: function () {
                    player.mute = false;
                },
            });
        }