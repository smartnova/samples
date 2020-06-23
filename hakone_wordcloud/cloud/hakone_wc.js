$(() => {
  const topics = ['00-03', '00-05', '01-03', '02-00', '03-00', '04-00', '04-02', '05-01', '06-03', '07-00', '07-03', '08-00', '08-02', '08-04', '09-00', '10-00', '11-03', '12-00', '13-00', '14-02', '14-05', '15-01', '16-00', '16-02', '17-00', '18-01', '19-00', '19-04'];

  const topics0 = ['06-03', '04-02', '04-00', '00-05', '00-03', '05-01', ];

  $body = $('body');

  $cloud0 = $('<div id="cloud0"/>');
  $body.append($cloud0);

  let svg_loaded = 0;

  for (topic in topics0) {
    console.log(topic);
    let $span = $('<span id ="' + topics0[topic] + '">');
    $cloud0.append($span);
    let svg_fname = 'topic' + topics0[topic] + '.svg';
    $span.load(svg_fname, () => { svg_loaded++;
      if (svg_loaded == topics0.length) {
        $('#cloud0 svg').each((i, svg) => {
          console.log('#cloud0 svg', i)
          $svg = $(svg);
          $svg.attr('width', 200);
          $svg.attr('height', 200);
          $svg.attr('viewBox', '0 0 900 900');
        });
        $('text').each((i, text) => {
          $(text).hover(() => {
            const $text = $(text);
            $word.text($text.text());
            $word.css('font-size', $text.attr('font-size') + 'px');
            $word.css('color', $text.css('fill'));
          });
        });
      }
    });
  }

  const $word = $('<p>word</p>');
  $body.append($word);
});
