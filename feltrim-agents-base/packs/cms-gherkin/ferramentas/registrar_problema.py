from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
REPORT_PATH = ROOT / "MEMORIA-OPERACIONAL" / "PROBLEMAS-E-SOLUCOES.md"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Registra problemas e solucoes na memoria operacional do projeto."
    )
    parser.add_argument("--titulo", required=True)
    parser.add_argument("--contexto", required=True)
    parser.add_argument("--causa", required=True)
    parser.add_argument("--solucao", required=True)
    parser.add_argument("--prevencao", default="Nao informado.")
    parser.add_argument("--categoria", default="Operacional")
    parser.add_argument("--status", default="Resolvido")
    parser.add_argument(
        "--arquivos",
        nargs="*",
        default=[],
        help="Lista de arquivos relacionados ao problema.",
    )
    args = parser.parse_args()

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    if not REPORT_PATH.exists():
        REPORT_PATH.write_text(default_report_header(), encoding="utf-8")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    related_files = ", ".join(args.arquivos) if args.arquivos else "Nao informado."

    entry = [
        "",
        f"## {args.titulo}",
        "",
        f"- Data: `{timestamp}`",
        f"- Categoria: `{args.categoria}`",
        f"- Status: `{args.status}`",
        f"- Arquivos relacionados: `{related_files}`",
        "",
        "### Contexto",
        "",
        args.contexto,
        "",
        "### Causa raiz",
        "",
        args.causa,
        "",
        "### Solucao aplicada",
        "",
        args.solucao,
        "",
        "### Prevencao",
        "",
        args.prevencao,
        "",
    ]

    with REPORT_PATH.open("a", encoding="utf-8") as handle:
        handle.write("\n".join(entry))

    print(f"[ok] Problema registrado em {REPORT_PATH.relative_to(ROOT)}")
    return 0


def default_report_header() -> str:
    return """# Problemas e Solucoes

Este arquivo consolida o historico operacional do projeto.

Registre aqui:
- problemas recorrentes
- causa raiz
- solucao aplicada
- forma de prevencao
"""


if __name__ == "__main__":
    raise SystemExit(main())
