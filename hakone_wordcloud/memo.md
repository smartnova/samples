# PyPI アカウントを登録。

- [本番用](https://pypi.python.org/pypi?%3Aaction=register_form)

# 配布物の作成

```
rm -rf build *.egg-info dist
python setup.py sdist bdist_wheel
```

# テスト

```
venv empty
pip install ****/dist/*.tar.gz
```

ちゃんと動作するかテスト

# 本番用

```
twine upload --repository pypi dist/*
https://pypi.org/project/hakone_wordcloud_snkw/
pip --no-chache-dir install --upgrade hakone_wordcloud_snkw
```

# 参考文献
- [PyPIパッケージ公開手順](https://qiita.com/shinichi-takii/items/e90dcf7550ef13b047b5)

    わかりやすい。認証情報の設定については、この人が勧めるアカウントの認証情報の生設定ではなく、API Token を設定すること。

    永野くんによればテストサイトは使わないらしい。
