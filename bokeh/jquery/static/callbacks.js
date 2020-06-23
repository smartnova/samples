$(() => {
  const $utterances = $('div[name="utterances"]');
  for (var i = 0; i < 10; i++) {
    $('<p>').append($(`<span>#{i} - <b>speaker ${i%3}</b>: Utterance #{i}</span>`)).appendTo($utterances);
  }
})

function buffer_on_change() {
  console.log('buffer_on_change', $('input[name="buffer"]').text());
}
