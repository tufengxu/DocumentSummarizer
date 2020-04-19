#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
from doc_summarizer.textteaser_Chinese import TextTeaserChinese


def test():
    title = "山东济南楼市新规：优先满足刚需购房 不得要求全款买房"
    text = '''来自山东齐鲁晚报下属的齐鲁壹点网站的消息，4月26日，山东省济南市城乡建设委员会发布《关于进一步规范商品房销售行为的通知》（以下简称“《通知》”），该通知主要针对各房地产开发企业、房产中介及承销机构，意在规范相关方的商品房销售行为。　　《通知》要求，销售商品房时，应优先满足无住房记录的刚性购房者需求。不得要求购房人一次性付款或一次性付款优先选房，不得拒绝购房人正常使用住房公积金或商业个人贷款购房，不得要求住宅销售捆绑车位及地下室。　　住宅项目申请商品房预售许可证时，应提交销售方案。销售方案包括：房源信息、销售方式、付款方式、意向购房者组成（30%首付、60%首付、全款客户占比情况）。销售方案审批通过后，向社会公示。　　商品住宅项目形象进度满足预售要求的，应当一次性申请预售。　　在取得《商品房预售许可证》后，应本着公开、公平、公正的原则对外销售。一次性公开全部准售房源，公示销售进度控制表，在销售现场醒目位置明码标价，并告知所有购房者。　　对于违反规定的相关房地产开发企业，将依法责令立即整改，拒不整改的，依法予以行政处罚，记入房地产开发企业信用档案，向社会公示。整改完成前，暂停项目合同网签及后续预售审批项目的办理。　　《通知》发布的背景则为，近期，济南市城乡建设委员会接到多份来自“12345”市民热线转办及市民群众来电来信，反映济南市部分热点区域住宅项目存在全款购房、全款优先选房、拒绝使用商业贷款或个人公积金贷款等歧视刚性需求购房者，以及住宅销售捆绑车位、地下室销售等行为，这些行为严重扰乱了房地产市场秩序，造成了极其恶劣的社会影响。　　此前中国山东网曾报道，被国家明令叫停的设置购房门槛的情况又在济南出现。为此，济南市住建委，住建委的工作人员向中国山东网明确表示，选择全款购买还是贷款购买是购房人的基本权利，开发商不得刻意设置购房门槛限制购买，更不允许以捆绑地下室或者捆绑车位的形式进行销售，此类行为一经查处，济南市住建委将对该楼盘进行包括吊销预售证，拉入诚信黑名单等一系列处罚，维护济南房地产市场的平稳。'''

    # initialize the CHinese stopwords.
    sys.path.append("textteaser")
    sys.path.insert(1, "..")
    # stopWordsPath = os.path.dirname(os.path.abspath(__file__)) + '/textteaser_Chinese/trainer/stopWords.txt'
    stopWordsPath = "doc_summarizer/textteaser_Chinese/trainer/stopWords.txt"

    tt = TextTeaserChinese(stopWordsPath, text)
    sentences = tt.summarize(title, text)
    summary = ""
    for sentence in sentences:
        summary += sentence
    assert summary != ""
