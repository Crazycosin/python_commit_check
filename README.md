# python_commit_check
a demo about python program commit check

## check process
1.来保证代码风格正确
   ```bash
   pre-commit install  # 只在第一次运行
   pre-commit run --all-files
   ```

2.来查看单元测试覆盖率　
   ```bash
   coverage run --source demo --omit demo/version.py -m pytest tests/
   coverage report -m
   ```

3.生成docstring文档
   ```bash
   cd docs
   sphinx-apidoc -o . ../demo -f
   make clean
   make html
   ```
   然后用浏览器打开`docs/build/html/index.html`查看自己新增的docstring是否在**API Document**是否渲染正确。
