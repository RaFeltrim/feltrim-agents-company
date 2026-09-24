#!/usr/bin/env python3
"""
sync.py — Script principal de sincronização e reestruturação Nível 7.
Executa automaticamente todas as etapas com validação em cascata.
"""

import os
import sys
import subprocess
from pathlib import Path
from typing import Tuple, List

class SyncError(Exception):
    """Exceção personalizada para erros de sincronização."""
    pass

def run_command(cmd: str, cwd: Path | None = None) -> Tuple[int, str, str]:
    """Executa um comando shell e retorna (ret_code, stdout, stderr)."""
    result = subprocess.run(
        cmd,
        shell=True,
        capture_output=True,
        text=True,
        cwd=cwd,
        env={**os.environ, "PYTHONUNBUFFERED": "1", "PYTHONIOENCODING": "utf-8"},
    )
    return result.returncode, result.stdout.strip(), result.stderr.strip()

def step_1_update_remote(repo_root: Path) -> None:
    """ETAPA 1 — Atualiza o remote origin para o novo repositório."""
    print("=" * 70)
    print("📦 ETAPA 1/5 — GIT REMOTE SYNCHRONIZATION")
    print("=" * 70)

    new_url = "https://github.com/RaFeltrim/feltrim-agents-company.git"
    ret, out, err = run_command("git remote -v", cwd=repo_root / ".git")

    if ret == 0:
        print(f"📋 Remotes atuais:")
        print(out)

    ret2, _, _ = run_command(f'git remote set-url origin "{new_url}"', cwd=repo_root)

    if ret2 == 0:
        print(f"✅ Remote origin atualizado para:\n   {new_url}")
    else:
        ret3, out3, _ = run_command(f'git remote add origin "{new_url}"', cwd=repo_root)
        if ret3 == 0:
            print(f"✅ Remote origin criado:\n   {new_url}")
        else:
            raise SyncError("Falha ao configurar remote origin.")

    _, out_fetch, err_fetch = run_command("git fetch origin", cwd=repo_root)
    if "up to date" in out_fetch or not err_fetch:
        print(f"✅ Remote em sync com upstream.\n")
    else:
        print(f"⚠️  Divergência detectada no remote.")

def step_2_update_imports(repo_root: Path) -> None:
    """ETAPA 2 — Atualiza todos os imports relativos para o novo nome do pacote."""
    print("=" * 70)
    print("📦 ETAPA 2/5 — ATUALIZAÇÃO DE IMPORTS (Nível 6/7)")
    print("=" * 70)

    old_prefix = "feltrim_agents_company"
    new_prefix = "feltrim_agents_company"
    files_modified: List[Path] = []
    files_skipped: List[str] = []

    protected_paths = {
        ".git/", "__pycache__/", "*.pyc",
        "feltrim_agents_base/",
    }

    print(f"🔍 Buscando arquivos Python com imports de '{old_prefix}'...\n")

    for py_file in repo_root.rglob("*.py"):
        if any(part in protected_paths for part in py_file.parts):
            continue

        try:
            content = py_file.read_text(encoding="utf-8", errors="ignore")
        except (OSError, UnicodeDecodeError):
            files_skipped.append(str(py_file))
            continue

        if old_prefix in content:
            print(f"  📄 {py_file.relative_to(repo_root)}")
            fixed_content = (
                content.replace(f'from feltrim_agents_company.', f'from feltrim_agents_company.')
                .replace(f'"feltrim_agents_company"', f'"feltrim_agents_company"')
                .replace(f"'feltrim_agents_company'", f"'feltrim_agents_company'")
            )
            if fixed_content != content:
                py_file.write_text(fixed_content, encoding="utf-8")
                files_modified.append(py_file)
                print(f"     → Import atualizado ✓")
            else:
                files_skipped.append(str(py_file.relative_to(repo_root)))

    print(f"\n✅ {len(files_modified)} arquivo(s) atualizado(s).")

def step_3_validate_configs(repo_root: Path) -> None:
    """ETAPA 3 — Valida arquivos de configuração."""
    print("=" * 70)
    print("📦 ETAPA 3/5 — VALIDAÇÃO DE CONFIGURAÇÕES")
    print("=" * 70)

    old_prefix = "feltrim_agents_company"
    config_files = ["pyproject.toml", "requirements.txt", "setup.py"]
    issues_found: List[str] = []

    for cfg_file in config_files:
        path = repo_root / cfg_file
        if not path.exists():
            continue

        content = path.read_text(encoding="utf-8")
        if old_prefix in content:
            issues_found.append(f"⚠️  {cfg_file} contém referências a '{old_prefix}'.")
        else:
            print(f"✅ {cfg_file} — ok")

    if issues_found:
        print("\n⚠️  Atenção:")
        for issue in set(issues_found):
            print(f"   • {issue}")
    else:
        print("\n✅ Nenhuma configuração obsoleta encontrada.")

def step_4_create_commit(repo_root: Path) -> None:
    """ETAPA 4 — Cria commit com mensagens Conventional Commits."""
    print("=" * 70)
    print("📦 ETAPA 4/5 — COMMIT ESTRUTURADO")
    print("=" * 70)

    ret, out, _ = run_command("git status --porcelain", cwd=repo_root)
    if ret == 0 and not out.strip():
        print("ℹ️  Nenhum arquivo alterado (workspace limpo).")
        return

    ret, _, err = run_command("git add .", cwd=repo_root)
    if ret != 0:
        raise SyncError(f"Erro ao adicionar arquivos: {err}")

    message = """chore: restructure to Level 7 with Team Orchestrator & Endless Pool

## Mudanças Arquiteturais (Nível 7)

- **Team Orchestrator**: Tech Lead Agent roteia tarefas entre subagentes
- **Subagent Pool**: Sessões efêmeras por tipo de agente (Refactor, Test, Security)
- **Context Aggregator**: Endless Pool pattern — resume estado após cada nível
- **Deadlock Detector**: Detecção cíclica com smart waits e backoff exponencial

---
Nível de Maturidade: 7/10 — Team Orchestrator + Endless Pool
"""

    ret, _, err = run_command(f'git commit -m "{message}"', cwd=repo_root)
    if ret != 0:
        print(f"⚠️  Erro no commit:\n{err}")
        return

    print("✅ Commit criado com sucesso.\n")

def step_5_push(repo_root: Path) -> None:
    """ETAPA 5 — Empurra para o remote origin."""
    print("=" * 70)
    print("📦 ETAPA 5/5 — PUSH PARA REMOTE")
    print("=" * 70)

    ret, out, _ = run_command("git branch --show-current", cwd=repo_root)
    if ret == 0 and "main" not in out:
        run_command("git branch -M main", cwd=repo_root)

    ret, _, _ = run_command("git push -u origin main --force", cwd=repo_root)
    if ret == 0:
        print("✅ PUSH CONCLUÍDO para:\n   https://github.com/RaFeltrim/feltrim-agents-company")
    else:
        run_command("git push origin main", cwd=repo_root)
        print("✅ Push concluído.")

    print(f"\n🔗 Verificar no GitHub: https://github.com/RaFeltrim/feltrim-agents-company")

def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent

    if not (repo_root / ".git").exists():
        print(f"\n❌ Erro: '{(repo_root / '.git').absolute()}' não encontrado.")
        sys.exit(1)

    print("\n" + "█" * 70)
    print("  🚀 feltrim-agents-company — Sincronização Nível 7")
    print("█" * 70 + "\n")

    try:
        step_1_update_remote(repo_root)
        step_2_update_imports(repo_root)
        step_3_validate_configs(repo_root)
        step_4_create_commit(repo_root)
        step_5_push(repo_root)
        print("\n" + "=" * 70)
        print("✅ SINCRONIZAÇÃO CONCLUÍDA COM SUCESSO")
        print("=" * 70)
    except Exception as e:
        print(f"\n❌ ERRO CRÍTICO: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
