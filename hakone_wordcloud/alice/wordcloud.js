$(() => {
  $body = $('body');

  $alice = $('<div id="alice"/>');
  $body.append($alice);

  const $word = $('<p>word</p>');
  $body.append($word);

  $alice.load('alice.svg', () => {
    /** SVG 表示の大きさを変更する仕掛け
      * 「The SVG Scaling Toolbox」節を参照 (https://css-tricks.com/scale-svg/)
      * width, height: 表示するときの画面上でのピクセル数
      * viewBox: SVG の中で使われている論理的な座標系にしたがって表示すべき領域を指定している。
      */
    $('#alice svg').each((i, svg) => {
      $svg = $(svg);
      $svg.attr('width', 500);
      $svg.attr('height', 500);
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
  });
});
