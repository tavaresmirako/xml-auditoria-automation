import json
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

from lxml import etree


class XMLAuditProcessor:
    """Extracts, transforms and exports data from compact XML files."""

    def __init__(self, xml_path: str):
        self.xml_path = xml_path

    def extract_with_xpath(self) -> dict[str, Any]:
        parser = etree.XMLParser(remove_blank_text=True, recover=True)
        tree = etree.parse(self.xml_path, parser)

        return {
            "numero_nota": self._get_text(tree, "//*[local-name()='infNFe']/*[local-name()='ide']/*[local-name()='nNF']"),
            "serie": self._get_text(tree, "//*[local-name()='infNFe']/*[local-name()='ide']/*[local-name()='serie']"),
            "data_emissao": self._get_text(tree, "//*[local-name()='infNFe']/*[local-name()='ide']/*[local-name()='dhEmi']"),
            "cnpj_emitente": self._get_text(tree, "//*[local-name()='infNFe']/*[local-name()='emit']/*[local-name()='CNPJ']"),
            "nome_emitente": self._get_text(tree, "//*[local-name()='infNFe']/*[local-name()='emit']/*[local-name()='xNome']"),
            "cnpj_destinatario": self._get_text(tree, "//*[local-name()='infNFe']/*[local-name()='dest']/*[local-name()='CNPJ']"),
            "cpf_destinatario": self._get_text(tree, "//*[local-name()='infNFe']/*[local-name()='dest']/*[local-name()='CPF']"),
            "nome_destinatario": self._get_text(tree, "//*[local-name()='infNFe']/*[local-name()='dest']/*[local-name()='xNome']"),
            "valor_total": self._get_text(tree, "//*[local-name()='infNFe']/*[local-name()='total']/*[local-name()='ICMSTot']/*[local-name()='vNF']"),
            "chave_acesso": self._extract_access_key(tree),
            "produtos": self._extract_products(tree),
        }

    def _get_text(self, tree: etree._ElementTree, xpath: str) -> str | None:
        result = tree.xpath(xpath)

        if not result:
            return None

        item = result[0]
        return item.text if hasattr(item, "text") else str(item)

    def _extract_access_key(self, tree: etree._ElementTree) -> str | None:
        result = tree.xpath("//*[local-name()='infNFe']/@Id")

        if not result:
            return None

        return result[0].replace("NFe", "")

    def _extract_products(self, tree: etree._ElementTree) -> list[dict[str, Any]]:
        products = []
        items = tree.xpath("//*[local-name()='infNFe']/*[local-name()='det']")

        for item in items:
            products.append(
                {
                    "numero_item": item.get("nItem"),
                    "codigo": self._get_text_from_node(item, ".//*[local-name()='prod']/*[local-name()='cProd']"),
                    "descricao": self._get_text_from_node(item, ".//*[local-name()='prod']/*[local-name()='xProd']"),
                    "ncm": self._get_text_from_node(item, ".//*[local-name()='prod']/*[local-name()='NCM']"),
                    "cfop": self._get_text_from_node(item, ".//*[local-name()='prod']/*[local-name()='CFOP']"),
                    "quantidade": self._get_text_from_node(item, ".//*[local-name()='prod']/*[local-name()='qCom']"),
                    "valor_unitario": self._get_text_from_node(item, ".//*[local-name()='prod']/*[local-name()='vUnCom']"),
                    "valor_total": self._get_text_from_node(item, ".//*[local-name()='prod']/*[local-name()='vProd']"),
                }
            )

        return products

    def _get_text_from_node(self, node: etree._Element, xpath: str) -> str | None:
        result = node.xpath(xpath)

        if not result:
            return None

        item = result[0]
        return item.text if hasattr(item, "text") else str(item)

    def append_audit_marker(self, output_path: str) -> str:
        tree = ET.parse(self.xml_path)
        root = tree.getroot()
        inf_nfe = self._find_by_local_name(root, "infNFe")

        if inf_nfe is not None:
            audit = ET.Element("auditoriaSistema")

            status = ET.SubElement(audit, "status")
            status.text = "PROCESSADO"

            source = ET.SubElement(audit, "origem")
            source.text = "AUTOMACAO_PYTHON_GOOGLE_DRIVE"

            inf_nfe.append(audit)

        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        tree.write(output_path, encoding="utf-8", xml_declaration=True)

        return output_path

    def _find_by_local_name(self, root: ET.Element, local_name: str) -> ET.Element | None:
        for element in root.iter():
            tag = element.tag.split("}")[-1]

            if tag == local_name:
                return element

        return None

    def save_json(self, payload: dict[str, Any], output_path: str) -> str:
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, "w", encoding="utf-8") as file:
            json.dump(payload, file, ensure_ascii=False, indent=4)

        return output_path
