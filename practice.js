var detail = "hoge";
// :の後に型名を指定（指定がない場合も初期値で決定）
// anyにするとなんでも受け入れちゃう
detail = "foo";
// detail = 100; ←エラーになる
var nums = 100;
nums = 0xFF; //16進数（x）
nums = 438; //8進数（o）
nums = 185; //2進数(b)
nums = 3E5; //指数？
var mail = "hogehoge@gmail.com";
var msg = "\u30D0\u30C3\u30AF\u30AF\u30A9\u30FC\u30C8\uFF08shift+@\uFF09\u3067\u56F2\u3046\u3068\n\u6539\u884C\u3068\u304B\u306E\u51E6\u7406\u3092\u52DD\u624B\u306B\u3057\u3066\u304F\u308C\u308B\u4E0A\u306B\n\u5909\u6570\u3092\u305D\u306E\u307E\u307E\u57CB\u3081\u8FBC\u3081\u308B\u3088\uFF01\u30E1\u30FC\u30EB\u306F\u3053\u3061\u3089\u2192" + mail;
function show(result) {
    return result + "\u306Fstring\u578B\u3067\u3059";
}
;
// console.log(show(100)); ←数値型を渡すと当然エラー
console.log(show(100)); //anyかstring型にしちゃう
console.log(show("100")); //as 型名 でもおｋ
var DATA = [1, 2, 3]; //constは定数の宣言（大文字にすることが多いよ
// DATA = [4, 5, 6]; 再代入しようとするとエラー
DATA[0] = 10; // 中身の要素だけ書き換えはできる！
var data = ["Java", "Python", "PHP"];
// 配列のときは型名の後に[]をつけないとダメだよ！
var data2 = [["Java", "Python", "PHP"], ["JavaScript", "HTML", "CSS"]];
// 入れ子にするときは次元の数だけ[]を指定！
// new Array(要素数)or(要素, 要素…)でも定義できるけど扱いづらい
var obj = {
    // 連想配列（Pythonでいうところの辞書）indexの部分はほかの名前でもいいよ
    "usa": "usako",
    "kato": "kato",
    "mya": "myako"
};
console.log(obj.usa);
console.log(obj["usa"]);
