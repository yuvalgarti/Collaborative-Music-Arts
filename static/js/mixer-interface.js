function create_mixer_interface() {
    var timeSlider;
    var dragging;
    var play_btn;
    timeSlider = Interface.Slider({
        name: "At: 0.00",
        drag: function (val) {
            Tone.Transport.seconds = val;
            timeSlider.name[0].innerHTML = "At: " + Number(val).toFixed(2);
        },
        start: function () {
            dragging = true;
        },
        end: function () {
            dragging = false;
        }
    });
    var transport;
    transport = Interface.TransportInSeconds({
        start: function () {
            var curr_pos = Number(Tone.Transport.seconds).toFixed(2);
            if (!dragging && curr_pos < timeSlider.max) {
                this.position.text(curr_pos);
                timeSlider.value(curr_pos);
                timeSlider.name[0].innerHTML = "At: " + curr_pos;
            }
            if (curr_pos >= timeSlider.max) {
                play_btn._end();
            }
        }
    });

    play_btn = Interface.Button({
        type: "toggle",
        text: "Start",
        activeText: "Stop",
        start: function () {
            var max_duration = 0;
            for (var i = 0; i < all_players.length; i++) {
                var timingStart_id = $("#timingStart" + all_players[i]['id']).val();
                var timingStop_id = $("#timingStop" + all_players[i]['id']).val();
                all_players[i]['player'].unsync();
                all_players[i]['player'].sync().start(timingStart_id);
                if (timingStop_id !== "") {
                    all_players[i]['player'].sync().stop(timingStop_id);
                }
                if (max_duration < Number(all_players[i]['player'].buffer._buffer.duration) + Number(timingStart_id)) {
                    max_duration = Number(all_players[i]['player'].buffer._buffer.duration) + Number(timingStart_id);
                }
            }

            timeSlider.max = max_duration;
            Tone.Transport.start();
            if (Tone.context.state !== 'running') {
                Tone.context.resume();
            }
        },
        end: function () {
            Tone.Transport.stop();
            timeSlider.value(0);
            timeSlider.name[0].innerHTML = "At: 0.00";
        },
    });
}