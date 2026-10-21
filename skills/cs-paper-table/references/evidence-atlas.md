# 表格证据图谱：从具体论文学习可复用的设计判断

本库包含 **54 篇独立论文／技术报告、95 个独立目视检查的表格锚点、9 个公司分组**，检查日期为 **2026-10-21**。每个公司分组各 6 篇。计数由实际 PDF SHA256、规范化作品标识、打印表号和物理页码重新核验；详细结果见 [校验记录](evidence/catalog-validation.json)。

这是一组以表格类型和科学表达任务为目标的定向样本。它不构成“顶级论文”或期刊／会议排名，也不能推出任何公司的统一字体、配色或表格规范。机构分组保留了原始 affiliation 证据和合作关系。52 篇通过此前的图形语料定位，另补入 2 篇；**此前的 figure 检查不计作 table 检查**，也不声称已检查此前全部 120 篇论文的表格。

## 如何使用证据

先按实验含义选表格结构，再查询相近的实证例子。每条记录明确区分：

| 层级 | 可以从中获得什么 | 不能据此声称什么 |
|---|---|---|
| `measured` | PDF 的名义字号、字体程序、对象色值／透明度、线宽、坐标及说明过算法的布局统计 | 原始 TeX 命令、真实行内边距、字体授权、推荐最小字号、视觉重要性 |
| `observed` | 目视读到的表头层级、对齐外观、比较条件、强调含义、缺失状态、图注／表注语义 | 未显示的统计显著性、隐藏精度、统一公司风格 |
| `recommended` | 从具体例子推导出的设计建议与反例警告 | 作者、公司或会议的正式政策 |

完整 JSON 把三层存为独立字段；原始研究笔记保留逐表观察、测量、经验和局限。分发版测量记录省略源论文逐字提取文本，保留字体、字号、颜色／透明度、坐标、字符数等样式属性与全部数值。不要把“测到了某个值”直接改写为“新表应该采用这个值”。

## 覆盖范围与年份统计

`year` 采用研究记录中的首次公开／报告年份，检索版本可晚于该年。各组样本量是选择设计的一部分，不能当作各公司论文总产量。完整来源和版本见 [paper-corpus.csv](paper-corpus.csv)，每表位置见 [table-corpus.csv](table-corpus.csv)。

| 公司分组 | 2025 论文 | 2026 论文 | 论文合计 | 2025 表格 | 2026 表格 | 表格合计 |
|---|---:|---:|---:|---:|---:|---:|
| OpenAI | 4 | 2 | 6 | 8 | 2 | 10 |
| Anthropic | 3 | 3 | 6 | 4 | 5 | 9 |
| Microsoft Research | 4 | 2 | 6 | 8 | 6 | 14 |
| Google / DeepMind | 4 | 2 | 6 | 6 | 4 | 10 |
| Meta / FAIR | 4 | 2 | 6 | 7 | 3 | 10 |
| NVIDIA | 2 | 4 | 6 | 3 | 7 | 10 |
| DeepSeek | 2 | 4 | 6 | 2 | 8 | 10 |
| Alibaba / Qwen | 2 | 4 | 6 | 3 | 7 | 10 |
| Tencent | 5 | 1 | 6 | 9 | 3 | 12 |
| **合计** | **30** | **24** | **54** | **50** | **45** | **95** |

Hunyuan-A13B 的报告封面日期为 2025-06-27，所检查的 arXiv 上传日期为 2026-09-23，因此计入 2025，而不是从 arXiv 编号推断为 2026。原始日期说明和 [官方仓库证据](https://github.com/Tencent-Hunyuan/Hunyuan-A13B)已保留。

唯一未计入的已下载筛查替代项是 *Natural Emergent Misalignment from Reward Hacking in Production RL*：当时仅进行了文本筛查，没有选出真正的编号源表格；示例对话内提及的 table 不计入表格检查。该组改补官方 Claude Sonnet 5 system card。另一新增来源为 Hunyuan-A13B。

## 关键规则及其证据锚点

下面的“规则”是本技能的推荐判断；引用指向被检查的具体表格，不把推荐反向归因给作者。一个表可以支持结构借鉴，同时暴露需要修正的表达问题。

| 推荐判断 | 观察依据与具体锚点 |
|---|---|
| 先确定表的科学角色，再选列类型和层级。统计描述、能力覆盖、训练配置和结果比较需要不同结构。 | [HealthBench Table 1，PDF p. 4](https://arxiv.org/pdf/2505.08775v1#page=4) 是描述性统计；[Phi-4 Reasoning Vision Table 2，PDF p. 5](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/03/Phi-4-reasoning-vision-15B-Tech-Report.pdf#page=5) 是配置／能力矩阵；[PaperBench Table 2，PDF p. 5](https://arxiv.org/pdf/2504.01848v3#page=5) 展示另一种任务覆盖组织。 |
| 排名只在事先定义的可比组内进行。保留数据集、模型版本、预算、推理条件、子集与单位。 | [Engram Table 1，PDF p. 9](https://arxiv.org/pdf/2601.07372v1#page=9) 显示受控预算与额外扩展条件；[SWE-Lancer Table 1，PDF p. 7](https://arxiv.org/pdf/2502.12115v4#page=7) 的任务及测评条件影响解释；[Qwen3.8-Next Table 8，PDF p. 15](https://arxiv.org/pdf/2608.30320v1#page=15) 区分预算重分配和新增容量。 |
| 为加粗／下划线声明用途、范围、指标方向和并列规则；不要自动把粗体解释为显著优胜。 | [DeepSeek-V4 Table 1，PDF p. 28](https://arxiv.org/pdf/2606.19348v1#page=28) 定义 0.3 的显示强调容差；[Qwen3-VL Table 2，PDF p. 15](https://arxiv.org/pdf/2511.21631v1#page=15) 使用 reasoning／non-reasoning 的不同排名池；[Astra Table 1，PDF p. 11](https://deploymentsafety.openai.com/gpt-6-astra/gpt-6-astra.pdf#page=11) 强调焦点模型列。 |
| 消融设计必须声明独立移除、累积增加、因素矩阵或独立面板；“+”标签不等于数值增量。 | [Fara Table 4，PDF p. 9](https://arxiv.org/pdf/2511.19663v1#page=9) 与 [Nemotron Diffusion Table 1，PDF p. 4](https://arxiv.org/pdf/2607.05722v1#page=4) 呈现累积设计；[SAM 3 Table 9，PDF p. 10](https://arxiv.org/pdf/2511.16719v1#page=10) 将独立实验并列。 |
| 把统计不确定性、增量、分位数和替代评估值作为不同数据类型；未说明的 ± 不补造 SD／SE／CI 或 n。 | [HunyuanVideo 1.5 Table 7，PDF p. 11](https://arxiv.org/pdf/2511.18870v1#page=11) 的时间 ± 未在所查上下文明确类型；[Qwen3.8-Next Table 6，PDF p. 12](https://arxiv.org/pdf/2608.30320v1#page=12) 的下标是配对增量；[Qwen3-ASR Table 2，PDF p. 5](https://arxiv.org/pdf/2601.21337v1#page=5) 包含 p95 延迟。 |
| 缺失状态要有类型。未评估、不适用、不支持、训练重叠而省略和 OOM 均不等于零。 | [Hidden Objectives Table 2，PDF p. 50](https://arxiv.org/pdf/2503.10965v2#page=50) 与 [WorldMirror Table 3，PDF p. 7](https://arxiv.org/pdf/2510.10726v1#page=7) 展示需要解释的省略；[HY-World 2.0 Table 14，PDF p. 37](https://arxiv.org/pdf/2604.14268v1#page=37) 保留 OOM 和资源条件。 |
| 精度跟随量的定义；保留整数计数、单位、指标方向、百分点与百分比、解析估计与实测的区别。 | [Qwen3.8-Next Table 5，PDF p. 11](https://arxiv.org/pdf/2608.30320v1#page=11) 对 loss 与分数采用不同精度；[DeepSeek-OCR 2 Table 4，PDF p. 11](https://arxiv.org/pdf/2601.20552v1#page=11) 的率差需要百分点解释；[Native Sparse Attention Table 4，PDF p. 14](https://arxiv.org/pdf/2502.11089v1#page=14) 报告预期解析加速比。 |
| 默认用少量横线表达层级；根据语义边界决定是否加入局部竖线或网格，避免把“无竖线”写成绝对禁令。 | [Gemma 4 Table 5，PDF p. 5](https://arxiv.org/pdf/2607.02770v2#page=5) 使用分组短横线；[Hidden Objectives Table 2，PDF p. 50](https://arxiv.org/pdf/2503.10965v2#page=50) 需要关联长文字；[Claude Sonnet 5 Table 4.1.1.A，PDF p. 37](https://www-cdn.anthropic.com/283ef97c476cf442c91d9a37d5b214242a55bb92/Claude%20Sonnet%205%20System%20Card.pdf#page=37) 是采用网格的报告式例子。 |
| 颜色要有可解释的角色，并以文字、标签或其他通道保留含义；链接色、焦点色、基线色和增量色不能混用。 | [Engram Table 1，PDF p. 9](https://arxiv.org/pdf/2601.07372v1#page=9) 灰色表示另一预算条件；[DeepSeek-OCR 2 Table 1，PDF p. 9](https://arxiv.org/pdf/2601.20552v1#page=9) 区分数据增量蓝与引用蓝；[HY-World 2.0 Table 7，PDF p. 27](https://arxiv.org/pdf/2604.14268v1#page=27) 用淡色标记基线／选定设置。 |
| 将最终宽度下的可读性作为独立验收。先考虑拆表、缩短标签、迁移注释、转置或改变版面，再缩字号。 | [PerceptionLM Table 9，PDF p. 14](https://arxiv.org/pdf/2504.13180v3#page=14) 的主导字形名义大小仅约 4.483 pt；[Qwen3-VL-Embedding Table 2，PDF p. 11](https://arxiv.org/pdf/2601.04720v1#page=11) 有约 0.099 pt 的细线；[Nemotron 3 Super Table 5，PDF p. 31](https://arxiv.org/pdf/2604.12374v1#page=31) 提供较大字号的高表格方案。 |
| 把表注当作测量定义的一部分；检查方向、聚合、比较条件和强调图例，不能只复制可见形状。 | [SkillOpt Table 6，PDF p. 14](https://arxiv.org/pdf/2605.23904v2#page=14) 与 [Automated Alignment Researchers Table 3，PDF p. 44](https://www-cdn.anthropic.com/7b1c44894e980876479947dcdd40716278aeeffd/automated-alignment-researchers-august-2026.pdf#page=44) 的统计／条件需结合说明；[DeepSeek-OCR 2 Table 1，PDF p. 9](https://arxiv.org/pdf/2601.20552v1#page=9) 的 reading-order edit 箭头与改善增量存在表面不一致，适合作为需核查的反例。 |

## 字体、线宽和颜色的代表样本

以下是 **PDF 名义对象测量值，不是制作默认值**。字号取所选表体内可见字符贡献最多的字体程序；小型表中它可能是粗体表头。数值仅在此处四舍五入为三位小数，完整精度保留在 JSON 中。线宽列标注统计范围：“全描边”可能包含数字下划线；“长横线候选”由几何筛选得到。所有本节列出的颜色样本 opacity 均为 1.0。

| 来源锚点 | 主导字体程序／名义字号（pt） | 名义线宽（pt）及范围 | 测得的颜色与观察到的作用 |
|---|---|---|---|
| [Astra Table 1，PDF p. 11](https://deploymentsafety.openai.com/gpt-6-astra/gpt-6-astra.pdf#page=11) | `OpenAISans-Regular` / 9.775 | 0.535, 0.857（全描边） | 底色 `#F3F3F1`，交替中性条带；焦点列加粗另有含义。 |
| [gpt-oss Table 3，PDF p. 11](https://arxiv.org/pdf/2508.10925v1#page=11) | `SFRM1000` / 9.963 | 0.398, 0.542, 0.868（全描边） | 黑色文本和线；与同组 Astra 的字体和条带明显不同。 |
| [Claude Sonnet 5 Table 4.1.1.A，PDF p. 37](https://www-cdn.anthropic.com/283ef97c476cf442c91d9a37d5b214242a55bb92/Claude%20Sonnet%205%20System%20Card.pdf#page=37) | `Lora-Bold` / 10.995 | 0.750（全描边） | 深色表头 `#141413`、浅色区 `#DEDCD1`，另有白字；不是通用论文配色。 |
| [Phi-4 Reasoning Vision Table 2，PDF p. 5](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/03/Phi-4-reasoning-vision-15B-Tech-Report.pdf#page=5) | `URWPalladioL-Roma` / 8.966 | 0.498, 0.797（全描边） | 黑色文字／线，无填色；符号字体另列在完整记录。 |
| [SkillOpt Table 1，PDF p. 7](https://arxiv.org/pdf/2605.23904v2#page=7) | `LMRoman8-Regular` / 7.970 | 0.327, 0.398, 0.545, 0.873（全描边） | 淡色 `#EBEBFF`；数值文本含 `#0E8A4A` 与 `#B91C1C`，须结合增量含义。 |
| [Gemma 4 Table 5，PDF p. 5](https://arxiv.org/pdf/2607.02770v2#page=5) | `XCharter-Roman` / 10.909 | 0.325, 0.542, 0.868（长横线候选） | 黑色，无数据填色；短横线表达列组。 |
| [PerceptionLM Table 9，PDF p. 14](https://arxiv.org/pdf/2504.13180v3#page=14) | `NimbusRomNo9L-Regu` / 4.483 | 0.224, 0.359（长横线候选） | 模态带 `#C0DFDB`／`#D9CAEF`／`#E5E6E5`；链接色另属来源信息。 |
| [Cosmos 3 Table 10，PDF p. 51](https://arxiv.org/pdf/2606.02800v4#page=51) | `XCharter-Roman` / 7.551 | 0.453, 0.755, 1.208（长横线候选） | 焦点列 `#E8F4E0`，另有 `#F5F5F5`；长横线与下划线须分开。 |
| [Engram Table 1，PDF p. 9](https://arxiv.org/pdf/2601.07372v1#page=9) | `URWPalladioL-Roma` / 8.966 | 0.542, 0.868（长横线候选） | 次要预算条件文字／线 `#7F807F`；灰色不代表差值小或统计不显著。 |
| [DeepSeek-OCR 2 Table 1，PDF p. 9](https://arxiv.org/pdf/2601.20552v1#page=9) | `URWPalladioL-Roma` / 8.966 | 0.542, 0.897（长横线候选） | 增量字 `#0000FF`，引用字 `#1976D2`；无背景填色。 |
| [Qwen3-VL-Embedding Table 2，PDF p. 11](https://arxiv.org/pdf/2601.04720v1#page=11) | `URWPalladioL-Roma` / 6.841 | 0.099, 0.165, 0.264（长横线候选） | 正文黑色；`#000080` 为引用来源色，不是得分热图。 |
| [HY-World 2.0 Table 7，PDF p. 27](https://arxiv.org/pdf/2604.14268v1#page=27) | `NimbusRomNo9L-Regu` / 7.970 | 0.498, 0.797（长横线候选） | 角色底色 `#FFE5E5`／`#E5E5FF`；它们是实心淡色，并非半透明。 |

同一公司分组内存在多种出版模板、字体与强调语义。样本中的紧凑表格可以提供组织信息的思路，但其最小字号、最细线宽、专有字体和颜色不应成为新表的盲目目标。完整对象坐标、颜色成分、opacity、字符数和 path 数量见每表分发版样式测量；对象数量不等于面积占比，也不自动说明视觉重要性。

## 检索与可携带格式

从技能根目录运行，无额外 Python 依赖：

```bash
python scripts/search_corpus.py --company DeepSeek --year 2026 --query tie --limit 2
python scripts/search_corpus.py --company Tencent --query "uncertainty timing" --limit 1
python scripts/search_corpus.py --company Google --query memory --limit 3 --format json
```

`--company` 支持不区分大小写的子串和常见中英文机构别名，可重复；`--year` 也可重复。公司条件内部为 OR，年份内部为 OR，不同条件之间为 AND。`--query` 的词／引号短语必须全部出现，按角色、建议和观察中的相关性排序；原始逐表笔记主要用英文，因此可用 `ablation`、`uncertainty`、`tie`、`latency`、`memory` 等关键词。`--limit` 为正整数，默认 5。Markdown 输出精选观察及完整建议／警告；`--format json` 返回完整对应表格记录和论文来源信息。

JSON 主索引采用 `papers[]` 与扁平 `tables[]`。`paper_id`、打印 `anchor`、物理 `page_1based`、版本和 `pdf_sha256` 联合定位证据；`coordinates` 同时保留显示裁剪、表体范围和原始测量范围。`source_page_url` 的 `#page=N` 便于跳转，但应根据打印表号确认表格。`measurement_method.measurement_records` 指向可移植的样式属性测量 JSON，不含源表逐字文本副本。

三组完整研究笔记：

- [OpenAI / Anthropic / Microsoft：18 篇、33 表](evidence/openai-anthropic-microsoft.md)；[结构化记录](evidence/openai-anthropic-microsoft.json)。
- [Google / DeepMind / Meta / NVIDIA：18 篇、30 表](evidence/google-meta-nvidia.md)；[结构化记录](evidence/google-meta-nvidia.json)。
- [DeepSeek / Tencent / Alibaba：18 篇、32 表](evidence/deepseek-tencent-alibaba.md)；[结构化记录](evidence/deepseek-tencent-alibaba.json)。

测量选择规则、PyMuPDF 版本、字体可见性局限、长线／基线的不同算法以及复现命令见 [measurement-method.md](evidence/measurement-method.md)。所有坐标使用未旋转物理页左上角为原点的 PDF points；1 pt = 1/72 inch。正文裁剪和含表注裁剪不能混用：Google / Meta / NVIDIA 的原始向量直方图含表注，而其字体汇总另在表体范围提取。另两组原始对象测量采用表体范围。

## 需要保留的局限和反例

样本按覆盖目的选择，未进行随机抽样，也没有按期刊、会议或引文建立质量排名。技术报告、system card 与研究论文的排版约束不同，不能从“六篇来自同一公司”推出该公司的稳定家族风格。检查内容针对表格表达，未重新执行实验或认证任何性能主张。

原始 PDF 的对象属性不等于最终可见结果：文字可能被裁剪或遮挡，背景可能改变颜色，细线可能是填充矩形，文字可能已被轮廓化。精确测量必须与实际渲染相互核对。基线间距算法在各研究中不同，不能直接合并为统一行高统计；测得的居中外观也不能证明作者用了某一种 TeX 列格式。

源表亦可能不完整或不一致。[Hunyuan-A13B Table 3，PDF p. 9](https://arxiv.org/pdf/2609.27284v1#page=9) 中相同显示值 44.6 出现不同排名强调；可见证据不能判断它来自隐藏精度还是不一致的并列规则。[HunyuanVideo 1.5 Table 7，PDF p. 11](https://arxiv.org/pdf/2511.18870v1#page=11) 的 ± 类型未明确，[DeepSeek-OCR 2 Table 1，PDF p. 9](https://arxiv.org/pdf/2601.20552v1#page=9) 的 reading-order edit 方向存在需要核查的表面矛盾。新表应明确解决这些问题，不把它们复制成规范。详见各表 `cautions` 和原始笔记。

本库保存 95 份 PDF 对象样式测量的分发版记录与 30 份补充布局报告，共 125 个测量文件，**仍然对应 95 个表格锚点**。分发原则为 `distribution omits extracted source text; style properties retained`：省略 `text_in_pdf_order` 等逐字提取字段，保留测量样式属性、全部数值及方法。不打包源论文 PDF、原论文截图或字体二进制，原创观察和设计分析保持完整。重新下载时先核对版本与 SHA256；如果官方 URL 的内容已更新，应重新定位和检查，不默认旧坐标仍适用。

