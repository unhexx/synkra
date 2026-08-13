# GitOps Tools & Recommendations for Synkra (2026 Best Practices)

## Recommended Stack

### Primary (Cloud-native, Kubernetes)
1. **Flux CD** (preferred for GitOps purity)  
   - Continuous reconciliation from Git  
   - Image automation (ImageRepository + ImagePolicy + ImageUpdateAutomation)  
   - Multi-tenancy and progressive delivery support  
   - Official CNCF project, excellent for agentic / GitOps-first workflows

2. **Argo CD**  
   - Strong UI and ApplicationSet  
   - Good for multi-cluster and progressive delivery (Argo Rollouts)  
   - Widely adopted in enterprise

### Supporting Tools
- **GitHub Actions** — CI, image build/push to GHCR, create release tags, update kustomize/helm values
- **Kustomize** (or Helm) — manifest management
- **Sealed Secrets / External Secrets Operator** — secrets management
- **Kyverno or OPA Gatekeeper** — policy-as-code
- **Prometheus + Grafana + OpenTelemetry** — observability of the GitOps loop itself

### Local / Lightweight alternative
- **Skaffold** or **Tilt** for local iteration
- **kind / k3d / minikube** for local production-like testing of manifests

## Recommended GitOps Flow for Synkra
1. Feature branch → PR → CI (lint/test/build)
2. Merge to `main` → auto-build & push image to GHCR with tag `main-<sha>` and semver on release
3. Flux / Argo CD watches `deploy/` or `k8s/` directory (or a separate gitops repo)
4. Image automation updates the image tag in the GitOps repo
5. Cluster reconciles and rolls out new version
6. Optional: canary / progressive delivery via Argo Rollouts or Flagger

## Agent Guidance
When implementing T-012 / T-013:
- Prefer Flux CD for pure GitOps
- Keep manifests in `k8s/` or `deploy/` with clear environments (dev/staging/prod)
- Use Kustomize overlays
- Document the exact Flux bootstrap commands in docs/DEVELOPMENT.md or a new docs/DEPLOYMENT.md
